```
docker build -t f1startos-mongo:1 -f Dockerfile.mongo .
```
### test dell'immagine
``` 
docker run --rm f1startos-mongo:1 cat /docker-entrypoint-initdb.d/init-db.js
```

### prova container 
```
docker run -d \
  --name f1stratos_mongo \
  -p 27017:27017 \
  --env-file .env \
  -e MONGO_INITDB_ROOT_USERNAME=${MONGO_ROOT_USER} \
  -e MONGO_INITDB_ROOT_PASSWORD=${MONGO_ROOT_PASSWORD} \
  -e MONGO_INITDB_DATABASE=${F1_DB_NAME} \
  -e F1_APP_USER=${F1_APP_USER} \
  -e F1_APP_PASSWORD=${F1_APP_PASSWORD} \
  -v /home/db/mongo_data2:/data/db \
  f1stratos-mongo:1
```