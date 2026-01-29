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



## Rotte Beckend:

### 🗄️ Mongo-Stalker (Port: 8080)
| Metodo | Prefisso | Endpoint | Descrizione |
| :--- | :--- | :--- | :--- |
| ![GET](https://img.shields.io/badge/GET-blue?style=flat-square) | `/api/drivers` | `getDriverByNumber` | Recupera un pilota tramite il suo numero di gara. |
| ![GET](https://img.shields.io/badge/GET-blue?style=flat-square) | `/api/drivers` | `getAllDrivers` | Recupera tutti i piloti. |
| ![POST](https://img.shields.io/badge/POST-green?style=flat-square) | `/api/drivers` | `insertDriver` | Inserisce un nuovo pilota. |
| ![POST](https://img.shields.io/badge/POST-green?style=flat-square) | `/api/drivers` | `insertManyDrivers` | Inserisce più piloti contemporaneamente. |
| ![DELETE](https://img.shields.io/badge/DELETE-red?style=flat-square) | `/api/drivers` | `deleteDriverByNumber` | Elimina un pilota tramite il suo numero. |
| ![DELETE](https://img.shields.io/badge/DELETE-red?style=flat-square) | `/api/drivers` | `deleteAllDrivers` | Elimina l'intero database piloti. |



### 🏎️ OPF1-Stalker (Port: 8090)
| Metodo | Prefisso | Endpoint | Descrizione |
| :--- | :--- | :--- | :--- |
| ![GET](https://img.shields.io/badge/GET-blue?style=flat-square) | `/api/drivers` | `getDriverByNumber` | Recupera un pilota tramite il suo numero di gara. |
| ![GET](https://img.shields.io/badge/GET-blue?style=flat-square) | `/api/drivers` | `getAllDrivers` | Recupera tutti i piloti. |



### 🚪 Gateway (Port: 8070)
| Metodo | Prefisso | Endpoint | Descrizione |
| :--- | :--- | :--- | :--- |
| ![GET](https://img.shields.io/badge/GET-blue?style=flat-square) | `/api/drivers` | `getDriverByNumber` | Routing verso il recupero pilota. |
| ![GET](https://img.shields.io/badge/GET-blue?style=flat-square) | `/api/drivers` | `getAllDrivers` | Routing verso il recupero totale piloti. |

---
