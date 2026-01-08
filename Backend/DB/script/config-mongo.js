// Script per configurare un utente MongoDB con privilegi di lettura e scrittura su un database specifico.


db = db.getSiblingDB(process.env.APP_DB_NAME);

db.createUser({
  user: process.env.APP_USER,
  pwd: process.env.APP_PASSWORD,
  roles: [{ role: "readWrite", db: process.env.APP_DB_NAME }]
});