# Makefile - Task runner for backend service

PROJECT_NAME := assistant-backend
DOCKER_COMPOSE := docker compose

.PHONY: help up down restart logs build rebuild shell clean

help:  ## Show available commands
	@echo "Usage: make [command]"
	@echo ""
	@echo "Commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

up:  ## Start the backend and MongoDB services
	$(DOCKER_COMPOSE) up

up-d:  ## Start in detached mode
	$(DOCKER_COMPOSE) up -d

down:  ## Stop and remove containers and volumes
	$(DOCKER_COMPOSE) down -v --remove-orphans

restart: down up  ## Restart the stack

build:  ## Build services
	$(DOCKER_COMPOSE) build

rebuild:  ## Build without cache
	$(DOCKER_COMPOSE) build --no-cache

logs:  ## Tail logs
	$(DOCKER_COMPOSE) logs -f

shell:  ## Open a shell inside the backend container
	$(DOCKER_COMPOSE) exec backend sh

clean:  ## Full cleanup (containers, volumes, etc.)
	docker system prune -af --volumes

