SHELL := /bin/bash

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: start
start: ## run the docker compose command of the project
	docker-compose up -d --build

.PHONY: restart
restart: ## re-run the docker compose command of the project
	docker-compose restart

.PHONY: stop
stop: ## stop the docker compose command
	docker-compose down

.PHONY: logs
logs: ## follow up the logs of the service
	docker-compose logs -f web

.PHONY: test
test: ## Run the tests of the app
	docker-compose exec web pytest . -v

.PHONY: shell
shell: ## Enter to the shell of the container app
	docker-compose exec web sh