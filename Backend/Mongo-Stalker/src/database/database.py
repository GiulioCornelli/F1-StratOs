from pymongo import MongoClient
import os 
from dotenv import load_dotenv

class MongoManager:
    _client = None

    @classmethod
    def get_client(cls):
        """
            Crea il clinet per la connessione al DB
        Returns:
            _type_: MongoClient
        """
        if cls._client is None:
            load_dotenv()
            db_user = os.getenv("APP_USER")
            db_pwd = os.getenv("APP_PASSWORD")
            ip_database = os.getenv("IP_DATABASE")
            port_database = os.getenv("PORT_DATABASE")

            if db_user and db_pwd:
                url = f"mongodb://{db_user}:{db_pwd}@{ip_database}:{port_database}/"
                print(f"Tentativo di connessione a: {url}")
            else:
                url = f"mongodb://{ip_database}:{port_database}/"

            cls._client = MongoClient(url)
        
        return cls._client

    @classmethod
    def get_db(cls):
        """
            Ritorna il databese specifico, in questo caso f1stratos_db
        Returns:
            _type_: MongoClinet[Database]
        """
        client = cls.get_client()
        return client["f1stratos_db"]
    


