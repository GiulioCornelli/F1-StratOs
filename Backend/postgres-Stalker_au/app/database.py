import os
import sys
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurazione connection string
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:Jj00@localhost:5432/f1stratos")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dipendenza per ottenere la sessione DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_connection():
    print(f"Testing connection to: {DATABASE_URL}...")
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("Connection successful!", result.scalar())
        return 0
    except Exception as e:
        print(f"Connection failed: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(test_connection())
