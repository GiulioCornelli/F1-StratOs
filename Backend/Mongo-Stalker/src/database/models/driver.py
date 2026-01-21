from pydantic import BaseModel, Field
from typing import Optional

class Driver(BaseModel): # Così facendo diamo uno sche ai dati in ingresso e in uscita per MongoDB
    
    meeting_key: int = Field(..., description="l'identificativo univoco del pilota nella sessione")
    session_key: int = Field(..., description="l'identificativo univoco della sessione")
    driver_number: int = Field(..., description="il numero identificativo del pilota")
    broadcast_name: str = Field(..., description="il nome del pilota come appare in TV")
    full_name: str = Field(..., description="il nome completo del pilota")
    name_acronym: str = Field(..., description="l'acronimo del nome del pilota")
    team_name: str = Field(..., description="il nome del team del pilota")    
    team_colour: Optional[str] = Field(None, description="il colore del team del pilota")
    first_name: str = Field(..., description="il nome del pilota")
    last_name: str = Field(..., description="il cognome del pilota")
    headshot_url: Optional[str] = Field(None, description="l'url dell'immagine del pilota") 
    country_code: Optional[str] = Field(None, description="il codice della nazione del pilota")
