run:
	docker compose up -d --build

stop:
	docker compose stop

.PHONY: run stop