HTML
====

Sintaxis y Semántica de HTML
----------------------------

Inicio de página en HTML5

.. literalinclude:: example01.html
    :linenos:
    :language: html
    :lines: 1-4

Iniicio de página en HTML 4.01

.. code-block:: html
   :linenos:

   <?xml version="1.0" encoding="utf-8"?>
   <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
   <html xmlns="http://www.w3.org/1999/xhtml">
   <head>

Estructura completa de una página en HTML5

.. literalinclude:: example01.html
    :linenos:
    :language: html

Elementos de HTML
-----------------

<main>
~~~~~~
El área principal del contenido de un documento incluye contenido que es único a ese documento y excluye el contenido que se repite a través de un conjunto de documentos, tales como navegación del sitio, información de copyright, logos de sitio y formularios de búsqueda.

Solo puede haber un elemento *main* por pagína, y no puede ser usado como desendiente de otro elemento semántico.


<section>
~~~~~~~~~
Este elemento se usa para definir una sección generica de un documento.


<nav>
~~~~~
Se usa para agrupar links de navegación a otras páginas o secciónes de la misma pagína.


<article>
~~~~~~~~~
Se usa par agrupar un pedaso de contenido independiente. Entradas de un blog,noticias.


<aside>
~~~~~~~
Se usa para contenido que esta relacionado con el  contenido


<figure> y <figcaption>
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html
   :linenos:

   <figure>
     <img src="img/fciencias.jpg" alt="Facultad de Ciencias" />
     <figcaption>Logo de la Facultad de Ciencias de la UNAM</figcaption>
   </figure>

.. raw:: html

   <figure>
     <img src="img/fciencias.jpg" alt="Facultad de Ciencias" />
     <figcaption>Logo de la Facultad de Ciencias de la UNAM</figcaption>
   </figure>


<details> y <summary>
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html
   :linenos:

    <details open>
       <summary>Boletín UNAM-2015/530</summary>
       <p>Instrumentan en la UNAM métodos para control de calidad del concreto reforzado con fibras
       </p>
   </details>


.. raw:: html

    <details>
       <summary>Boletín UNAM-2015/530</summary>
       <p>Instrumentan en la UNAM métodos para control de calidad del concreto reforzado con fibras
       </p>
   </details>


<header>
~~~~~~~~
Se puede usar mas de una vez en la misma página. Podriamso tener un header dentro de cada sección.


<footer>
~~~~~~~~
EL pie de página.


<adrdess>
~~~~~~~~~
Marca información de contacto para el *<article>* o *<body>* que lo contiene

.. seealso::

    La lista completa de los elementos en HTML5 se puede consultar en
    `<http://www.w3.org/TR/html5/ semantics.html#semantics>`_


Formas
------

Herramientas de desarrollo
--------------------------


.. note::  **HTML5 Boilerplate**. (https://html5boilerplate.com/).
