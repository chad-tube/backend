Initial intention for project deployment is Vercel where we can not maintain the same project structure as in local development meaning we can not deploy docker images on Vercel unlike AWS, GCP or Azure which is a great drawback, hence running project locally and in production is different.

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
