from typing import Optional
from ..models.driver import Driver
from ..database import MongoManager

class DriverRepository:
    def __init__(self):
        self.db = MongoManager.get_db()
        self.collection = self.db["Drivers"]
    
    def get_driver_by_number(self, driver_number: int) -> Optional[Driver]:
        """
        Description:

            Funzione che permette di cercare nel db un driver, in base al suo numero

        Args:
            driver_number (int): Numero del pilota che vinene usato in gara

        Returns:
            Optional[Driver]: se esiste ti riporterà il driver con tutte le sue caratteristiche
        """
        try:
            data = self.collection.find_one({"driver_number": driver_number})
            if data:
                data.pop("_id", None)
                return Driver(**data)
            return None
        except Exception as e:
            print(f"Errore nel recupero del driver errore: {e}")
            return None
            
    def insert_driver(self, driver: Driver) -> bool:
        """
        Description:
            inserisce un driver nel db

        Args:
            driver (Driver): nuovo driver da inserire
        Returns:
            bool: valore di conferma (treu: trasazione riuscita con successo)
        """
        try:
            data = driver.model_dump()
            self.collection.insert_one(data)
            return True
        except Exception as e:
            print(f"Errore nell'inserimento del driver errore: {e}")
            return False