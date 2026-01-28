#librerie esterne
from fastapi import APIRouter ,HTTPException, status
from typing import Optional
import httpx

#librerie custom
from ..models import Driver


routerDriver = APIRouter(prefix="/api/drivers", tags=["Drivers"])


## ------------Search Functions  -----------------

@routerDriver.get("/getAllDrivers")
async def getAllDrivers() -> list[Driver]:
    """
    Description:
        Questo endpoint api permette di ottenere tutti i piloti presenti nel database

    Raises:
        HTTPException: nel caso di errori interni

    Returns:
        list[Driver]: lista di tutti i piloti
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("http://127.0.0.1:8080/api/drivers/getAllDrivers")
        
        data : list[Driver] = response.json()
        return data

    except Exception as e:
        print(f"Errore interno: {e}") 
        
        # 500 Internal Server Error per errori imprevisti (es. database offline)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Si è verificato un errore interno nel server."
        )

@routerDriver.get("/getDriverByNumber")
async def getDriverByNumber(number : int) -> Optional[Driver]:
    """
    Description:
        Questo endpoint api permette di ottenere un pilota(se esiste) tramite il suo numero in gara

    Args:
        number (int): numero del pilota

    Raises:
        HTTPException: nel caso di errori interni

    Returns:
        Optional[Driver]: eventuali dati del pilota 
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("http://127.0.0.1:8080/api/drivers/getDriverByNumber", params={"number": number})
        
        data : Driver = response.json()
        print(data)
        return data

    except Exception as e:
        print(f"Errore interno: {e}") 
        
        # 500 Internal Server Error per errori imprevisti (es. database offline)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Si è verificato un errore interno nel server."
        )