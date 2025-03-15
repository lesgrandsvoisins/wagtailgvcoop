# Loading environment variables
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

ifndef DOCKER_CONTAINER
	DOCKER_CONTAINER := web
endif

ifeq ($(USE_DOCKER),1)
	EXEC_CMD := docker-compose exec -ti $(DOCKER_CONTAINER)
	PROJECT_PATH := /home/wagtail/gdvoisins/
else
	EXEC_CMD := 
	PROJECT_PATH := ${dir ${abspath ${lastword ${MAKEFILE_LIST}}}}
endif

# Simplified env variables
ENV_EXISTS := $(wildcard ${PROJECT_PATH}.env)
VENV_EXISTS := $(wildcard ${PROJECT_PATH}.venv/)

initenv:
	mkdir -p static
	mkdir -p media 
ifneq (,$(ENV_EXISTS))
	$(error .env exists at $(ENV_EXISTS) please remove.)
endif
	cp example.env .env
	echo "MERCI DE CONFIGURER .env AVEC VOS VARIABLES D'ENVIRONNEMENT"

initvenv:
ifneq (,$(VENV_EXISTS))
	$(error venv exists at $(PROJECT_PATH).venv. please remove if you wish to recreate.)
endif
	$(EXEC_CMD) python -m venv $(PROJECT_PATH).venv

messages:
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/python manage.py makemessages -l fr -l en --ignore=manage.py --ignore=medias --ignore=setup.py --ignore=staticfiles --ignore=templates

sass:
	make -C $(PROJECT_PATH)/gdvoisins/tailwind compile
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/python manage.py compilescss

init:
	make -C $(PROJECT_PATH)/gdvoisins init
ifeq (,$(ENV_EXISTS))
	make initenv
	$(error .env required at $(ENV_PATH)  )
endif
ifeq (,$(VENV_EXISTS))
	make initvenv
endif
	make requirements

requirements:
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/pip install --upgrade pip
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/pip install -r $(PROJECT_PATH)/requirements.txt
	make -C ./gdvoisins requirements

superuser:
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/python manage.py createsuperuser --username admin

update: 
	make sass
	make messages
	make collectstatic
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/python ./manage.py makemigrations
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/python ./manage.py migrate

runserver:
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/python ./manage.py runserver

start:
	make runserver

secretkey:
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

collectstatic:
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/python ./manage.py collectstatic --noinput