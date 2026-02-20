// Recupera le variabili iniettate da Docker
const dbName = process.env.MONGO_INITDB_DATABASE || 'f1stratos_db';
const appUser = process.env.F1_APP_USER;
const appPass = process.env.F1_APP_PASSWORD;

const targetDb = db.getSiblingDB(dbName);

// Crea l'utente dell'applicazione usando le ENV
targetDb.createUser({
  user: appUser,
  pwd: appPass,
  roles: [
    { role: "readWrite", db: dbName },
    { role: "dbAdmin", db: dbName }
  ]
});

// Elenco collezioni
const collections = [
  "Cardata", "Driverschampionship", "Teamschampionship", "Drivers",
  "Intervals", "Laps", "Location", "Meetings", "Overtakes", "Pit",
  "Position", "Racecontrol", "Sessions", "Sessionresult", 
  "Startinggrid", "Stints", "Teamradio", "Weather"
];

collections.forEach(col => {
    targetDb.createCollection(col);
    print(`✔️ Collezione ${col} creata nel database ${dbName}`);
});

print("🚀 Inizializzazione completata con successo!");