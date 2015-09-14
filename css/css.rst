CSS
===

.. literalinclude:: 01.html
    :linenos:
    :language: html

Sintaxis
--------

CSS asocia reglas de estilo con elementos HTML

.. code-block:: css
   :linenos:

   p {
     font-family: Arial;
   }

.. code-block:: css
   :linenos:

   h2, h3 {
     font-size: 30px;
     color: green;
   }

.. code-block:: html
   :linenos:

    <!doctype html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Ejemplo CSS</title>
            <link rel="stylesheet" href="css/main.css">
        </head>


Selector universal
~~~~~~~~~~~~~~~~~~~
.. code-block:: css
   :linenos:

   * {}


Selector por tipo
~~~~~~~~~~~~~~~~~

.. code-block:: css
   :linenos:

   h2, h3 {}

Selector de clase
~~~~~~~~~~~~~~~~~

.. code-block:: css
   :linenos:

   .jumbotron {}
   div.navbar-header {}

Selector de id
~~~~~~~~~~~~~~

.. code-block:: css
   :linenos:

   #navbar {}

Selecctor de hijos
~~~~~~~~~~~~~~~~~~

.. code-block:: css
   :linenos:

   li>a  {}

Selector de desendientes
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: css
   :linenos:

   p a  {}


Media Queries
-------------

Herramientas de desarrollo
--------------------------