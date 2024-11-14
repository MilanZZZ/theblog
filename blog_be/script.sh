pip list --format=freeze > requirements.txt
docker compose up --build --force-recreate --no-deps db
docker exec -it django_backend /bin/bash
