# Frontend F1StratOs

## Descrizione del Servizio

Il **Frontend F1StratOs** è l'interfaccia utente principale dell'applicazione F1StratOs. È un'applicazione web moderna costruita con **React**, **TypeScript** e **Vite** che fornisce l'accesso ai dati e alle funzionalità del sistema di gestione dei dati Formula 1.

### Funzionalità Principali

- **Autenticazione**: Sistema di login sicuro per accedere alle funzionalità protette
- **Gestione Driver**: Visualizzazione e ricerca dei driver F1 con relativi dettagli
- **Dashboard**: Pagina home con panoramica generale del sistema
- **Interfaccia Glassmorphism**: Design moderno e minimalista con effetto glassmorphism
- **Gestione dello Stato**: Utilizzo di Redux per la gestione centralizzata dello stato (autenticazione, dati utente, ecc.)
- **Routing Protetto**: Percorsi che richiedono l'autenticazione dell'utente

### Stack Tecnologico

- **React** + **TypeScript**: Per la costruzione di componenti tipizzati e robusti
- **Vite**: Build tool veloce e moderno per lo sviluppo
- **Redux**: Gestione dello stato globale dell'applicazione
- **CSS Glassmorphism**: Stili moderni e sofisticati

### Struttura del Progetto

- `src/pages/`: Pagine principali dell'applicazione (Login, Home, Drivers, ecc.)
- `src/components/`: Componenti riutilizzabili (Navbar, Card, CarDriver, ecc.)
- `src/store/`: Configuration Redux e slices
- `src/styles/`: Fogli di stile globali e del tema
- `src/types/`: Definizioni TypeScript per i tipi di dati

### Installazione e Avvio

```bash
npm install
npm run dev
```

L'applicazione si avvierà su `http://localhost:5173`

