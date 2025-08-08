# PocketBase Development Makefile
.DEFAULT_GOAL := help

# Colors for output
BLUE := \033[36m
GREEN := \033[32m
YELLOW := \033[33m
RED := \033[31m
RESET := \033[0m

.PHONY: help
help: ## Show this help message
	@echo "$(BLUE)PocketBase Development Commands$(RESET)"
	@echo "================================"
	@awk 'BEGIN {FS = ":.*##"} /^[a-zA-Z_-]+:.*##/ { printf "$(GREEN)%-20s$(RESET) %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

.PHONY: setup
setup: ## Set up PocketBase with Docker
	@echo "$(YELLOW)🚀 Starting PocketBase...$(RESET)"
	docker compose -f PB_docker-compose.yml up -d
	@echo "$(GREEN)✅ PocketBase is running on http://localhost:8080$(RESET)"

.PHONY: stop
stop: ## Stop PocketBase
	@echo "$(YELLOW)🛑 Stopping PocketBase...$(RESET)"
	docker compose -f PB_docker-compose.yml down
	@echo "$(GREEN)✅ PocketBase stopped$(RESET)"

.PHONY: logs
logs: ## Show PocketBase logs
	docker compose -f PB_docker-compose.yml logs -f

.PHONY: status
status: ## Check PocketBase status
	@echo "$(BLUE)📊 PocketBase Status:$(RESET)"
	@docker compose -f PB_docker-compose.yml ps

.PHONY: create-collections
create-collections: ## Create all collections from JSON
	@echo "$(YELLOW)📝 Creating collections...$(RESET)"
	python3 create_json_collection.py
	@echo "$(GREEN)✅ Collections created$(RESET)"

.PHONY: create-specific
create-specific: ## Create specific collections (usage: make create-specific COLLECTIONS="posts user_settings")
	@echo "$(YELLOW)📝 Creating specific collections: $(COLLECTIONS)$(RESET)"
	python3 create_json_collection.py $(COLLECTIONS)

.PHONY: flask-deps
flask-deps: ## Install Flask dependencies
	@echo "$(YELLOW)📦 Installing Flask dependencies...$(RESET)"
	pip install -r flask_requirements.txt
	@echo "$(GREEN)✅ Dependencies installed$(RESET)"

.PHONY: flask-run
flask-run: ## Run sample Flask application connected to PB
	@echo "$(YELLOW)🌐 Starting Flask app...$(RESET)"
	python3 flask_pocketbase_app.py

.PHONY: dev
dev: setup create-collections flask-deps ## Full development setup
	@echo "$(GREEN)🎉 Development environment ready!$(RESET)"
	@echo "$(BLUE)Next steps:$(RESET)"
	@echo "  1. Visit PocketBase admin: http://localhost:8080/_/"
	@echo "  2. Run Flask app: make flask-run"
	@echo "  3. Visit Flask app: http://localhost:5000"

.PHONY: clean
clean: ## Clean up containers and volumes
	@echo "$(RED)🧹 Cleaning up...$(RESET)"
	docker compose -f PB_docker-compose.yml down -v
	@echo "$(GREEN)✅ Cleanup complete$(RESET)"

.PHONY: reset
reset: clean setup ## Reset everything (clean + setup)
	@echo "$(GREEN)🔄 Reset complete$(RESET)"





