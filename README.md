# site-backend 
[![Maintainability](https://api.codeclimate.com/v1/badges/f1fd60c36583e3daf1c3/maintainability)](https://codeclimate.com/repos/66e704389d3b78502cae3498/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/f1fd60c36583e3daf1c3/test_coverage)](https://codeclimate.com/repos/66e704389d3b78502cae3498/test_coverage)

Django rest framework backend for company web-site


### Local deploy

1. **Requirements**
   - python="^3.12"
   ```commandline
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install python3.12.3
   ```
   - poetry
   ```commandline
    sudo apt update
    sudo apt install pipx
    pipx ensurepath
    pipx install poetry
   ```
2. **Installation**
   ```commandline
    git clone git@github.com:mallakto-dev/site-backend.git
    cd site-backend/
    make install
   ```
3. **Set env variables**
    ```commandline
     nano .env
    ```
   add lines:
    ```.env
    DATABASE_URL=sqlite:///db.sqlite3
    SECRET_KEY=secret_key
    ```
   
   save and exit
4.  **Prepare database**
   ```commandline
    source .venv/bin/activate
    make migrate
    poetry run python manage.py loaddata dumpdb.json.gz 
   ```
5. **Launch Test server**
   ```commandline
    make dev
   ```
   
   API will be enabled at ```http://127.0.0.1:8000```
      
   _To specify another host you should use another command:_
   ```commandline
   poetry run python manage.py runserver {host:port}
   ```
   _for example_ ```poetry run python manage.py runserver 0.0.0.0:5000```.
   
   _Providing port without host also acceptable_
   _with ```poetry run python manage.py runserver 7000``` server woold be hosted at ```http://127.0.0.1:7000```_

### Admin panel:

To use admin panel features like update or create database instances you should create admin user first:
```commandline
poetry run python manage.py createsuperuser
```
admin panel will be enabled at ```admin/``` endpoint 

### Application endpoints:

- ```admin/``` - administrator interface
- ```categories/``` - categories list
- ```categories/{pk}/``` - category details
- ```items/``` - shop items list
- ```items/{pk}/``` - shop item details

### Environment variables

#### **required:**

```DATABASE_URL```

```SECRET_KEY```

#### **optional:**
