Django
======


`Django <https://www.djangoproject.com/>`_ es un Web Framework para
`Python <https://www.python.org/>`_.

Instalación
-----------

Se recomienda usar un ambiente virtual

.. code-block:: bash

    $ virtualenv-2.7 pycon2020_project
    $ cd pycon2020_project/
    $ source bin/activate

para instalar django usamos pip

.. code-block:: bash

    $ pip install django
    Downloading/unpacking django
    Downloading Django-1.8.4-py2.py3-none-any.whl (6.2MB): 6.2MB downloaded
    Installing collected packages: django
    Successfully installed django
    Cleaning up...


Iniciando un proyecto
---------------------

.. code-block:: bash

    $ django-admin startproject pycon2020_site
    $ cd pycon2020_site


.. code-block:: bash

    pycon2020_site
    |-- pycon2020_site
    |   |-- __init__.py
    |   |-- settings.py
    |   |-- urls.py
    |   |-- wsgi.py
    `-- manage.py

manage.py
~~~~~~~~~

.. code-block:: bash

    $ python manage.py runserver 0.0.0.0:8000
    Performing system checks...

    System check identified no issues (0 silenced).

    You have unapplied migrations; your app may not work properly until they are applied.
    Run 'python manage.py migrate' to apply them.

    September 28, 2015 - 01:19:18
    Django version 1.8.4, using settings 'pycon2020_site.settings'
    Starting development server at http://0.0.0.0:8000/
    Quit the server with CONTROL-C.

En el navegador ir a `<http://localhost:8000>`_

.. image:: images/django-admin.png

Bases de Datos
~~~~~~~~~~~~~~

Una migración sirve para mover la base de datos de un diseño a otro.

.. code-block:: bash

    $ python manage.py migrate
    Operations to perform:
      Synchronize unmigrated apps: staticfiles, messages
      Apply all migrations: admin, contenttypes, auth, sessions
    Synchronizing apps without migrations:
      Creating tables...
      ...

Django usa por default como base de datos `sqlite <https://www.sqlite.org>`_

La configuración se encuentra en pycon2020_site/pycon2020_site/settings.py

.. code-block:: bash

    pycon2020_site
    |-- db.sqlite3
    |-- pycon2020_site
    |   |-- __init__.py
    |   |-- settings.py
    |   |-- urls.py
    |   |-- wsgi.py
    `-- manage.py


Views y URLs
------------

Crea el archivo pycon2020_site/pycon2020_site/views.py y agregamos una vista

.. literalinclude:: src/pycon2020_site/pycon2020_site/views.py
    :linenos:
    :language: python
    :lines: 1, 3-7

Creamos una URL que respondera con la vista anterior

.. literalinclude:: src/pycon2020_site/pycon2020_site/urls.py
    :language: python
    :lines: 19-21, 23-24

En el navegador ir a `<http://localhost:8000>`_

Apps
----
En Django un proyecto representa un sitioweb completo.

* configuración global
* inclusion de funcionalidad adicional
* lista principal de URLs

Una **app** de Django encapsula una unidad de duncionalidad

* Una sección de Blog
* Un Foro de discusión
* Un sistema de etiquetas

Creamos una app que incluiremos en el proyecto.

.. code-block:: bash

    $ python manage.py startapp talks


.. code-block:: bash

    talks
    |-- migrations
    |   |-- __init__.py
    |-- __init__.py
    |-- admin.py
    |-- models.py
    |-- tests.py
    `-- views.py


Para extender el proyecto con la **app** modificamos el archivo pycon2020_site/pycon2020_site/settings.py

.. literalinclude:: src/pycon2020_site/pycon2020_site/settings.py
    :language: python
    :lines: 33-40, 90-92

Models
------

ORM (Object Relational Mapper)

Los Modelos son Clases que represntan tablas en una base de datos.
Cada modelo es una tabla y cada atributo de la clase es una columna en la tabla.

.. literalinclude:: src/pycon2020_site/talks/models.py
    :language: python
    :lines: 1, 11-17

Tenemos un nuevo modelo, necesitamos una migración.

.. code-block:: bash

    $ python manage.py makemigrations talks

Realizamos la migración

.. code-block:: bash

    $ python manage.py migrate talks
    Operations to perform:
      Apply all migrations: talks
    Running migrations:
      Rendering model states... DONE
      Applying talks.0001_initial... OK


Interacción con Django
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    $ python manage.py shell
    Python 2.7.8 (default, Nov 24 2014, 11:29:53)
    [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.54)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>>

Cuando queremos hacer una consulta con el ORM necesitamos el nombre del modelo y su atributo objects. objects apunta al 'model manager' que controla el acceso a las instancias del modelo y otras cosas.


.. code-block:: bash

    >>> from talks.models import Talk
    >>> Talk.objects.all()
    []
    >>> type(Talk.objects.all())
    <class 'django.db.models.query.QuerySet'>
    >>>


.. code-block:: bash

    >>> t = Talk()
    >>> t.title = "Python"
    >>> t.description = "Introduccion"
    >>> t.save()
    >>> Talk.objects.all()
    [<Talk: Talk object>]
    >>>

.. code-block:: bash

    >>> from talks.models import Talk
    >>> Talk(title='Estructuras de Datos con python', description='Aprende sobre listas, diccionario y tuplas').save()
    >>> Talk.objects.all()
    [<Talk: Talk object>, <Talk: Talk object>]
    >>>

.. code-block:: bash

    >>> Talk.objects.create(title='Orientacion a Objectos en Python', description="Revisaremos las clases en python")
    <Talk: Talk object>
    >>> Talk.objects.all()
    [<Talk: Talk object>, <Talk: Talk object>, <Talk: Talk object>]
    >>>

modificamos talks/models.py

.. literalinclude:: src/pycon2020_site/talks/models.py
    :language: python
    :lines: 20-21


.. code-block:: bash

    >>> from talks.models import Talk
    >>> Talk.objects.all()
    [<Talk: Python>, <Talk: Estructuras de Datos con python>, <Talk: Orientacion a Objectos en Python>]
    >>>


Vistas en la app
----------------

En talks/views.py

.. literalinclude:: src/pycon2020_site/talks/views.py
    :language: python
    :lines: 1-3, 5-11

Agregamos talks/urls.py

.. literalinclude:: src/pycon2020_site/talks/urls.py
    :language: python
    :lines: 1-6, 8

Agregamos en  pycon2020_site/urls.py

.. literalinclude:: src/pycon2020_site/pycon2020_site/urls.py
    :language: python
    :lines: 20-24

En el navegador ir a `<http://localhost:8000/talks>`_

