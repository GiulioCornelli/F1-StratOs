# librerie esterne
from fastapi import FastAPI
from contextlib import asynccontextmanager
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import httpx
from httpx import ConnectTimeout, ReadTimeout
import asyncio

## test grafico
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn


# librerie custom
from .routes import routerDriver, routerMeeting
from src.logo import OPF1_STALKER_BANNER,F1_STRATOS_EXIT,BOLD, RESET, GREEN


console = Console()


async def Update_Driver():
    """
    Descrption:
        aggiunta task per aggiornare i dati dei driver
    Tasks:
        1. Cancellazione vecchi dati da Mongo-Stalker
        2. Fetch dati da OpenF1
        3. Invio dati a Mongo-Stalker
    """


    # Definiamo timeout unico e sensato
    timeout_config = httpx.Timeout(10.0, connect=3.0)
    
    with Progress(
        SpinnerColumn(spinner_name="dots", style="bold green"),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        
        async with httpx.AsyncClient(timeout=timeout_config) as client:
            # --- TASK 1: Cancellazione vecchi dati ---
            task1 = progress.add_task(description="Cancellazione vecchi dati...", total=None)
            try:
                resp1 = await client.delete("http://127.0.0.1:8080/api/drivers/deleteAllDrivers")
                await asyncio.sleep(4) 
                
                if resp1.status_code != 200:
                    progress.update(task1, description=f"[bold red]Errore Mongo: {resp1.status_code}")
                
                progress.update(task1, description="[bold green]Vecchi dati cancellati!")
            except Exception as e:
                progress.update(task1, description=f"[bold red]Errore connessione Mongo: {e}")


            # --- TASK 2: Fetch dati ---
            data_to_send = []
            task2 = progress.add_task(description="Chiamata API OpenF1...", total=None)
            try:
                resp2 = await client.get("https://api.openf1.org/v1/drivers?session_key=latest")
                await asyncio.sleep(4) 
                
                if resp2.status_code != 200:
                    progress.update(task2, description=f"[bold red]Errore OpenF1: {resp2.status_code}")
                
                progress.update(task2, description="[bold green]Dati OpenF1 ricevuti!")
                data_to_send = resp2.json()

            except Exception as e:
                progress.update(task2, description=f"[bold red]Errore connessione OpenF1: {e}")            




            # --- TASK 3: Invio dati ---
            task3 = progress.add_task(description="Invio Dati Mongo-Stalker...", total=None)
            try:
                await asyncio.sleep(4) 
                resp2 = await client.post("http://127.0.0.1:8080/api/drivers/insertManyDrivers", json=data_to_send)
                
                if resp2.status_code == 200:
                    progress.update(task3, description="[bold green]Dati inviati correttamente a Mongo!")
                else:
                    progress.update(task3, description=f"[bold red]Mongo ha risposto con errore: {resp2.status_code}")
            
            except (ConnectTimeout, ReadTimeout):
                progress.update(task3, description="[bold red]Timeout: Mongo-Stalker non raggiungibile")
            except Exception as e:
                progress.update(task3, description=f"[bold red]Errore imprevisto Mongo: {e}")

                



@asynccontextmanager
async def lifespan(app: FastAPI):
    print(OPF1_STALKER_BANNER)
    print(f"{BOLD}{GREEN}Inizializzazione Lifespan...{RESET}")
    scheduler = AsyncIOScheduler(timezone="Europe/Rome")

    scheduler.add_job(
        Update_Driver, 
        CronTrigger(hour=8, minute=00)
    )

    scheduler.add_job(
        Update_Driver, 
        CronTrigger(hour=20, minute=00)
    )
    
    scheduler.start()
    print(f"{BOLD}{GREEN}Scheduler avviato...{RESET}")
    yield
    print(F1_STRATOS_EXIT)

    scheduler.shutdown()
    print("Scheduler spento.")



app = FastAPI(lifespan=lifespan)



app.include_router(routerDriver)
app.include_router(routerMeeting)
