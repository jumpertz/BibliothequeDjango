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
	docker exec -it "bibliothequedjango-web-1" pip install

#lancer les fixtures
generate-fixtures:
	docker exec -it "bibliothequedjango-web-1" python "app_python/fixtures/generate_fixtures.py"

load-fixtures:
	docker exec -it "bibliothequedjango-web-1" python manage.py loaddata ./app_python/fixtures/*.json

#dump les données de users
dump-data-users:
	docker exec -it "bibliothequedjango-web-1" python manage.py dumpdata auth.User --output=app_python/fixtures/users.json

migrations:
	docker exec -ti "bibliothequedjango-web-1" python manage.py makemigrations app_python

migrate:
	docker exec -ti "bibliothequedjango-web-1" python manage.py migrate app_python