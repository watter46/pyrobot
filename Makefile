up:
	docker compose up -d
build:
	docker compose build --no-cache --force-rm
down:
	docker compose down --remove-orphans
restart:
	@make down
	@make up
destroy:
	docker compose down --rmi all --volumes --remove-orphans
destroy-volumes:
	docker compose down --volumes --remove-orphans
ps:
	docker ps -a --no-trunc
logs:
	docker compose logs
logs-watch:
	docker compose logs --follow
log-app:
	docker compose logs app
log-app-watch:
	docker compose logs --follow app
app:
	docker compose exec app bash