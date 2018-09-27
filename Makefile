install:
	pip install .
	pip install beacon/

dev-install:
	pip install -e .
	pip install beacon/

run:
	python -m swagger_server

docker-build:
	docker build -t ncats:knowledge-beacon .

docker-run:
	docker run -d --rm --name beacon -p 8080:8080 ncats:knowledge-beacon

docker-stop:
	docker stop beacon

docker-logs:
	docker logs beacon
