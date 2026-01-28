# F1-StratOs
Progetto per la fruizione di dati sulla Formula Uno
ciao

## Mapping delle Porte
# 🛰️ Service Infrastructure & API Mapping

Benvenuto nella documentazione tecnica del networking del progetto. Questo file serve come riferimento rapido per la mappatura delle porte e la struttura degli endpoint API.

---

## 🛠️ Architettura dei Servizi

Il sistema è composto da tre microservizi principali che comunicano tra loro. Il **Gateway** funge da punto di ingresso unico per le chiamate esterne.



### 🔌 Mappatura delle Porte

| Servizio | Porta | Protocollo | Descrizione |
| :--- | :---: | :---: | :--- |
| **Gateway** | `8070` | HTTP | Entry point per il frontend |
| **Mongo-Stalker** | `8080` | HTTP | Gestione database. |
| **OPF1-Stalker** | `8090` | HTTP | Logica di business specifica i dati della f1. |



#### Esempi di Rotte Comuni:
* **List Drivers:** `GET /api/drivers`
* **Driver Details:** `GET /api/drivers/:id`
* **Update Driver:** `PUT /api/drivers/:id`

