# Robot-To-Cloud-Computing

Robot to Cloud Computing is a tool for storing, analyzing, and presenting data collected by a robot.

## Quick Start

Follow these insstructions to get the server up and running for a debug setup. Note that the debug setup is not suitable for a production environment. See the [Setup](#setup) section for full instructions on configuring a production environment:

1. Install all the dependencies from the [Dependencies](#dependencies) section
2. Navigate to the directory that contains `manage.py`. If the root project directory is named `Robot-To-Cloud-Computing`, `manage.py` should be found in `Robot-To-Cloud-Computing/RobotToCloudComputing`.
3. Run the database migrations.

    ```
    python3 manage.py migrate
    ```
    
4. Run the development server. See the [Setup](#setup) section for instructions on running the *production* server.

    ```
    python3 manage.py runserver
    ```
    
The server should now be running on `localhost:8000`. You can navigate to the homepage in your brower by entering [http://localhost:8000/RobotMonitor](http://localhost:8000/RobotMonitor) into your address bar, or by clicking the link.

## Contents

- [Robot-To-Cloud-Computing](#robot-to-cloud-computing)
  - [Quick Start](#quick-start)
  - [Contents](#contents)
  - [Server Installation](#server-installation)
    - [Dependencies](#dependencies)
    - [Setup](#setup)
  - [API Endpoints](#api-endpoints)
    - [Using the API Endpoints](#using-the-api-endpoints)
  - [Testing](#testing)
    - [Unit Testing](#unit-testing)
    - [Manual Testing](#manual-testing)
  - [Running the Server](#running-the-server)
  - [Building and Debugging the C Code](#building-and-debugging-the-c-code)
    - [Production Builds](#production-builds)
        - [macOS x86_64 (`gcc`)](#macos-x86_64-gcc)
        - [macOS Apple Silicon (`clang`)](#macos-apple-silicon-clang)
        - [Linux (`gcc`)](#linux-gcc)
        - [Windows (`mingw` from WSL)](#windows-mingw-from-wsl)
    - [Debug Builds](#debug-builds)
        - [macOS x86_64 (`gcc`)](#macos-x86_64-gcc-1)
        - [macOS Apple Silicon (`clang`)](#macos-apple-silicon-clang-1)
        - [Linux (`gcc`)](#linux-gcc-1)
        - [Windows (`mingw` from WSL)](#windows-mingw-from-wsl-1)
  - [Other](#other)
    - [Generating an RSA key pair](#generating-an-rsa-key-pair)

## Server Installation

### Dependencies

1. Python (^3.9)

    ##### MacOS
    ```
    brew install python
    ```
    ##### Debian
    ```
    sudo apt install python
    ```
    ##### Windows
    
    Download and run the installer from the [Python website](https://www.python.org/downloads/).

2. Django (^3.2)
    
    ```
    pip3 install django==3.2.8
    ```

3. Python Cryptography (^36.0)
    
    ```
    pip3 install cryptography
    ```

4. argon2 (^20.1)
    
    ```
    pip3 install argon2-cffi
    ```

5. Django REST Framework with JWT (^4.7)

    ```
    pip3 install djangorestframework-simplejwt
    ```

6. Gunicorn (^20.1.0)
    
    ```
    pip3 install gunicorn
    ```

7. django_cryptography (^1.0)
    
    ```
    pip3 install django-cryptography
    ```

### Setup

1. **Install dependencies**
   
   See [Dependencies](#dependencies) section

   It might be a good idea to create the Django application and install the Python dependencies in a Python virtual environment. See the [Python docs](https://docs.python.org/3/library/venv.html) on creating a virtual envronment.

2. **Navigate to directory containting `manage.py`**

3. **Configure settings in `settings.py`**
    
    - Configure JWTs
        1. Add `rest_framework_jwt` to `INSTALLED_APPS` in `settings.py`

            ```
            INSTALLED_APPS = [
                ...
                'rest_framework_simplejwt',
                'rest_framework_simplejwt.token_blacklist',
            ]
            ```

        2. Generate two RSA key pairs (on a secure machine if deploying to a production environment), one current pair and one pair for the future when keys are rotated. Keys should be rotated at least once per year in a production environment. Place the current public and private keys in the `.keys` directory along with the future public key. Save the future private key in a **secure offline location**, such as a VeraCrypt volume, and remove it from the machine. Follow best practices to ensure this key has as few opportunities of being comprimised as possible. See [Generating and RSA key pair](#generating-an-rsa-key-pair) for generating the keys.

        3. In the same `settings.py`, add the following configurations. The `REFRESH_TOKEN_LIFETIME_DAYS` will determine how frequently users have to re-enter their sign-in credentials. Be sure the `_key_path` variables point to the correct paths of the RSA keys generated in the previous step. It may make sense to use an absolute path.

            ```
            _private_key_path = os.path.join(BASE_DIR, '../.keys/jwt-RS256.key')
            _public_key_path = os.path.join(BASE_DIR, '../.keys/jwt-RS256.key.pub')

            with open(_private_key_path) as f:
                _private_key = f.read()

            with open(_public_key_path) as f:
                _public_key = f.read()

            # It is IMPERITIVE that the PRIVATE_TOKEN_SIGNING_KEY be kept secret in a production environment
            PRIVATE_TOKEN_SIGNING_KEY = _private_key
            PUBLIC_TOKEN_VERIFYING_KEY = _public_key

            REST_FRAMEWORK = {
                'DEFAULT_AUTHENTICATION_CLASSES': (
                    'rest_framework_simplejwt.authentication.JWTAuthentication',
                )
            }

            ACCESS_TOKEN_LIFETIME_MINUTES = 8
            REFRESH_TOKEN_LIFETIME_DAYS = 21

            SIMPLE_JWT = {
                'ACCESS_TOKEN_LIFETIME': timedelta(minutes=ACCESS_TOKEN_LIFETIME_MINUTES),
                'REFRESH_TOKEN_LIFETIME': timedelta(days=REFRESH_TOKEN_LIFETIME_DAYS),
                'ROTATE_REFRESH_TOKENS': True,
                'BLACKLIST_AFTER_ROTATION': True,

                'ALGORITHM': 'RS256',
                'SIGNING_KEY': PRIVATE_TOKEN_SIGNING_KEY,
                'VERIFYING_KEY': PUBLIC_TOKEN_VERIFYING_KEY,
            }
            ```

            You will need to add the following import to the top of `settings.py`:

            ```
            from datetime import timedelta
            ```

    - Generate a `SECRET_KEY`

        1. In the Django interactive shell, generate a secret key with Django's `generate_random_secret_key()` function.

            ```
            python manage.py shell

            from django.core.management.utils import get_random_secret_key
            print(get_random_secret_key())
            ```

        2. Copy the key into a text file named `django-secret-key.txt` and put it in the `.keys` directory you created for the RSA keys. You should have something like this in your settings file:

            ```
            _secret_key_path = os.path.join(BASE_DIR, '../.keys/django-secret-key.secret'

            with open(_secret_key_path) as f:
                _secret_key = f.read()

            SECRET_KEY = _secret_key
            ```
	    
    - *(Production only)* Set `DEBUG = False`
    - *(Production only)* Add domain name to `ALLOWED_HOSTS`
    - *(Production only)* Set `SECURE_BROWSER_XSS_FILTER = True` and `SECURE_CONTENT_TYPE_NOSNIFF = True`
    - *(Production only)* Make sure `django.contrib.auth.hashers.Argon2PasswordHasher` is the first item in `PASSWORD_HASHERS`
    - Configure language and timezone settings (`USE_TZ` should be `True` if server will operate over multiple time zones)

4. **Collect static files**
    
    Set `STATIC_ROOT` in `settings.py` to the directory where user static files ought to be stored. Add the path of static files for the templates to `STATICFILES_DIRS`, then run
    ```
    python manage.py collectstatic
    ```
    Double-check to ensure static files have been copied to the directory specified in  `STATICFILES_DIR`

5. **Run Database Migrations**

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Configure Gunicorn**

    The Gunicorn configuration can be found in `conf/gunicorn_conf.py`. For the most part, this should be configured as desired. The following settings should be reviewed for production:

    * `bind` should be set to the IP/port Gunicorn will bind to. This port will be used by NGINX to communicate with Gunicorn and thereby the Django application
    * `backlog` is an integer between 64 and 2048 that specifies the maximum number of pending connections
    * `workers` is the number of worker processes that will be used to handle requests. The [Gunicorn documentation](https://docs.gunicorn.org/en/stable/settings.html#workers) recommends using two times the number of cores on your machine, plus one.
    * `timeout` specifies how long workers are silent before they are killed (then subsequently restarted when needed)
    * `loglevel` specifies the log level. Options are, progressively,  `debug`, `info`, `warning`, `error`, and `critical`
    * `capture_output` specifies whether or not output from Django (e.g. stacktraces) should be printed to the Gunicorn error log
    * `accesslog` is the file path of the log file storing a record of HTTP requsts
    * `errorlog` is the file path of the log file storing a record of error, warning, info, and debug output

    See the [Gunicorn documentation](https://docs.gunicorn.org/en/stable/settings.html) to learn more about each setting.

    If logs are to be stored in the `logs` directory, you'll have to create that directory.

    ```
    mkdir logs
    ```

## API Endpoints

There are three different API calls you can make in this application. The API endpoints can be used to return the available robots in the database, return a list of the available time ranges for a given robot, and return a list of JSON objects containing the csv file paths, data, and associated images for a robot within a given time range.

### Using the API Endpoints

Get the available robots in the database
    
    "/RobotMonitor/data/get_robots"

Get the available time ranges for a given `robot_id`

    "/RobotMonitor/data/get_available_data_time_ranges?robot_id=<robot_id>"

Get the csv files for a given robot and time range

    "/RobotMonitor/data/get_data?robot_id=<robot_id>&start_time=<start_time>&end_time=<end_time>"

## Testing

### Unit Testing

- Testing the whole application
    
    ```
    python manage.py test
    ```

- Testing a single Django app
    
    ```
    python manage.py test RobotMonitor
    ```

- Testing in parallel

    ```
    python manage.py test --parallel
    ```

### Manual Testing

You can hit the endpoints using cURL. Here is an example of how to make a POST request with cURL:

```
curl -X POST "http://localhost:8000/RobotMonitor/user/user_login" -d "email=test@example.com&password=aT3stPa$$w0rd"
```
or
```
curl -X POST "http://localhost:8000/RobotMonitor/user/user_login" -H "Content-Type: application/json" -d '{"email": "test@example.com", "password": "aT3stPa$$w0rd"}'
```

To authenticate, send a JWT access token in the `Authorization` header:

```
curl -X GET "http://localhost:8000/RobotMonitor/user/get" -H "Authorization: Bearer [ACCESS_TOKEN]"
```

To refresh a JWT access token, you need to use a JWT refresh token (you should get it upon login):

```
curl -X POST "http://localhost:8000/RobotMonitor/refresh_token" -H "Content-Type: application/json" -d '{"refresh": "[REFRESH_TOKEN]"}'
```

## Running the Server

- Development mode (don't use in production):
    
    ```
    python manage.py runserver
    ```

- Gunicorn (WSGI server):

    From the directory with `manage.py`:

    ##### Foreground
    ```
    gunicorn -c gunicorn_conf.py RobotToCloudComputing.wsgi
    ```

    ##### Background
    ```
    nohup gunicorn -c gunicorn_conf.py RobotToCloudComputing.wsgi &>/dev/null &
    ```
## Building and Debugging the C Code

The CSV-to-JSON translator is written in C and gets compiled to a shared dynamic link library. A Python wrapper uses Python's C Foreign Function Interface (FFI). To build the libraries, run the appropriate version of the following command from the directory containing the `.c` and `.h` source files:

### Production Builds

##### macOS x86_64 (`gcc`)
```
gcc -O3 -fPIC -shared -o ../libs/csv-to-json-x86.dylib dynarray.c csvjson.c
```

##### macOS Apple Silicon (`clang`)
```
clang -O3 -fPIC -shared -o ../libs/csv-to-json-arm64.dylib dynarray.c csvjson.c
```

##### Linux (`gcc`)
```
gcc -O3 -fPIC -shared -o ../libs/csv-to-json.so dynarray.c csvjson.c
```

##### Windows (`mingw` from WSL)
```
x86_64-w64-mingw32-gcc -O3 -fPIC -shared -o ../libs/csv-to-json.dll dynarray.c csvjson.c
```

### Debug Builds

##### macOS x86_64 (`gcc`)
```
gcc -DDEBUG -g -Wall -fPIC -shared -o ../libs/csv-to-json-x86.dylib dynarray.c csvjson.c
```

##### macOS Apple Silicon (`clang`)
```
clang -DDEBUG -g -Wall -fPIC -shared -o ../libs/csv-to-json-arm64.dylib dynarray.c csvjson.c
```

##### Linux (`gcc`)
```
gcc -DDEBUG -g -Wall -fPIC -shared -o ../libs/csv-to-json.so dynarray.c csvjson.c
```

##### Windows (`mingw` from WSL)
```
x86_64-w64-mingw32-gcc -DDEBUG -g -Wall -fPIC -shared -o ../libs/csv-to-json.dll dynarray.c csvjson.c
```

## Other

### Generating an RSA key pair

```
ssh-keygen -t rsa -b 2048 -m pem -f jwt-RS256.key
# Don't add passphrase
openssl rsa -in jwt-RS256.key -pubout -outform PEM -out jwt-RS256.key.pub
```
