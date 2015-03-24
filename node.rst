Noe.js
======

Los binarios de node los podemos encontrar en ::

    /usr/local/bin/node
    /usr/local/bin/npm



The ~/.npm folder is a cache folder that contains local packages so that you don't have to download them over and over when you install them in a new project. You can safely delete this folder and you can in fact do it using the npm cache command ::

    $ npm cache clean

The ~/.node-gyp folder is the devDir of node-gyp (see relevant source code). This is where development header files are copied in order to perform the compilation of native modules. you can safely delete this directory, as it will be re-created the next time you'll install a module that needs node-gyp.


Folder Structures Used by npm https://docs.npmjs.com/files/folders



pkg-config
----------

Check for pkg-config via $ which pkg-config, if not found you will want to install it ::

    $ curl http://pkgconfig.freedesktop.org/releases/pkg-config-0.28.tar.gz -o pkgconfig.tgz
    $ tar -zxf pkgconfig.tgz && cd pkg-config-0.28
    $ ./configure --with-internal-glib
    $ sudo make install

Check for pkg-config via $ which pkg-config


Pixam
-----

the pixel manipulation dependency of cairo

    $ curl http://www.cairographics.org/releases/pixman-0.32.6.tar.gz -o pixman-0.32.6.tar.gz
    $ tar -zxf pixman-0.32.6.tar.gz && cd pixman-0.32.6/
    $ ./configure --prefix=/usr/local --disable-dependency-tracking
    $ make install

libpng
------
    $ curl http://downloads.sourceforge.net/project/libpng/libpng16/1.6.16/libpng-1.6.16.tar.gz -o libpng-1.6.16.tar.gz
    $ tar xfzv libpng-1.6.16.tar.gz && cd libpng-1.6.16/
    $ ./configure --prefix=/usr/local
    $ make install

giflib
------

    $ curl https://downloads.sourceforge.net/project/giflib/giflib-5.x/giflib-5.1.1/giflib-5.1.1.tar.gz -o giflib-5.1.1.tar.gz
    $ tar -zxf giflib-5.1.1.tar.gz && cd giflib-5.1.1/
    $ ./configure --prefix=/usr/local
    $ make install

freetype
--------

    $ curl http://download.savannah.gnu.org/releases/freetype/freetype-2.5.5.tar.gz -o freetype-2.5.5.tar.gz
    $ tar xfvz freetype-2.5.5.tar.gz && cd freetype-2.5.5/
    $ ./configure --prefix=/usr/local
    $ make install


cairo
-----

    curl http://cairographics.org/releases/cairo-1.14.2.tar.xz -o cairo-1.14.2.tar.xz
    https://github.com/Automattic/node-canvas/wiki/Installation---OSX
    $ tar -xf cairo.tar.xz && cd cairo-1.12.8
    $ ./configure --prefix=/usr/local --disable-dependency-tracking
    $ make install

https://github.com/Automattic/node-canvas/wiki/Installation---OSX

https://github.com/creationix/nvm
