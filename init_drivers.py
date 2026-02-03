#!/usr/bin/env python3
"""
Script to fetch real F1 driver data from OpenF1 API and populate MongoDB.
This ensures the database has real, up-to-date driver information.
"""

import requests
import sys

def fetch_drivers_from_api():
    """Fetch latest driver data from OpenF1 API"""
    print("🔍 Fetching drivers from OpenF1 API...")
    
    try:
        # Get latest session data
        response = requests.get("https://api.openf1.org/v1/drivers?session_key=latest")
        response.raise_for_status()
        drivers = response.json()
        
        if not drivers:
            print("⚠️  No drivers found in latest session, trying alternative...")
            # Try getting from a specific recent session
            response = requests.get("https://api.openf1.org/v1/drivers?session_key=9839")
            response.raise_for_status()
            drivers = response.json()
        
        print(f"✅ Found {len(drivers)} drivers from OpenF1 API")
        return drivers
    
    except Exception as e:
        print(f"❌ Error fetching from OpenF1 API: {e}")
        return None

def insert_drivers_to_mongo(drivers):
    """Insert drivers into MongoDB via the Mongo-Stalker API"""
    print("📤 Inserting drivers into MongoDB...")
    
    try:
        response = requests.post(
            "http://localhost:8080/api/drivers/insertManyDrivers",
            json=drivers,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200 and response.json() == True:
            print(f"✅ Successfully inserted {len(drivers)} drivers into MongoDB")
            return True
        else:
            print(f"❌ Failed to insert drivers: {response.text}")
            return False
    
    except Exception as e:
        print(f"❌ Error inserting to MongoDB: {e}")
        return False

def main():
    print("🏎️  F1-StratOS Driver Data Initializer")
    print("=" * 50)
    
    # Fetch drivers from OpenF1 API
    drivers = fetch_drivers_from_api()
    
    if not drivers:
        print("❌ Could not fetch drivers from API. Exiting.")
        sys.exit(1)
    
    # Insert into MongoDB
    success = insert_drivers_to_mongo(drivers)
    
    if success:
        print("=" * 50)
        print("✅ Driver data initialization complete!")
        sys.exit(0)
    else:
        print("=" * 50)
        print("❌ Driver data initialization failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
