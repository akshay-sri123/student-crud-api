virtualenv:
	pip3 install virtualenv
	virtualenv .venv
	source .venv/bin/activate

requirements: virtualenv
	pip3 install -r requirements.txt

docker_build:
	DB_USERNAME="app_user" DB_PASSWORD="app_pass123" docker build --no-cache -f Dockerfile . -t student_crud_api:1.0

app_run_docker: docker_build
	docker run -it -e DB_USERNAME="app_user" -e DB_PASSWORD="app_pass123" -p 5000:5000 --network host student_crud_api:1.0

app_run_docker_compose: 
	docker-compose up -d

app_run_local:
	DB_USERNAME="app_user" DB_PASSWORD="app_pass123" flask run