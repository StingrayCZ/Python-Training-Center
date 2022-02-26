# DJango labs

```cmd
(venv) C:\Users\jarom\PycharmProjects\SQL Database>django-admin startproject minitwitter
```

```cmd
Microsoft Windows [Version 10.0.18363.1556]
(c) 2019 Microsoft Corporation. Všechna práva vyhrazena.

(venv) C:\Users\jarom\PycharmProjects\SQL Database>pip list
Package            Version
------------------ -------
asgiref            3.5.0
Django             4.0.2                                                                                        
pip                21.1.2                                                                                       
psycopg2           2.9.3                                                                                        
setuptools         57.0.0                                                                                       
setuptools         57.0.0
sqlparse           0.4.2
tzdata             2021.5
wheel              0.36.2
WARNING: You are using pip version 21.1.2; however, version 22.0.3 is available.
You should consider upgrading via the 'C:\Users\jarom\PycharmProjects\SQL Database\venv\Scripts\python.exe -m pi
p install --upgrade pip' command.

(venv) C:\Users\jarom\PycharmProjects\SQL Database>django-admin startproject minitwitter

(venv) C:\Users\jarom\PycharmProjects\SQL Database>cd minitwitter

(venv) C:\Users\jarom\PycharmProjects\SQL Database\minitwitter>python manage.py check --database default        
Traceback (most recent call last):
  File "C:\Users\jarom\PycharmProjects\SQL Database\venv\lib\site-packages\django\db\backends\base\base.py", lin
e 230, in ensure_connection
    self.connect()
  File "C:\Users\jarom\PycharmProjects\SQL Database\venv\lib\site-packages\django\utils\asyncio.py", line 25, in
 inner
    return func(*args, **kwargs)
  File "C:\Users\jarom\PycharmProjects\SQL Database\venv\lib\site-packages\django\db\backends\base\base.py", lin
e 211, in connect
    self.connection = self.get_new_connection(conn_params)
  File "C:\Users\jarom\PycharmProjects\SQL Database\venv\lib\site-packages\django\utils\asyncio.py", line 25, in
 inner
    return func(*args, **kwargs)
  File "C:\Users\jarom\PycharmProjects\SQL Database\venv\lib\site-packages\django\db\backends\postgresql\base.py
", line 199, in get_new_connection
    connection = Database.connect(**conn_params)
  File "C:\Users\jarom\PycharmProjects\SQL Database\venv\lib\site-packages\psycopg2\__init__.py", line 122, in c
onnect
    conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
psycopg2.OperationalError: connection to server at "127.0.0.1", port 5432 failed: FATAL:  role "p" does not exis
t
unc(*args, **kwargs)
  File "C:\Users\jarom\PycharmProjects\SQL Database\venv\lib\site-packages\django\db\backends\base\base.py", lin
e 230, in ensure_connection
    self.connect()
  File "C:\Users\jarom\PycharmProjects\SQL Database\venv\lib\site-packages\django\db\utils.py", line 90, in __ex
it__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "C:\Users\jarom\PycharmProjects\SQL Database\venv\lib\site-packages\django\db\backends\base\base.py", lin
e 230, in ensure_connection
    self.connect()
  File "C:\Users\jarom\PycharmProjects\SQL Database\venv\lib\site-packages\django\utils\asyncio.py", line 25, in
 inner
    return func(*args, **kwargs)
  File "C:\Users\jarom\PycharmProjects\SQL Database\venv\lib\site-packages\django\db\backends\base\base.py", lin
e 211, in connect
    self.connection = self.get_new_connection(conn_params)
  File "C:\Users\jarom\PycharmProjects\SQL Database\venv\lib\site-packages\django\utils\asyncio.py", line 25, in
 inner
    return func(*args, **kwargs)
  File "C:\Users\jarom\PycharmProjects\SQL Database\venv\lib\site-packages\django\db\backends\postgresql\base.py
", line 199, in get_new_connection
    connection = Database.connect(**conn_params)
  File "C:\Users\jarom\PycharmProjects\SQL Database\venv\lib\site-packages\psycopg2\__init__.py", line 122, in c
onnect
    conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
django.db.utils.OperationalError: connection to server at "127.0.0.1", port 5432 failed: FATAL:  role "p" does not exist


(venv) C:\Users\jarom\PycharmProjects\SQL Database\minitwitter>python manage.py check --database default
System check identified no issues (0 silenced).

(venv) C:\Users\jarom\PycharmProjects\SQL Database\minitwitter>python manage.py startapp minitwitterapp

(venv) C:\Users\jarom\PycharmProjects\SQL Database\minitwitter>python manage.py makemigrations
No changes detected

(venv) C:\Users\jarom\PycharmProjects\SQL Database\minitwitter>python manage.py makemigrations
Traceback (most recent call last):
  File "manage.py", line 22, in <module>
    main()
  File "manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "C:\Users\jarom\PycharmProjects\SQL Database\venv\lib\site-packages\django\core\management\__init__.py", line 425, in execute_from_command_line
    utility.execute()
  File "C:\Users\jarom\PycharmProjects\SQL Database\venv\lib\site-packages\django\core\management\__init__.py", line 401, in execute
    django.setup()
  File "C:\Users\jarom\PycharmProjects\SQL Database\venv\lib\site-packages\django\__init__.py", line 24, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "C:\Users\jarom\PycharmProjects\SQL Database\venv\lib\site-packages\django\apps\registry.py", line 114, in populate
    app_config.import_models()
  File "C:\Users\jarom\PycharmProjects\SQL Database\venv\lib\site-packages\django\apps\config.py", line 300, in import_models
    self.models_module = import_module(models_module_name)
  File "C:\Users\jarom\AppData\Local\Programs\Python\Python38-32\lib\importlib\__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 975, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 671, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 783, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "C:\Users\jarom\PycharmProjects\SQL Database\minitwitter\minitwitterapp\models.py", line 1, in <module>
    from django.db import model
ImportError: cannot import name 'model' from 'django.db' (C:\Users\jarom\PycharmProjects\SQL Database\venv\lib\site-packages\django\db\__init__.py)

(venv) C:\Users\jarom\PycharmProjects\SQL Database\minitwitter>python manage.py makemigrations


(venv) C:\Users\jarom\PycharmProjects\SQL Database\minitwitter>python manage.py makemigrations
Migrations for 'minitwitterapp':
  minitwitterapp\migrations\0001_initial.py
    - Create model Tweets

(venv) C:\Users\jarom\PycharmProjects\SQL Database\minitwitter>python manage.py sqlmigrate minitwitter 0001
CommandError: No installed app with label 'minitwitter'.

(venv) C:\Users\jarom\PycharmProjects\SQL Database\minitwitter>python manage.py sqlmigrate minitwitterapp 0001
BEGIN;
--
-- Create model Tweets
--
CREATE TABLE "minitwitterapp_tweets" ("id" bigserial NOT NULL PRIMARY KEY, "content" varchar(200) NOT NULL, "created" timestamp with time zone NOT NULL);
COMMIT;

(venv) C:\Users\jarom\PycharmProjects\SQL Database\minitwitter>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, minitwitterapp, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying minitwitterapp.0001_initial... OK
  Applying sessions.0001_initial... OK

(venv) C:\Users\jarom\PycharmProjects\SQL Database\minitwitter>python manage.py shell
Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> python
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'python' is not defined
>>> python manage.py shell
  File "<console>", line 1
    python manage.py shell
           ^
SyntaxError: invalid syntax
>>> from miniwitterapp import models
Traceback (most recent call last):
  File "<console>", line 1, in <module>
ModuleNotFoundError: No module named 'miniwitterapp'
>>> from minitwiterapp import models 
Traceback (most recent call last):
  File "<console>", line 1, in <module>
ModuleNotFoundError: No module named 'minitwiterapp'
>>> from minitwitterapp import models
>>> models.Tweets
<class 'minitwitterapp.models.Tweets'>
>>> tweet = models.Tweets(content="Hello, world!") 
>>> tweet
<Tweets: Tweets object (None)>
>>> tweet.save()
>>> tweet
<Tweets: Tweets object (1)>
>>> tweet.save()
>>> tweet.content = "Hello, world!"
>>> tweet.save()
>>> python manage.py makemigration
  File "<console>", line 1
    python manage.py makemigration
           ^
SyntaxError: invalid syntax
>>> exit
Use exit() or Ctrl-Z plus Return to exit
>>> exit()

(venv) C:\Users\jarom\PycharmProjects\SQL Database\minitwitter>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, minitwitterapp, sessions
Running migrations:
  No migrations to apply.

(venv) C:\Users\jarom\PycharmProjects\SQL Database\minitwitter>python manage.py makemigration
Unknown command: 'makemigration'. Did you mean makemigrations?
Type 'manage.py help' for usage.

(venv) C:\Users\jarom\PycharmProjects\SQL Database\minitwitter>python manage.py makemigration
Unknown command: 'makemigration'. Did you mean makemigrations?
Type 'manage.py help' for usage.

(venv) C:\Users\jarom\PycharmProjects\SQL Database\minitwitter>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, minitwitterapp, sessions
Running migrations:
  No migrations to apply.

(venv) C:\Users\jarom\PycharmProjects\SQL Database\minitwitter>python manage.py makemigrations
No changes detected

(venv) C:\Users\jarom\PycharmProjects\SQL Database\minitwitter>python manage.py shell
Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> exit()

(venv) C:\Users\jarom\PycharmProjects\SQL Database\minitwitter>python manage.py makemigrations
No changes detected

(venv) C:\Users\jarom\PycharmProjects\SQL Database\minitwitter>python manage.py makemigrations

TypeError: __init__() got an unexpected keyword argument 'auto'

(venv) C:\Users\jarom\PycharmProjects\SQL Database\minitwitter>python manage.py makemigrations
Migrations for 'minitwitterapp':
  minitwitterapp\migrations\0002_tweets_updated.py
    - Add field updated to tweets

(venv) C:\Users\jarom\PycharmProjects\SQL Database\minitwitter>pip list       
```
