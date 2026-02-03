# F1-StratOS Driver Data Management

## Overview
F1-StratOS automatically fetches **real, live F1 driver data** from the official OpenF1 API, including:
- Driver names and numbers
- Team information and colors
- Official headshot photos
- Country codes and more

## Data Source
**OpenF1 API**: https://openf1.org/

The system uses the latest F1 session data to ensure drivers, teams, and photos are always up-to-date.

## How It Works

### Automatic Initialization
When you start the project with `./start_all.sh`, the system automatically:
1. Checks if driver data exists in MongoDB
2. If empty, fetches the latest drivers from OpenF1 API
3. Populates the database with real F1 driver data

### Manual Update
To manually refresh driver data:

```bash
# Delete existing drivers (optional)
curl -X DELETE http://localhost:8080/api/drivers/deleteAllDrivers

# Fetch latest data from OpenF1 API
python3 init_drivers.py
```

## File Structure
- `init_drivers.py` - Python script that fetches from OpenF1 API and populates MongoDB
- `start_all.sh` - Startup script that auto-initializes driver data if needed

## API Endpoints
- **Get All Drivers**: `GET http://localhost:8070/api/drivers/getAllDrivers`
- **Get Driver by Number**: `GET http://localhost:8070/api/drivers/getDriverByNumber?number=1`

## Notes
- Driver photos are high-quality images from Formula1.com
- Data includes all 20 current F1 drivers
- Updates automatically pull the latest session data
