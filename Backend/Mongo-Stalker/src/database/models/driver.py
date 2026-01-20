from pydantic import BaseModel, Field
from typing import Optional

class Driver(BaseModel): # Così facendo diamo uno sche ai dati in ingresso e in uscita per MongoDB
    brodcast_name: str = Field(..., description="il nome del pilota come appare in TV")
    country_code: Optional[str] = Field(None, description="il codice della nazione del pilota")
    driver_number: int = Field(..., description="il numero identificativo del pilota")
    first_name: str = Field(..., description="il nome del pilota")
    full_name: str = Field(..., description="il nome completo del pilota")
    headshot: Optional[str] = Field(None, description="l'url dell'immagine del pilota")
    meeting_key: int = Field(..., description="l'identificativo univoco del pilota nella sessione")
    name_acronym: str = Field(..., description="l'acronimo del nome del pilota")
    session_key: int = Field(..., description="l'identificativo univoco della sessione")
    team_color: Optional[str] = Field(None, description="il colore del team del pilota")
    team_name: str = Field(..., description="il nome del team del pilota")