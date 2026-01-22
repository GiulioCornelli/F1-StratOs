#librerie esterne
from typing import Optional

# librerie custom 
from ..models.driver import Driver
from ..database import MongoManager

class DriverRepository:
    def __init__(self):
        self.db = MongoManager.get_db()
        self.collection = self.db["Drivers"]
    

    ## ------------Search Functions  -----------------
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

    def get_all_drivers(self)-> list[Driver]:
        """
        Description:
            Funzione che permette di recuperare tutti i piloti presenti nel db
        Returns:
            list[Driver]: lista di tutti i piloti presenti nel db
        """
        drivers = []
        
        try:
            data = self.collection.find()
            for item in data:
                item.pop("_id", None)
                drivers.append(Driver(**item))
            return drivers
        except Exception as e:
            print(f"Errore nel recupero del driver errore: {e}")
            return drivers


    ## ------------Insert Functions  -----------------    

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
        
    def insert_many_drivers(self, drivers: list[Driver]) -> bool:
        """
        Description:
            Questa funzione permette di inserire una lista di diriver nel db

        Args:
            drivers (list[Driver]): lista di piloti da inserire

        Returns:
            bool: conferma se la trasazione è andata a buon fine
        """
        try:
            data = [driver.model_dump() for driver in drivers]
            self.collection.insert_many(data)
            return True
        except Exception as e:
            print(f"Errore nell'inserimento dei driver errore: {e}")
            return False

    ## ------------Update Functions  -----------------

    ## ------------Delete Functions  -----------------
    def delete_all_drivers(self) -> bool:
        """
        Description:
            elimina tutti i piloti dal db

        Returns:
            bool: valore di conferma (treu: trasazione riuscita con successo)
        """
        try:
            self.collection.delete_many({})
            return True
        except Exception as e:
            print(f"Errore nell'eliminazione dei driver errore: {e}")
            return False
        
    def delete_driver_by_nuber(self, driver_number: int) -> bool:
        """
        Description:
            elimina un driver in base al suo numero

        Args:
            driver_number (int): numero del pilota in gara

        Returns:
            bool: conferma se la trasazione è andata a buon fine
        """
        try:
            self.collection.delete_one({"driver_number": driver_number})
            return True
        except Exception as e:
            print(f"Errore nell'eliminazione del driver errore: {e}")
            return False