JavaScript
----------

Sintaxis
~~~~~~~~
Algunos ejemplos de sintaxis:

.. code-block:: javascript

    // doble diagonal invertida comienza comentario de una linea

    var x;  // declaración de una variable

    x = 3 + y;  // asigna un valor a la variable `x`

    foo(x, y);  // llmada a la función `foo` con parametros `x` e `y`
    obj.bar(3);  // llamada al método `bar` del objeto `obj`

    // un condicional
    if (x === 0) {  // es `x` igual a cero?
        x = 123;
    }

    // definicíon de la función `baz` con parametros `a` y `b`
    function baz(a, b) {
        return a + b;
    }

Sentencias VS Expresiones
~~~~~~~~~~~~~~~~~~~~~~~~~

Una sentencia representa una instrucción bien definida que es ejecutada por la computadora.

.. code-block:: javascript

    var foo;

Una expresión es una combinación de valores y operaciones que, al ser evaluados, entregan un valor.

.. code-block:: javascript

    3 * 7

En JavaScript hay dos maneras de hacer un `if-then-else`, como una sentencia:

.. code-block:: javascript

    var x;
    if (y >= 0) {
        x = y;
    } else {
        x = -y;
    }

o como una expresión:

.. code-block:: javascript

    var x = y >= 0 ? y : -y;

La expresión se puede usar como argumento en una función:

.. code-block:: javascript

    myFunction(y >= 0 ? y : -y)


Punto y coma
~~~~~~~~~~~~

El punto y coma es opcional en JavaScript.

El punto y coma termina sentencias, no bloques.

.. code-block:: javascript

    // Patron: var _ = ___;
    var x = 3 * 7;
    var f = function () { };  // función expresión dentro de la declaración de variable

Comentarios
~~~~~~~~~~~

Comentarios de una línea:

.. code-block:: javascript

    x++; // comentario de una línea

Comentarios de varias líneas:

.. code-block:: javascript

    /* comentario
       de varias
       líneas.
    */


Variables y tipos de datos
~~~~~~~~~~~~~~~~~~~~~~~~~~

Las variables se declaran antes de usarse:

.. code-block:: javascript

    var foo; // declaramos la variable `foo`
    var foo = 6; //Se puede declarar la variable y asignar un valor:
    foo = 4;

Operadores de asignación compuestos:

.. code-block:: javascript

    x += 1;
    x = x +1;

Nombre de variables
~~~~~~~~~~~~~~~~~~~

El primer caracter de un identificador puede ser cualquier letra Unicode,
el signo de pesos ($) o el guion bajo (_). Los siguientes caracteres pueden ser adicionalmente cualquier digito.

.. code-block:: javascript

    arg0
    _tmp
    $elem
    π


Palabras reservadas:

.. code-block:: javascript

    arguments
    break
    case
    catch
    class
    const
    continue
    debugger
    default
    delete
    do
    else
    enum
    export
    extends
    false
    finally
    for
    function
    if
    implements
    import
    in
    instanceo
    interface
    let
    new
    null
    package
    private
    protected
    public
    return
    static
    super
    switch
    this
    throw
    true
    try
    typeof
    var
    void
    while

Las siguientes no son palabras recervadas, pero deben tratarse como cual.

.. code-block:: javascript

    Infinity
    NaN
    undefined

Los tipos primitivos son `booleans`, `numbers`,  `strings`, `null` y `undefined`.

Todos lo demas son objetos.

Los tipos tienen propiedades.

.. code-block:: javascript

    > var str = 'abc';
    > str.length
    3
    > 'abc'.length
    3

El punto se puede usar para asignar valores a propiedades:

.. code-block:: javascript

    > var obj = {}; // un objeto vacio
    > obj.foo = 123;
    123
    > obj.foo
    123

El punto se puede usar para llamar metodos:

.. code-block:: javascript

    > 'hello'.toUpperCase()
    'HELLO'


La diferencia entre los tipos primitivos y los objetos es que cada objeto tiene una identidad unica y solo es igual a si mismo.

.. code-block:: javascript

    > var obj1 = {};  // un objeto vacio
    > var obj2 = {};  // otro objeto vacio
    > obj1 === obj2
    false
    > obj1 === obj1
    true

.. code-block:: javascript

    > var prim1 = 123;
    > var prim2 = 123;
    > prim1 === prim2
    true


En los tipos primitivos no se puede cambiar, agregar o eliminar propiedades.

.. code-block:: javascript

    > var str = 'abc';

    > str.length = 1; // trata de cambiaar la propiedad `length`
    > str.length      // ⇒ sin efecto
    3

    > str.foo = 3; // trata de agregar la propiedad `foo`
    > str.foo      // ⇒ sin efecto, propiedd desconocida
    undefined

Objetos
~~~~~~~




Funciones
~~~~~~~~~

Arreglos
~~~~~~~~

Pruebas
~~~~~~~

Herramientas de desarrollo
~~~~~~~~~~~~~~~~~~~~~~~~~~

Exercise 1
^^^^^^^^^^

Your mission, should you choose to accept it...

..  admonition:: Solution
    :class: toggle

    To save the world with only seconds to spare do the following:

    .. code-block:: python

        from plone import api
