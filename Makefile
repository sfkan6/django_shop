.DEFAULT_GOAL := help
.ONESHELL:
.PHONY: help push test venv deps run docker venv
VENV = venv


migrate: ## Make migrations
	. $(VENV)/bin/activate
	cd django_shop
	python manage.py migrate

load: ## database loading
	. $(VENV)/bin/activate
	cd django_shop
	python manage.py loaddata db.json

dump: ## database dump
	. $(VENV)/bin/activate
	cd django_shop
	python manage.py dumpdata --indent 4 > db.json

deps: ## Install requirements
	. $(VENV)/bin/activate
	python -m pip install -r requirements.txt

run: ## Run djnago
	. $(VENV)/bin/activate
	cd django_shop
	python manage.py runserver 0.0.0.0:8000

fast-run: ## Quick launch
	python -m venv $(VENV)
	@make deps
	@make migrate
	@make load
	@make run	

docker-b: ## Docker build
	docker build -t shop .

docker-r: ## Docker run
	docker run --rm -p 8000:8000 -it shop

docker: ## Docker launch
	@make docker-b
	@make docker-r

help: ## Show help message
	@IFS=$$'\n' ; \
	help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/:/'`); \
	printf "%s\n\n" "Usage: make [task]"; \
	printf "%-20s %s\n" "task" "help" ; \
	printf "%-20s %s\n" "------" "----" ; \
	for help_line in $${help_lines[@]}; do \
		IFS=$$':' ; \
		help_split=($$help_line) ; \
		help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		printf '\033[36m'; \
		printf "%-20s %s" $$help_command ; \
		printf '\033[0m'; \
		printf "%s\n" $$help_info; \
	done
