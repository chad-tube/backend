Initial intention for project deployment was Vercel where we can not maintain the same project structure as in local development meaning we can not deploy docker images on Vercel unlike AWS, GCP or Azure which is a great drawback, hence running project locally and in production is different.

Second intention was to use `render` to deploy the project but it does not support docker-compose which is why we can not keep the same project structure as in local.

When running project locally, we tend to use the best practices and use docker images for each service which is why locally we use docker images for postgres and redis.

## Running project locally
To run the project locally, you need to have external volumes for docker.

### Create external volumes
```bash
docker volume create yt_downloader_backend_db
docker volume create yt_downloader_backend_cache
```

### Run docker-compose
```bash
chmod +x ./scripts/run.sh
bash ./scripts/run.sh
```

### Settings and environment variables

Settings are devided into production and development. Production settings are located in `settings/prod.py` and development settings are located in `settings/local.py`.

Local variables are defined in `dev.env` file and production variables are defined in render's variable groups