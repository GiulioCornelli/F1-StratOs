
import sys
import os
from sqlalchemy import create_engine, text

# Usa la stessa connection string di main.py o default
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:Jj00@localhost:5432/f1stratos")

def test_connection():
    print(f"Testing connection to: {DATABASE_URL}...")
    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("Connection successful!", result.scalar())
        return 0
    except Exception as e:
        print(f"Connection failed: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(test_connection())
