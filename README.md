
## Podéis utilizar entorno virtual venv (SOLO LA PRIMERA VEZ)

        python -m venv venv
        source venv/Scripts/activate
        python -m pip install --upgrade pip
        pip install -r venv-requirements.txt

        Si no existe la carpeta del proyecto ejercutar los siguiente:
        mkdir django-backend
        django-admin startproject core django-backend/.

### Levantar servicio Django dentro de entorno virtual venv
        cd django-backend/
        set -a; source ../.env; set +a
        python manage.py runserver 0.0.0.0:8001
        Abrir navegador: http://localhost:8001/

### Levantar servicio Django dentro de entorno virtual venv, con comando Make
        Make runserver


### startapp:
python manage.py startapp $(app)

# makemigrations:
 python manage.py makemigrations

# no olvidar
set -a; source ../.env; set +a

# migrate:
python manage.py migrate

# createsuperuser:
python manage.py createsuperuser

## Adicional Comandos para PSql
# Crear
createdb -p [puerto] -h localhost -U [usuario] -W [nombre_de_la_base_de_datos]

# Borrar
Dropdb -p [puerto] -h localhost -U [usuario] -W [nombre_de_la_base_de_datos]

# Ver Bases de datos
psql -p [puerto] -h localhost -U [usuario]
postgres=# \l
