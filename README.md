# site-backend
Django rest framework backend for company web-site

### Environment variables

#### **required:**

<<<<<<< Updated upstream
```DATABASE_URL```, ```SECRET_KEY```
=======
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
   _with_ 
   ```poetry run python manage.py runserver 7000``` 
   _server would be hosted at ```http://127.0.0.1:7000```_
>>>>>>> Stashed changes

#### **optional:**


### Application endpoints:

- ```admin/``` - administrator interface
- ```categories/``` - categories list
- ```categories/{pk}/``` - category details
- ```items/``` - shop items list
- ```items/{pk}/``` - shop item details