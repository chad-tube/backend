Project requires environmental variables to be set in order to communicate with Postgres and Redis.

For each case, in development and production, the variables are not looking alike since the services running locally requires different variables to connect to postgres for example whereas the production database provides url for connection.

### Development env

POSTGRES_DB=

POSTGRES_USER=

POSTGRES_PASSWORD=

POSTGRES_HOST=

POSTGRES_PORT=

REDIS_PORT=6405

### Production env

EXTERNAL_DATABASE_URL=

EXTERNAL_REDIS_URL=

### Note:

environmental variables for development must be named **dev.env** and must be placed in the root of the project. (same level as .gitignore for example)