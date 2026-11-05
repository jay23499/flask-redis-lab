# Flask + Redis Lab
By Jerry Williams

A local Docker Compose project with a Flask web application,
Gunicorn, and a Redis visit counter.

## Requirements
- Docker Desktop running
- Docker Compose

## Run
docker compose up -d --build --wait

Open http://localhost:8087

## Verify
docker compose ps
curl -i http://localhost:8087/health

Refresh the home page to increase the visit counter.

## Architecture
- Flask runs behind Gunicorn on container port 8000.
- Host port 8087 is bound to 127.0.0.1.
- Flask connects to Redis using the Compose service name redis.
- Redis uses a named volume and append-only persistence.
- Both services have health checks.

## Tests completed
- Built and started both containers successfully.
- Verified the visit counter in the browser.
- Verified the counter remained 2 after removing and recreating containers.
- Stopped Redis and observed an unhealthy application health response.
- Restored Redis and verified both containers became healthy.
- Removed containers and the network using docker compose down.

## Stop
docker compose down

This preserves the Redis data volume for the next run.

## Lessons learned
Containers can be recreated while data persists in a named volume.
Health checks detect dependency failures; they do not automatically
restart unhealthy containers.
