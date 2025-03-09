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
	PROJECT_PATH := /home/wagtail/wagtailgvcoop/
else
	EXEC_CMD := 
	PROJECT_PATH := ${dir ${abspath ${lastword ${MAKEFILE_LIST}}}}
endif

ENV_EXISTS := $(wildcard ${PROJECT_PATH}.env)
VENV_EXISTS := $(wildcard ${PROJECT_PATH}.venv/)

collectstatic:
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/python manage.py collectstatic --noinput --ignore=*.sass

messages:
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/python makemessages -l fr --ignore=manage.py --ignore=medias --ignore=setup.py --ignore=staticfiles --ignore=templates

sass:
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/python manage.py compilescss
	make collectstatic

init:
ifeq (,$(ENV_EXISTS))
	make initenv
	$(error .env required at $(ENV_PATH)  )
endif
ifeq (,$(VENV_EXISTS))
	make initvenv
endif
	make requirements

initenv:
	mkdir -p static
	mkdir -p media 
ifneq (,$(ENV_EXISTS))
	$(error .env exists at $(ENV_EXISTS) please remove.)
endif
	cp example.env .env
	echo "MERCI DE CONFIGURER .env AVEC VOS VARIABLES D'ENVIRONNEMENT"

initvenv:
ifneq (,$(ENV_EXISTS))
	$(error venv exists at $(PROJECT_PATH).venv. please remove if you wish to recreate.)
endif
	$(EXEC_CMD) python -m venv $(PROJECT_PATH).venv

requirements:
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/pip install --upgrade pip
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/pip install -r $(PROJECT_PATH)/requirements.txt

superuser:
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/python manage.py createsuperuser --username admin


update: 
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/python ./manage.py makemigrations
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/python ./manage.py migrate
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/python ./manage.py collectstatic --noinput

runserver:
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/python ./manage.py runserver

start:
	make runserver

	secretkey:
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

collectstatic:
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/python ./manage.py collectstatic --noinput

# From https://tailwindcss.com/docs/installation/tailwind-cli
tailwind-install-bin-linux:
	wget https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64 
	mv tailwindcss-linux-x64 venv/bin/tailwindcss
	chmod +x venv/bin/tailwindcss

# From https://tailwindcss.com/docs/installation/tailwind-cli
tailwind-install:
	npm install tailwindcss @tailwindcss/cli

# From https://tailwindcss.com/docs/installation/tailwind-cli
tailwind-compile:
	npx @tailwindcss/cli -i ./tailwind/src/input.css -o ./wagtailresdigitacom/static/css/tailwind.css -m

tailwind-compilemax:
	npx @tailwindcss/cli -i ./tailwind/src/input.css -o ./wagtailresdigitacom/static/css/tailwind.css 

tailwind-watch:
	npx @tailwindcss/cli -i ./tailwind/src/input.css -o ./wagtailresdigitacom/static/css/tailwind.css --watch