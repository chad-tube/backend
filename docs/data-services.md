Data services require environmental variables to be set in order to set up suitable configuration for the services.

It's required to add .env file in the **docker/** directory for cache and database services to access these variables.

### Development env

POSTGRES_DB=chadragan
POSTGRES_USER=chadragan
POSTGRES_PASSWORD=chadragan
POSTGRES_PORT=5441

REDIS_PORT=6405


### Production env

There is no need to set production env variables since the services are running on a cloud platform for production and does not require any separate docker services to be set up.
