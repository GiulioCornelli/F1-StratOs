from database.repositories.driverRepository import DriverRepository
from database.models.driver import Driver

driver_data = {
    "brodcast_name": "M VERSTAPPEN",  # Allineato a 'brodcast_name' del modello
    "country_code": "NED",
    "driver_number": 1,
    "first_name": "Max",
    "full_name": "Max VERSTAPPEN",
    "headshot": "https://www.formula1.com/content/dam/fom-website/drivers/M/MAXVER01_Max_Verstappen/maxver01.png.transform/1col/image.png",
    "meeting_key": 1219,
    "name_acronym": "VER",
    "session_key": 9158,
    "team_color": "3671C6",           # Allineato a 'team_color' del modello
    "team_name": "Red Bull Racing"
}

d = Driver(**driver_data)

repo = DriverRepository()
repo.insert_driver(d)