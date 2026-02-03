#!/bin/bash

# F1-StratOs Ultra-Launcher
# Version: 2.2
# Author: Antigravity

# Set colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to handle shutdown
cleanup() {
    echo -e "\n${RED}🛑 Shutting down F1-StratOs...${NC}"
    # Kill all background processes spawned by this script
    pkill -P $$ > /dev/null 2>&1
    echo -e "${GREEN}✅ All backend processes stopped.${NC}"
    exit
}

# Trap SIGINT (Ctrl+C)
trap cleanup SIGINT

ROOT_DIR=$(pwd)

echo -e "${BLUE}🏎️  F1-StratOS | THE ULTIMATE STARTUP${NC}"
echo -e "------------------------------------------------"

# 1. Dependency check helper
get_docker_compose() {
    if docker compose version >/dev/null 2>&1; then
        echo "docker compose"
    elif docker-compose version >/dev/null 2>&1; then
        echo "docker-compose"
    else
        echo ""
    fi
}

DOCKER_COMPOSE_CMD=$(get_docker_compose)

echo -e "${YELLOW}🔍 Checking dependencies...${NC}"
if [ -z "$DOCKER_COMPOSE_CMD" ]; then
    echo -e "${RED}❌ Docker Compose is required but not installed.${NC}"
    exit 1
fi

command -v npm >/dev/null 2>&1 || { echo -e "${RED}❌ npm is required but not installed.${NC}" >&2; exit 1; }
echo -e "${GREEN}✅ Dependencies satisfied.${NC}"

# 2. Start PostgreSQL & MongoDB
echo -e "${YELLOW}🐘 Starting Databases (PostgreSQL & MongoDB)...${NC}"
cd "$ROOT_DIR"
$DOCKER_COMPOSE_CMD up -d --build --quiet-pull > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Databases are up.${NC}"
else
    echo -e "${RED}❌ Failed to start Databases. Check if Docker is running.${NC}"
    exit 1
fi

# Wait for Auth service to be ready and initialize
(
    echo -e "${YELLOW}🛠️  Initializing Database Records...${NC}"
    # Wait for port 8000 to be open
    while ! nc -z localhost 8000; do   
      sleep 0.5
    done
    curl -s -X POST http://localhost:8000/init-privileges > /dev/null
    echo -e "${GREEN}✅ Auth database initialized.${NC}"
) &

# Wait for MongoDB service to be ready and populate drivers from OpenF1 API
(
    echo -e "${YELLOW}🏎️  Initializing Driver Data from OpenF1 API...${NC}"
    # Wait for port 8080 to be open
    while ! nc -z localhost 8080; do   
      sleep 0.5
    done
    # Check if drivers exist
    driver_count=$(curl -s http://localhost:8080/api/drivers/getAllDrivers 2>/dev/null | jq 'length' 2>/dev/null || echo "0")
    if [ "$driver_count" -eq 0 ]; then
        python3 "$ROOT_DIR/init_drivers.py" 2>&1 | while read line; do
            echo "   $line"
        done
    else
        echo -e "${GREEN}✅ Drivers already in database ($driver_count found).${NC}"
    fi
) &

# 3. Start Backend Services
echo -e "${YELLOW}📡 Starting Microservices...${NC}"

services=(
    "Backend/postgres-Stalker_au:8000:Auth"
    "Backend/Mongo-Stalker:8080:MongoData"
    "Backend/OPF1-Stalker:8090:Logic"
    "Backend/Gateway:8070:EntryPoint"
)

# Kill any existing processes on these ports to avoid conflicts
for entry in "${services[@]}"; do
    IFS=":" read -r path port name <<< "$entry"
    # Try to free the port (Linux)
    fuser -k ${port}/tcp > /dev/null 2>&1 || true
done

for entry in "${services[@]}"; do
    IFS=":" read -r path port name <<< "$entry"
    echo -e "   🚀 Starting ${BLUE}$name${NC} on port ${YELLOW}$port${NC}..."
    cd "$ROOT_DIR/$path"
    
    # Run using venv python if available, otherwise system python3
    if [ -f "venv/bin/python" ]; then
        ./venv/bin/python main.py > "$ROOT_DIR/logs_${name,,}.log" 2>&1 &
    else
        python3 main.py > "$ROOT_DIR/logs_${name,,}.log" 2>&1 &
    fi
    
    # Give a tiny bit of time between starts
    sleep 1
done

# 4. Start Frontend
echo -e "${YELLOW}💻 Starting Frontend (Vite)...${NC}"
cd "$ROOT_DIR/Frontend"
# Kill existing vite process on 5173
fuser -k 5173/tcp > /dev/null 2>&1 || true
npm run dev > "$ROOT_DIR/logs_frontend.log" 2>&1 &
echo -e "${GREEN}✅ Frontend dev server triggered.${NC}"

echo -e "------------------------------------------------"
echo -e "${GREEN}✨ F1-StratOs is now ENGINE START!${NC}"
echo -e "------------------------------------------------"
echo -e "🏁 ${BLUE}Gateway:${NC}   http://localhost:8070"
echo -e "📺 ${BLUE}Frontend:${NC}  http://localhost:5173"
echo -e "🐘 ${BLUE}Database:${NC}  PostgreSQL (Port 5432)"
echo -e "------------------------------------------------"
echo -e "${YELLOW}📝 Logs Available:${NC} logs_*.log in root"
echo -e "${YELLOW}⌨️  Press Ctrl+C to stop the entire grid.${NC}"

# Keep alive to catch Ctrl+C
wait
