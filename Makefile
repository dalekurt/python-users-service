help: ## prints out the menu of command options
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

run: ## Start users service
	. venv/bin/activate && python main.py

setup: ## Install dependencies
	pip install -r requirements.txt

clean: ## Clean cache
	rm -rf __pycache__

.PHONY: help run setup clean
