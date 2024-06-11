# fastflow-cms

## 1. Introduction

Fastflow CMS

## 2. Stack & Framework
- [Django](https://www.djangoproject.com/) - Batteries-included Python web framework.
- [PostgreSQL](https://www.postgresql.org/) - Well-know open source database system.

## 3. Dev tools (must install for local development)
- [Pyenv](https://github.com/pyenv/pyenv): python version management.
- [Docker](https://www.docker.com/products/docker-desktop/): docker app for launching services like db, redis, e.t.c.

## 4. Getting started
### Environment & dependencies setup (Pyenv installed)
- Create virtual env for easier maintain:
```bash
python -m venv .venv
```
- Sourcing the .venv:
```bash
source .venv/bin/activate
```
- Install package manager:
```bash
pip install -r requirements-init.txt
```
- Install all dependencies:
```bash
poetry install
```

### Run backend
- Edit the environment variables in [.env](.env) file.
- Start docker:
```bash
docker-compose up --detach
```
- Run migrations
```bash
bin/manage.sh migrate
```
- Create superuser to access to admin page
```bash
bin/manage.sh createsuperuser
```
- Populate Astrowind data (run first time only)
```bash
bin/manage.sh populate_aw_data
```
- (Optional) To use other admin interface, run this command to use `foundation` admin interface, more info
at [Django Admin Interface](https://github.com/fabiocaccamo/django-admin-interface).
```bash
bin/manage.sh loaddata admin_interface_theme_foundation.json
```
- Start server & admin panel
```bash
bin/manage.sh runserver 8000
```
- In order to use the below API playground, let create API key:
  - Visit: http://localhost:8000/admin/rest_framework_api_key/apikey/
  - Create API key for you, and save it, the key is generated and show only once.
  - More info at : https://florimondmanca.github.io/djangorestframework-api-key/
- Visit API playground and API documentation at:
  - API playground(Swagger): http://localhost:8000/api/cms-schema/swg/. Don't forget to click on
    `Authorize` and add your generated API key which we created in the previous step.
  - NOTE FOR API PLAYGROUND: in order to change the language code in header, you should open the URL in incognito mode
, otherwise the Django Admin session will override our API selected language.
  - API documentation: http://localhost:8000/api/cms-schema/redoc/
- (Optional) To set up pre-commit hook (to automatically code formatting and dependencies checking before commit) run:
```bash
pre-commit install
```
  (more info below)


## 5. Utilities
### Useful command:
- [bin/manage.sh](bin/manage.sh): aliases for `python fastflow_cms/manage.py` or `django-admin`, can config env later.
- Usually use:
  - `bin/manage.sh runserver 8000`: Run local server.
  - `bin/manage.sh createsuperuser`: Create superuser to access to admin at
[http://localhost:8000/admin/](http://localhost:8000/admin/)
  - `bin/manage.sh shell_plus`: Interactive shell_plus to access db, query, e.t.c.
- For a full list of Django utilities command, take a look at:
  - [Django official command](https://docs.djangoproject.com/en/4.2/ref/django-admin/)
  - [Django extension command](https://django-extensions.readthedocs.io/en/latest/command_extensions.html)

### Packages management
- [Poetry](https://python-poetry.org/docs/): the package dependencies management we use.
- When you want to add a dependency just run `poetry add your_package_name`.
- The automatically package checking code is at [bin/dep-validate.sh](bin/dep-validate.sh).

### Code conventions
- For code convention we are using:
  - [Ruff](https://pypi.org/project/ruff/): for speedy combination code formatting with flake8, blake or isort, e.t.c.
- The above tool have been wrapped with the executable script [bin/lint.sh](bin/lint.sh):
  - To lint only, run: `bin/lint.sh`
  - To automatically format, run: `bin/lint.sh --fix`

### Pre-commit hook
- To run these scripts automatically every time you commit, you need to install the pre-commit hooks:
  - Command: `pre-commit install`
  - [Pre-commit documentation](https://pre-commit.com/): Take a look at the documentation for more information.
  - After that, every time you commit, the `pre-commit` hooks will run the command defined in
[.pre-commit-config.yaml](.pre-commit-config.yaml) for you.


## 6. Running tests
- Normal run:
```bash
pytest fastflow_cms
```
- With coverage
```bash
pytest --cov-report term --cov=fastflow_cms fastflow_cms
```

## 7. Deployment
[![Run on Google Cloud](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run)
