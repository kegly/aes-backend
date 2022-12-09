.PHONY: up

up:

	docker-compose -f production-docker-compose.yml up

.PHONY: run

run: up

.PHONY: local

local:

	docker-compose up -d

	python django_core/manage.py migrate

	python django_core/manage.py runserver

.DEFAULT_GOAL := up

.PHONY: dev

dev:

	docker-compose -f dev-server-docker-compose.yml up -d
