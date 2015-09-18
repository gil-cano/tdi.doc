HTML
====

Sintaxis y Semántica de HTML
----------------------------

Inicio de una página en HTML5

.. literalinclude:: app/01-html.html
    :linenos:
    :language: html
    :lines: 1-4

Inicio de una página en HTML 4.01

.. literalinclude:: app/01-xhtml.html
    :linenos:
    :language: html
    :lines: 1-6


Estructura completa de una página en HTML5

.. literalinclude:: app/01-html.html
    :linenos:
    :language: html

Elementos de HTML
-----------------

Comentarios
~~~~~~~~~~~

.. code-block:: html
   :linenos:

   <!-- start of main text -->
   <p>En el Instituto de Ingeniería (II) de la UNAM se adaptan y mejoran métodos
      de prueba desarrollados en otras naciones para caracterizar el comportamiento
      del concreto reforzado con fibras, tecnología cada vez más utilizada en
      distintas obras mexicanas.</p>

   <p>En nuestro país se emplea en pisos industriales, pistas de aeropuerto,
      carreteras y revestimiento de túneles y lumbreras, así como en sostenimiento
      de taludes.<p>

   <p>Esta mezcla de cemento, grava, arena y agua con fibras plásticas o de acero
      se aplica para reducir y controlar el agrietamiento, así como para mejorar
      la resistencia al impacto y, principalmente, la tenacidad (energía de absorción).</p>
   <!-- end of main text -->


..  admonition:: Resultado
    :class: toggle

    .. raw:: html

        <!-- start of main text -->
        <p>En el Instituto de Ingeniería (II) de la UNAM se adaptan y mejoran métodos de prueba
        desarrollados en otras naciones para caracterizar el comportamiento del concreto reforzado
        con fibras, tecnología cada vez más utilizada en distintas obras mexicanas.</p>

        <p>En nuestro país se emplea en pisos industriales, pistas de aeropuerto, carreteras y revestimiento de túneles y lumbreras, así como en sostenimiento de taludes.<p>

        <p>Esta mezcla de cemento, grava, arena y agua con fibras plásticas o de acero se aplica para reducir y controlar el agrietamiento, así como para mejorar la resistencia al impacto y, principalmente, la tenacidad (energía de absorción).</p>
        <!-- end of main text -->


Atributo ID
~~~~~~~~~~~

.. code-block:: html
   :linenos:

   <p>En el Instituto de Ingeniería (II) de la UNAM se adaptan y mejoran métodos
      de prueba desarrollados en otras naciones para caracterizar el comportamiento
      del concreto reforzado con fibras, tecnología cada vez más utilizada en
      distintas obras mexicanas.</p>

   <p id="uso">En nuestro país se emplea en pisos industriales, pistas de aeropuerto,
      carreteras y revestimiento de túneles y lumbreras, así como en sostenimiento
      de taludes.<p>

   <p>Esta mezcla de cemento, grava, arena y agua con fibras plásticas o de acero
      se aplica para reducir y controlar el agrietamiento, así como para mejorar
      la resistencia al impacto y, principalmente, la tenacidad (energía de absorción).</p>

Atributo CLASS
~~~~~~~~~~~~~~

.. code-block:: html
   :linenos:

   <p class="important unam">En el Instituto de Ingeniería (II) de la UNAM se adaptan y mejoran métodos
      de prueba desarrollados en otras naciones para caracterizar el comportamiento
      del concreto reforzado con fibras, tecnología cada vez más utilizada en
      distintas obras mexicanas.</p>

   <p>En nuestro país se emplea en pisos industriales, pistas de aeropuerto,
      carreteras y revestimiento de túneles y lumbreras, así como en sostenimiento
      de taludes.<p>

   <p class="important">Esta mezcla de cemento, grava, arena y agua con fibras plásticas o de acero
      se aplica para reducir y controlar el agrietamiento, así como para mejorar
      la resistencia al impacto y, principalmente, la tenacidad (energía de absorción).</p>


Elementos de Bloque
~~~~~~~~~~~~~~~~~~~

.. code-block:: html
   :linenos:

    <h1>John Hopcroft</h1>
    <p>Las fechas de las platicas son:</p>
    <ul>
        <li>Lunes 10 de Agosto, 12:00 horas</li>
        <li>Martes 11 de Agosto, 13:00 horas</li>
    </ul>


..  admonition:: Resultado
    :class: toggle

    .. raw:: html

        <h1>John Hopcroft</h1>
        <p>Las fechas de las platicas son:</p>
        <ul>
            <li>Lunes 10 de Agosto, 12:00 horas</li>
            <li>Martes 11 de Agosto, 13:00 horas</li>
        </ul>


