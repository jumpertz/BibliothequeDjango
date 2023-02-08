#build le projet
build:
	docker compose build --pull --no-cache

#run le projet
run:
	docker compose up -d

#stop le projet
stop:
	docker compose down

#installer un module
install:
	pip install

#lancer les fixtures
load-fixtures:
	python3 app_python/fixtures/generate_fixtures.py

#dump les données de users
dump-data-users:
	python3 manage.py dumpdata auth.User --output=app_python/fixtures/users.json

migrations:
	docker exec -ti "bibliothequedjango-web-1" python manage.py makemigrations app_python

migrate:
	docker exec -ti "bibliothequedjango-web-1" python manage.py migrate app_python