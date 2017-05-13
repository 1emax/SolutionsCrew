# Installation

1. Install Docker
2. Install Docker-Compose
3. run `docker-compose build && docker-compose up -d`
4. login to web container and create superuser `docker exec -it dg01 /bin/bash`


#### Useful Commands
`docker-compose stop && docker-compose build && docker-compose up -d && docker-compose ps`  
`docker-compose logs --tail="all" -f celery`
