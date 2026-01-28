# F1-StratOs
Progetto per la fruizione di dati sulla Formula Uno

---

### 🔌 Mappatura delle Porte

| Servizio | Porta | Protocollo | Descrizione |
| :--- | :---: | :---: | :--- |
| **Gateway** | `8070` | HTTP | Entry point per il frontend |
| **Mongo-Stalker** | `8080` | HTTP | Gestione database. |
| **OPF1-Stalker** | `8090` | HTTP | Logica di business specifica i dati della f1. |

---



### Rotte:
## 🗄️ Mongo-Stalker
*Gestione della persistenza e del database dei piloti.*

| Metodo | Endpoint | Descrizione |
| :--- | :--- | :--- |
| ![GET](https://img.shields.io/badge/GET-blue?style=flat-square) | `getDriverByNumber` | Recupera un pilota tramite numero di gara. |
| ![GET](https://img.shields.io/badge/GET-blue?style=flat-square) | `getAllDrivers` | Recupera la lista completa dei piloti. |
| ![POST](https://img.shields.io/badge/POST-green?style=flat-square) | `insertDriver` | Inserisce un nuovo pilota nel sistema. |
| ![POST](https://img.shields.io/badge/POST-green?style=flat-square) | `insertManyDrivers` | Inserimento bulk di più piloti. |
| ![DELETE](https://img.shields.io/badge/DELETE-red?style=flat-square) | `deleteDriverByNumber` | Elimina un pilota specifico. |
| ![DELETE](https://img.shields.io/badge/DELETE-red?style=flat-square) | `deleteAllDrivers` | **Attenzione:** Svuota l'intera collezione. |



## 🏎️ OPF1-Stalker
*Servizio dedicato alla logica di business e telemetria.*

| Metodo | Endpoint | Descrizione |
| :--- | :--- | :--- |
| ![GET](https://img.shields.io/badge/GET-blue?style=flat-square) | `getDriverByNumber` | Recupera dati pilota elaborati da OPF1. |
| ![GET](https://img.shields.io/badge/GET-blue?style=flat-square) | `getAllDrivers` | Recupera tutti i piloti processati. |



## 🚪 Gateway
*Punto di accesso unico per i client esterni (Porta 8070).*

| Metodo | Endpoint | Descrizione |
| :--- | :--- | :--- |
| ![GET](https://img.shields.io/badge/GET-blue?style=flat-square) | `getDriverByNumber` | Proxy verso il recupero pilota. |
| ![GET](https://img.shields.io/badge/GET-blue?style=flat-square) | `getAllDrivers` | Proxy verso la lista totale piloti. |

---
