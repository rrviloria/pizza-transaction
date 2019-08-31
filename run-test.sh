#!/bin/sh
# run-test.sh

echo "Testing..."
docker exec -it pizza_web_1 pipenv run python manage.py test