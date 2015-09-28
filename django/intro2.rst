Vistas en la app
----------------

En talks/views.py

.. literalinclude:: src/pycon2020_site/talks/views.py
    :language: python

Agregamos talks/urls.py

.. literalinclude:: src/pycon2020_site/talks/urls.py
    :language: python


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
