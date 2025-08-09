# Default make goal
.DEFAULT_GOAL := help

.PHONY: local-flask-install
local-flask-install: ## Install Python deps for Flask app using uv (manages .venv automatically)
	uv sync

.PHONY: local-flask
local-flask: ## Run the Flask app on http://localhost:5050 using uv
	uv run app.py

.PHONY: flask-build
flask-build: ## Build Flask image using docker-compose-flask.yml
	docker compose -f docker-compose.yml build

.PHONY: flask-up
flask-up: ## Start Flask container using docker-compose-flask.yml (detached)
	docker compose -f docker-compose.yml up -d --build

.PHONY: flask-down
flask-down: ## Stop Flask container using docker-compose-flask.yml
	docker compose -f docker-compose.yml down

.PHONY: flask-logs
flask-logs: ## Tail Flask container logs
	docker compose -f docker-compose.yml logs -f

.PHONY: help
help: ## Show this help
	@awk 'BEGIN {FS = ":.*##"}; /^[a-zA-Z0-9_.-]+:.*?##/ {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)