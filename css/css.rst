CSS
===

CSS asocia reglas de estilo con elementos HTML

Sintaxis
--------

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

Para incluir un archivo css usamos el elemento *link*

.. code-block:: html
   :linenos:

    <!doctype html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Ejemplo CSS</title>
            <link rel="stylesheet" href="css/main.css">
        </head>


Selectores
----------

Selector universal

.. code-block:: css
   :linenos:

   * {}


Selector por tipo

.. code-block:: css
   :linenos:

   h2, h3 {}

Selector de clase

.. code-block:: css
   :linenos:

   .jumbotron {}
   div.navbar-header {}

Selector de id

.. code-block:: css
   :linenos:

   #navbar {}

Selecctor de hijos

.. code-block:: css
   :linenos:

   li>a  {}

Selector de desendientes

.. code-block:: css
   :linenos:

   p a  {}


Formato visual
--------------

*CSS* supone que cada elemento genera una o más cajas rectangulares
(*element boxes*)

 .. raw:: html

    <ul>
        <li><span style="color:cornflowerblue"> margin </span></li>
        <li><span style="color:black"> border </span></li>
        <li><span style="color:darkorange"> padding </span></li>
    </ul>
    <div style="border: 2em solid cornflowerblue; ">
        <div style="border: 1em solid black">
            <div style="border: 2em solid darkorange">
                <div style="margin:.5em; font-size:2em">
                    <span>content area<span>
                </div>
            </div>
        </div>
    </div>


Propiedades del margen
~~~~~~~~~~~~~~~~~~~~~~

 * margin
 * margin-top
 * margin-bottom
 * margin-right
 * margin-left

El margen siempre es tranparente, permitiendo que el fondo del elemento padre sea visible.


Propiedades del borde
~~~~~~~~~~~~~~~~~~~~~

 * border-style (dotted, dashed, solid, double)
 * border-top-style
 * border-right-style
 * border-bottom-style
 * border-left-style
 * border-width
 * border-color
 * border (border-width border-style border-color)


Propiedades del padding
~~~~~~~~~~~~~~~~~~~~~~~

  * padding
  * padding-top
  * padding-right
  * padding-bottom
  * padding-left

El fondo del contenido se aplica al padding.


Dislplay
~~~~~~~~

La propiedad *display* especifica si/como se muestra un elemento.
Los posibles valoress son:

  * none
  * inline
  * block


.. literalinclude:: src/display.html
    :linenos:
    :language: html
    :lines: 18-24

¿Que reglas aplicacmos si queremos que la lista se despliegue de la siguiente manera?

 | Contacto | Mapa del sitio | Directorio | Correo | Ingresar |

..  admonition:: Resultado
    :class: toggle

    .. literalinclude:: src/display.html
        :linenos:
        :language: css
        :lines: 7-14

Media Queries
-------------

Herramientas de desarrollo
--------------------------