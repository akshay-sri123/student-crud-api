virtualenv:
	pip3 install virtualenv
	virtualenv .venv

requirements:
	pip3 install -r requirements.txt

docker_build:
	DB_HOST="127.0.0.1" DB_USERNAME="app_user" DB_PASSWORD="app_pass123" docker build --no-cache -f Dockerfile . -t student_crud_api:1.0

app_run_docker: docker_build
	docker run -it -e DB_USERNAME="app_user" -e DB_HOST="127.0.0.1" -e DB_PASSWORD="app_pass123" -p 5000:5000 --network host student_crud_api:1.0

app_run_docker_compose: 
	docker-compose up

app_run_local:
	FLASK_APP=app/app.py DB_HOST="127.0.0.1" DB_USERNAME="app_user" DB_PASSWORD="app_pass123" flask run

migrate:
	DB_HOST="127.0.0.1" DB_USERNAME="app_user" DB_PASSWORD="app_pass123" flask db migrate && flask db upgrade