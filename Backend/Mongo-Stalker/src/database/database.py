#librerie esterne
from pymongo import MongoClient
import os 
from dotenv import load_dotenv
from requests.utils import requote_uri


class MongoManager:
    _client = None

    @classmethod
    def get_client(cls):
        """
        Description:
            Crea il clinet per la connessione al DB
        Returns:
            _type_: MongoClient
        """
        if cls._client is None:
            load_dotenv()
            db_user = os.getenv("F1_APP_USER")
            db_pwd = os.getenv("F1_APP_PASSWORD")
            ip_database = os.getenv("IP_DATABASE_MD")
            port_database = os.getenv("PORT_DATABASE_MD")

            if db_user and db_pwd:
                url = f"mongodb://{db_user}:{db_pwd}@{ip_database}:{port_database}/f1stratos_db?authSource=f1stratos_db"
                parsurl = requote_uri(url)
                print(f"Tentativo di connessione a: {parsurl}")
            else:
                url = f"mongodb://{ip_database}:{port_database}/f1stratos_db?authSource=f1stratos_db"
                parsurl = requote_uri(url)
                print(f"Tentativo di connessione a: {parsurl}")

            cls._client = MongoClient(parsurl)
        
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
    
    @classmethod
    def close_connection(cls):
        """Chiude la connessione in modo sicuro."""
        if cls._client is not None:
            cls._client.close()
            cls._client = None  

