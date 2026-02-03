#!/bin/bash
echo "--- 1. Inizializzazione Privilegi ---"
curl -s -X POST http://127.0.0.1:8000/init-privileges | jq .
echo -e "\n"

echo "--- 2. Registrazione Utente (Gilles Villeneuve) ---"
curl -s -X POST http://127.0.0.1:8000/register \
-H "Content-Type: application/json" \
-d '{
    "nome": "Gilles",
    "cognome": "Villeneuve",
    "email": "gilles.v@f1stratos.com",
    "paese": "Canada",
    "regione": "Quebec",
    "citta": "Saint-Jean-sur-Richelieu",
    "password": "SalutGilles27!",
    "id_privilegio": 1
}' | jq .
echo -e "\n"

echo "--- 3. Login Corretto (Stalker Mode) ---"
curl -s -X POST http://127.0.0.1:8000/login \
-H "Content-Type: application/json" \
-d '{
    "email": "gilles.v@f1stratos.com",
    "password": "SalutGilles27!"
}' | jq .
echo -e "\n"

echo "--- 4. Tentativo Login Errato (Password Sbagliata) ---"
curl -s -X POST http://127.0.0.1:8000/login \
-H "Content-Type: application/json" \
-d '{
    "email": "gilles.v@f1stratos.com",
    "password": "WRONG_PASSWORD"
}' | jq .
echo -e "\n"
