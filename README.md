# cookbook-django
Hands on Django Python Web Framework

- using Django version 2.2.4 with Python 3.7
- show install version: `python3 -m django --version`

## start
- create project: `django-admin startproject mysite`
- run django server: `python manage.py runserver` or `python3.7`
- add an app to project: `python manage.py startapp polls`

## sqlite3 cheatsheet
- open database: `developers$ sqlite3 db.sqlite3`
- list db's: `sqlite> .databases`
- list tables: `sqlite> .tables`
- show schema of table auth_user

```
sqlite> .schema auth_user

CREATE TABLE IF NOT EXISTS "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "last_name" varchar(150) NOT NULL);
```
- exit with: `.exit`

__table operation__

- select: `select * from auth_user;`
- create: `CREATE TABLE programming_lang ("id" integer PRIMARY KEY, name VARCHAR(512) NOT NULL);`
- drop: `DROP TABLE programming_lang ;`
- insert: `INSERT OR REPLACE INTO programming_lang (id, name) VALUES (0,'java');`


## links
- https://www.djangoproject.com/
