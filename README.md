# ICT.Hack

![photo_2022-12-10 12 11 06](https://user-images.githubusercontent.com/90460154/206842648-d02dc01c-1713-47cd-b80f-c04389dc095e.jpeg)

## Frontend
 :link: [Репозиторий aes-frontend](https://github.com/Nikita-quartZ/aes-frontend)
 ![web pages](https://user-images.githubusercontent.com/90460154/206898882-1fb95393-e747-4d89-b381-70a1268e2347.png)
 
 Вы можете посмотреть прототип без бэкенда [тут](https://hacaton-dist.vercel.app/#/projects)

##  Installation
<details>
<summary>

### Local

</summary>

#### Requirements
- [ ] Python >= 3.11

#### Django app
1. Create venv
```bash
python3.11 -m venv .venv
```

2. Activate venv
```bash
source .venv/bin/activate
```

3. Install requirements
```bash
pip install -r django_core/requirements/local.txt
```

4. Copy .env
```bash
cp django_core/django_core/local.example.env django_core/django_core/.env
```

5. Collect staticfiles
```bash
python django_core/manage.py collectstatic --noinput
```
#### Docker and Docker compose
Refer to:

https://docs.docker.com/engine/install/

#### Deploy

Use the script to start PSQL in Docker Compose, apply migrations and run development server:
```bash
make local
```
Your venv should be activated

#### Swagger Docs
Go to http://127.0.0.1:8000/api/swagger after running server

#### Development

During development, use Black formatter, Pylint and Flake8.

</details>

<details>
<summary>

### Dev Server

</summary>

1. Copy .env:
```bash
cp django_core/django_core/dev.example.env django_core/django_core/.env
```
2. Use shortcut script:
```bash
make dev
```

</details>
