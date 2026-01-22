#librerie esterne
import re
from fastapi import APIRouter ,HTTPException, status
from typing import Optional

# librerie custom
from ..database.repositories.driverRepository import DriverRepository
from ..database.models.driver import Driver



routerDriver = APIRouter(prefix="/api/drivers" , tags=["drivers"])

repo = DriverRepository()#impoert della repository driver

@routerDriver.get("/getDriverByNumber", response_model=Driver)
async def get_driver_by_number(number : int)-> Driver:
    """
    Description:

    Questa edpoint api permette di ottenere un pilota(se esiste) tramite il suo numero in gara

    Args:
        number (int): numero del pilota

    Raises:
        HTTPException: 404 Driver non trovato
        HTTPException: 50* Problemi interni

    Returns:
        Driver: eventuali dati del pilota 
    """
    try:
        data : Optional[Driver] = repo.get_driver_by_number(number)
        print(data)
        if data is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Driver numero:{number} non trovato"
            )
        return data

    except Exception as e:
        print(f"Errore interno: {e}") 
        
        # 500 Internal Server Error per errori imprevisti (es. database offline)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Si è verificato un errore interno nel server."
        )
        

@routerDriver.get("/getAllDrivers", response_model=list[Driver])
async def getall_drivers()-> list[Driver]:
    """
    Description:
        Questa endpoint api permette di ottenere tutti i piloti presenti nel database

    Raises:
        HTTPException: 500 Problemi interni

    Returns:
        list[Driver]: lista di tutti i piloti
    """
    try:
        data : list[Driver] = repo.get_all_drivers()
        return data

    except Exception as e:
        print(f"Errore interno: {e}") 
        
        # 500 Internal Server Error per errori imprevisti (es. database offline)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Si è verificato un errore interno nel server."
        )
    

@routerDriver.post("/insertDriver", response_model=bool)
async def isert_driver(driver: Driver)-> bool:
    """
    Description 
        Questa endpoint api permette di inserire un nuovo pilota nel database
    Args:
        driver (Driver): nuovo pilota da inserire

    Raises:
        HTTPException: nel caso di errori interni

    Returns:
        bool: True se l'inserimento è avvenuto con successo
    """
    try:
        print(driver)
        result : bool = repo.insert_driver(driver)
        return result
    except Exception as e:
        print(f"Errore interno: {e}") 
        
        # 500 Internal Server Error per errori imprevisti (es. database offline)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Si è verificato un errore interno nel server."
        )
        