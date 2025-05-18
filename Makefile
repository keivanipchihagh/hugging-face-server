setup:
	python3 -m .venv .venv
	source .venv/bin/activate

install:
	pip install --upgrade pip
	pip install -r requirements.txt

docker-up:
	DOCKER_BUILDKIT=1 docker compose -f deploy/docker-compose.yaml up -d --build

docker-down:
	docker compose -f deploy/docker-compose.yaml down