Elementos de Linea
~~~~~~~~~~~~~~~~~~

.. code-block:: html
   :linenos:

    <b>John Hopcroft</b>, <em>IBM</em> Professor of Engineering and Applied Mathematics,
    <a href="https://www.cornell.edu/">Cornell University</a>


..  admonition:: Resultado
    :class: toggle

    .. raw:: html

        <b>John Hopcroft</b>, <em>IBM</em> Professor of Engineering and Applied Mathematics,
        <a href="https://www.cornell.edu/">Cornell University</a>


<div>
~~~~~

El elemento *<div>* agrupa un conjunto de elementos en bloque.

.. code-block:: html
   :linenos:

    <div>
        <h1>John Hopcroft</h1>
        <p>Las fechas de las platicas son:</p>
        <ul>
            <li>Lunes 10 de Agosto, 12:00 horas</li>
            <li>Martes 11 de Agosto, 13:00 horas</li>
        </ul>
    </div>


..  admonition:: Resultado
    :class: toggle

    .. raw:: html

        <div>
            <h1>John Hopcroft</h1>
            <p>Las fechas de las platicas son:</p>
            <ul>
                <li>Lunes 10 de Agosto, 12:00 horas</li>
                <li>Martes 11 de Agosto, 13:00 horas</li>
            </ul>
        </div>

<span>
~~~~~~

.. code-block:: html
   :linenos:

    John Hopcroft, IBM Professor of Engineering and <span>Applied Mathematics</span>,
    Cornell University


..  admonition:: Resultado
    :class: toggle

    .. raw:: html

      John Hopcroft, IBM Professor of Engineering and <span>Applied Mathematics</span>,
      Cornell University


<iframe>
~~~~~~~~

.. code-block:: html
    :linenos:

    <iframe
      width="600"
      height="450"
      frameborder="0"
      style="border:0"
      src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15059.709826780037!2d-99.18979089002852!3d19.32895393180137!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x85ce000f915a888b%3A0xdf8bcb88b73cde0f!2sFacultad+de+Ciencias!5e0!3m2!1sen!2smx!4v1442601448499">
    </iframe>


..  admonition:: Resultado
    :class: toggle

    .. raw:: html

        <iframe
          width="600"
          height="450"
          frameborder="0"
          style="border:0"
          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15059.709826780037!2d-99.18979089002852!3d19.32895393180137!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x85ce000f915a888b%3A0xdf8bcb88b73cde0f!2sFacultad+de+Ciencias!5e0!3m2!1sen!2smx!4v1442601448499">
        </iframe>


Elementos de HTML5
------------------

<main>
~~~~~~
El área principal del contenido de un documento incluye contenido que es único a ese documento y excluye el contenido que se repite a través de un conjunto de documentos, tales como navegación del sitio, información de copyright, logos de sitio y formularios de búsqueda.

Solo puede haber un elemento *main* por pagína, y no puede ser usado como desendiente de otro elemento semántico.

.. code-block:: html
   :linenos:

   <body>
       <main class="main-container">
           Contenido
       </main>
   </body>

<article>
~~~~~~~~~
Se usa par agrupar un pedaso de contenido independiente. Entradas de un blog,noticias.

.. code-block:: html
   :linenos:

    <body>
        <main class="main-container">
            <article class="article-container flex-container">
                Contenido del articulo
            </article>
        </main>
    </body>


<section>
~~~~~~~~~
Este elemento se usa para definir una sección generica de un documento.

.. code-block:: html
   :linenos:

    <body>
      <main class="main-container" role="main">
        <article class="article-container flex-container">
          <section class="main-content">
            <header>
              <h1>El elemento <code>&lt;main></code> </h1>
            </header>
            <p>Definición:</p>
            <blockquote>
              <p>El elemento Main (<code>&lt;main></code>)
                representa&hellip;</p>
            </blockquote>
          </section>
        </article>
      </main>
    </body>


<nav>
~~~~~
Se usa para agrupar links de navegación a otras páginas o secciónes de la misma pagína.




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


..  admonition:: Resultado
    :class: toggle

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


..  admonition:: Resultado
    :class: toggle

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
Marca información de contacto para el *<article>* o *<body>* que lo contiene.

.. seealso::

    La lista completa de los elementos en HTML5 se puede consultar en
    `<http://www.w3.org/TR/html5/ semantics.html#semantics>`_


Herramientas de desarrollo
--------------------------


.. note::  **HTML5 Boilerplate**. (https://html5boilerplate.com/).