Django admin
------------

.. code-block:: bash

    $ python manage.py createsuperuser
    Username (leave blank to use 'gil'): gil
    Email address: gil@ciencias.unam.mx
    Password:
    Password (again):
    Superuser created successfully.

Modificamos talks/admin.py

.. literalinclude:: src/pycon2020_site/talks/admin.py
    :language: python
    :lines: 1-2, 15-16

Views
-----

Creamos un directorio templates dentro de la aplicción. Dentro de este un directorio con el nombre de la applciación.

.. code-block:: bash

    $ mkdir -p talks/templates/talks

Creamos el archivo talk_list.html


.. literalinclude:: src/pycon2020_site/talks/templates/talks/talk_list.html
    :linenos:
    :language: html

Agregamos una nueva vista en la aplicación.

.. literalinclude:: src/pycon2020_site/talks/views.py
    :linenos:
    :language: python
    :lines: 14-16

Update urls.py en la aplicación

.. literalinclude:: src/pycon2020_site/talks/urls.py
    :language: python


Templates en el proyecto
------------------------

Creamos un directorio *templates* al mismo nivel que el proyecto y la aplicación

.. code-block:: bash

    $ mkdir templates

Agregamos este directorio en la sección de templates en pycon2020_site/settings.py

.. literalinclude:: src/pycon2020_site/pycon2020_site/settings.py
    :linenos:
    :language: python
    :lines: 56-70

creamos el archivo templates/home.html

.. literalinclude:: src/pycon2020_site/templates/home.html
    :language: html
    :lines: 6


modificmos las vistas en el proyecto (si es necesario ajustamos la url)


.. literalinclude:: src/pycon2020_site/pycon2020_site/views.py
    :linenos:
    :language: python
    :lines: 2, 7-11


layouts
-------

Creamos un archivo layout.html dentro del directorio templates.
En los templates definimos bloques que pueden ser sobreescritos.

.. literalinclude:: src/pycon2020_site/templates/layout.html
    :language: html
    :lines: 3-7, 9-14


Modificamos el template home.html para que extienda el template layout.html

.. literalinclude:: src/pycon2020_site/templates/home.html
    :language: html
    :lines: 1

Veamos `<http://localhost:8000>`_

Sobre escribimos los bloques del template que extendimos

.. literalinclude:: src/pycon2020_site/templates/home.html
    :language: html

Archivos estaticos
------------------

Agregamos una nueva variable en settings.py

.. literalinclude:: src/pycon2020_site/pycon2020_site/settings.py
    :language: python
    :lines: 104-106

Creamos el directorio assets

.. code-block:: bash

    $ mkdir -p assets/css

Dentro de este directorio pueden ir archivos estaticos que servira Nginx. Mientras estemos desarrolando le indicaremos a django que sirva nuestros archivos estaticos.
En urls.py

.. literalinclude:: src/pycon2020_site/pycon2020_site/urls.py
    :language: python
    :lines: 18, 26-28


.. literalinclude:: src/pycon2020_site/templates/layout.html
    :language: html
    :lines: 1-9

Views
-----

Agregamos una vista para las platicas

.. literalinclude:: src/pycon2020_site/talks/views.py
    :language: python
    :lines: 19-21

.. literalinclude:: src/pycon2020_site/talks/urls.py
    :language: python
    :lines: 7

.. literalinclude:: src/pycon2020_site/talks/templates/talks/talk_details.html
    :language: html


Track Model
-----------

modificamos talks/models.py

.. literalinclude:: src/pycon2020_site/talks/models.py
    :linenos:
    :language: python
    :lines: 4-22

Hacemos las migraciones

.. code-block:: bash

    $ python manage.py makemigrations talks
    $ python manage.py migrate talks

Modificamos talks/admin.py

.. literalinclude:: src/pycon2020_site/talks/admin.py
    :language: python
    :lines: 3-5, 17

En el navegador ir a `<http://localhost:8000/admin>`_


Agregamos una vista en talks/admin.py

.. literalinclude:: src/pycon2020_site/talks/admin.py
    :language: python
    :lines: 6-15, 17


Agregamos una vista para los tracks:

En talks/views.py

.. literalinclude:: src/pycon2020_site/talks/views.py
    :language: python
    :lines: 4, 22-26

Agregasmo la vista html

.. literalinclude:: src/pycon2020_site/talks/templates/talks/track_details.html
    :linenos:
    :language: html

Modificamos la url:

.. literalinclude:: src/pycon2020_site/talks/urls.py
    :language: python
    :lines: 8


404 En talks/views.py

.. code-block:: python

    from django.shortcuts import get_object_or_404

    def track_details(request, pk):
        track = get_object_or_404(Track, pk=pk)
        return render(request, 'talks/track_details.html', {'track': track})
