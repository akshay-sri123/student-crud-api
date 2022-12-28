DOCKER_HUB_USERNAME = akshay754
DOCKER_HUB_PASSWORD = YWtzaGF5MTEyMzU4MTM=
DOCKER_HUB_REPOSITORY = akshay754/student_crud_api

set_global_env:
	$(eval GIT_HASH=$(shell git rev-parse --short HEAD))

virtualenv:
	pip3 install virtualenv
	virtualenv .venv

requirements:
	pip3 install -r requirements.txt

lint:
	pylint ./app

docker_build: set_global_env
	DB_HOST="127.0.0.1" DB_USERNAME="app_user" DB_PASSWORD="app_pass123" docker build --no-cache -f Dockerfile . -t student_crud_api:$(GIT_HASH)

docker_push: set_global_env
	echo ${DOCKER_HUB_PASSWORD} | base64 -d | docker login --username ${DOCKER_HUB_USERNAME} --password-stdin
	docker tag student_crud_api:$(GIT_HASH) $(DOCKER_HUB_REPOSITORY):$(GIT_HASH)
	docker tag student_crud_api:$(GIT_HASH) $(DOCKER_HUB_REPOSITORY):latest
	docker push $(DOCKER_HUB_REPOSITORY):$(GIT_HASH)
	docker push $(DOCKER_HUB_REPOSITORY):latest

app_run_docker:
	docker run -it -e DB_USERNAME="app_user" -e DB_HOST="127.0.0.1" -e DB_PASSWORD="app_pass123" -p 5000:5000 --network host student_crud_api:1.0

app_run_docker_compose:
	docker-compose up

app_run_local:
	FLASK_APP=app/app.py DB_HOST="127.0.0.1" DB_USERNAME="app_user" DB_PASSWORD="app_pass123" flask run

initial_migration:
	DB_HOST="127.0.0.1" DB_USERNAME="app_user" DB_PASSWORD="app_pass123" flask db init && flask db stamp head && flask db migrate && flask db upgrade

app_run_local_dev_compose:
	docker-compose -f local-dev-compose.yaml up
