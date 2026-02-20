# Database Setup

## Configurazione Iniziale

Prima di avviare i servizi Docker, è necessario creare un file `.env` nella root del progetto con le seguenti variabili d'ambiente:

```env
F1_APP_USER=your_source_user
F1_APP_PASSWORD=your_secure_password_here
F1_DB_NAME=your_db_name
```

## Descrizione delle Variabili

- **F1_APP_USER**: Username per l'accesso al database MongoDB (Mongo-Stalker)
- **F1_APP_PASSWORD**: Password sicura per l'accesso al database MongoDB (definire una password propria)
- **F1_DB_NAME**: Nome del database principale


