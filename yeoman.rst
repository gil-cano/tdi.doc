YEOMAN
======

`Yeoman <http://yeoman.io/>`_ ayuda a generar nuevos proyectos, siguiriendo las mejores parcticas y herraminetas para ser productivo.

* Workflow moderno para Apps modernas
* Tres componentes
   * `Yo <https://github.com/yeoman/yo>`_
   * `Bower <http://bower.io/>`_
   * `Grunt <http://gruntjs.com/>`_

Primero nececitamos instalar *Yo* y otras herramientas ::

    $ npm install -g yo
    $ npm install -g bower
    $ npm install -g grunt-cli

npm es el manejador de paquetes de Node.js

Para generar una aplicacción web necesitamos instalar el generador *generator-webapp* ::

    $ npm install -g generator-webapp

Este es el generador de aplicaciones web default que construira un proeyecto que contiene `HTML5 Boilerplate <http://html5boilerplate.com/>`_, `jQuery <http://jquery.com/>`_, `Modernizr <http://modernizr.com/>`_, and `Bootstrap <http://getbootstrap.com/>`_.

Una vez que el generador esta instalado creamos un directorio ::

    $ mkdir yo-project
    $ cd yo-project

despues ejecutamos ::

    $ yo webapp

         _-----_
        |       |    .--------------------------.
        |--(o)--|    |    Welcome to Yeoman,    |
       `---------´   |   ladies and gentlemen!  |
        ( _´U`_ )    '--------------------------'
        /___A___\
         |  ~  |
       __'.___.'__
     ´   `  |° ´ Y `

    Out of the box I include HTML5 Boilerplate, jQuery, and a Gruntfile.js to build your app.
    ? What more would you like?

Bower
-----
`Bower <http://bower.io/>`_ es un manejador de paquetes para web. ::

    # Search for a dependency in the Bower registry.
    $ bower search <dep>

    # Install one or more dependencies.
    $ bower install <dep>..<depN>

    # List out the dependencies you have installed for a project.
    $ bower list

    # Update a dependency to the latest version available.
    $ bower update <dep>

::

    # List out the dependencies you have installed for a project.
    $ bower list

    # Search Bower's registry for the plug-in we want.
    $ bower search bootstrap

    # Install it and save it to bower.json
    $ bower install bootstrap --save

    # Injects your dependencies into your index.html file.
    $ grunt wiredep

Grunt
-----

`Grunt <http://gruntjs.com/>`_ es una herramienta de manejo de tareas para proyectos de javascript ::

    # Preview an app you have generated (with Livereload).
    $ grunt serve

    # Run the unit tests for an app.
    $ grunt test

    # Build an optimized, production-ready version of your app.
    $ grunt

Yeoman Workflow
---------------

::

    $ yo webapp
    $ grunt serve
    $ grunt test
    $ grunt
