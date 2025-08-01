```sh
run-codex-only:	## Run only the Codex container (codex-container) via codex compose file and keeps it running
	@echo "Running only the Codex container from codex compose file..."
	docker compose -f docker-compose.codex.yml up codex
```


```sh
docker exec -it codex-container bash
docker exec -it codex-container bash -c "uv run endtoend.py"

#docker exec -t codex-container bash -c "cd /app/input-sources && codex --provider openai --model o4-mini --quiet --approval-mode full-auto \"$$(cat ./orchestrator/prompts/prompt-init-userguide-iterative.md)\" > .//output-init-userguide-iterative.json"
#docker exec -t $DOCKER_ENV_VARS "$CONTAINER_NAME" bash -c "cd /app/input-sources && $CODEX_COMMAND"
#codex --provider openai --model o4-mini --quiet --approval-mode full-auto "who are you"
#codex --provider openai --model o4-mini --quiet --approval-mode full-auto "$$(cat ./orchestrator/prompts/prompt-init-userguide-iterative.md)" > ./outputs_model/output-init-userguide-iterative.json

#Dev Containers: attach to running container
```