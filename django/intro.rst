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

.. code-block:: bash

    pycon2020_site
    |-- db.sqlite3
    |-- pycon2020_site
    |   |-- __init__.py
    |   |-- settings.py
    |   |-- urls.py
    |   |-- wsgi.py
    `-- manage.py


