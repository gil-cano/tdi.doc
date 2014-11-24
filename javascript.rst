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

Los tipos mas comunes de objetos son:

* Objetos simples

.. code-block:: javascript

    {
        firstName: 'Eduardo',
        lastName: 'Chavez'
    }

* Arreglos (los indices empiezan en 0)

.. code-block:: javascript

    ['manzana', 'platano', 'sandia']

* Expresiones Regulares


.. code-block:: javascript

    /^a+b+$/

Los objetos tienen las siguientes caracteristicas

* Se comparan por referencia

.. code-block:: javascript

    > {} === {}  // two different empty objects
    false

    > var obj1 = {};
    > var obj2 = obj1;
    > obj1 === obj2
    true

* Modificables por default. Podemos cambiar, agregar y borrar propiedades

.. code-block:: javascript

    > var obj = {};
    > obj.foo = 123; // add property `foo`
    > obj.foo
    123

undefined y null
~~~~~~~~~~~~~~~~

`undefined` quiere decir "Sin valor". Variables no inicializadas son `undefined`

.. code-block:: javascript

    > var foo;
    > foo
    undefined

Paramaetros omitidos son `undefined`

.. code-block:: javascript

    > function f(x) { return x }
    > f()
    undefined

Si leemos una propiedad que no existe nos da un `undefined`

.. code-block:: javascript

    > var obj = {}; // empty object
    > obj.foo
    undefined

`null` se refiere a que no existe el objeto.

Las funciones te permiten indicar la falta de un valor con `undefined` o con `null`.

.. code-block:: javascript

    if (x === undefined || x === null) {
        ...
    }

`undefined` y `null` se consideran `false`


.. code-block:: javascript

    if (!x) {
        ...
    }

typeof e instanceof
~~~~~~~~~~~~~~~~~~~

`typeof` regresa una cadena describiendo el "tipo"

.. code-block:: javascript

    > typeof true
    'boolean'
    > typeof 'abc'
    'string'
    > typeof {} // objeto vacio
    'object'
    > typeof [] // arreglo vacio
    'object'

`typeof null` regresa `object`, estees un bug que no puede ser coregido, por que romperia codigo existente. Esto no quiere decir que `null` sea un objeto.


`instanceof`

.. code-block:: javascript

    > var b = new Bar();  // object creado por el constructor Bar
    > b instanceof Bar
    true

    > {} instanceof Object
    true
    > [] instanceof Array
    true
    > [] instanceof Object  // un arreglo es un objeto
    true

    > undefined instanceof Object
    false
    > null instanceof Object
    false

Booleanos
~~~~~~~~~

El tipo primitivo `boolean` usa los valores `true` y `false`.

Los siguientes operadores producen booleanos:

* operadores logicos: && (And), || (Or)

* operadores logicos de prefijo: !(Not)

* operadores de comparación:

    * de igualdad: ===, !==, ==, !=

    * operadores de orden: >, >=, <, <=

Los siguientes valores se interpretan como falsos:

* undefined, null

* Boolean: false

* Number: -0, NaN

* String: ''

La función Boolean convierte su parametro a un booleano.

.. code-block:: javascript

    > Boolean(undefined)
    false
    > Boolean(0)
    false
    > Boolean(3)
    true
    > Boolean({}) // objeto vacio
    true
    > Boolean([]) // objeto vacio
    true

Los operadores logicos son de corto-circuito:

.. code-block:: javascript

    > NaN && 'abc'
    NaN
    > 123 && 'abc'
    'abc'

    > 'abc' || 123
    'abc'
    > '' || 123
    123

Números
~~~~~~~

Todos los números son flotantes

.. code-block:: javascript

    > 1 === 1.0
    true

Tenemos el número 'NaN' (not a number)

.. code-block:: javascript

    > Number('xyz')  // 'xyz' no puede ser convertida a número
    NaN


Infinity:

.. code-block:: javascript

    > 3 / 0
    Infinity
    > Math.pow(2, 1024)  // número muy grande
    Infinity


Operadores aritmeticos:

* Suma: n1 + n2

* Resta: n1 - n2

* Multiplicación: n1 * n2

* División: n1 / n2

* Residuo: n1 % n2

* Incremento: ++variable, variable++

* Decremento: --variable, variable--

* Negativos: -valor

* Comvierte a número: +valor


Cadenas
~~~~~~~

.. code-block:: javascript

    'abc'
    "abc"

    'Did she say "Hello"?'
    "Did she say \"Hello\"?"

    'That\'s nice!'
    "That's nice!"

    'Line 1\nLine 2'  // salto de linea
    'Backlash: \\'


.. code-block:: javascript

    > var str = 'abc';
    > str[1]
    'b'

.. code-block:: javascript

    > 'abc'.length
    3

Las cadenas on inmutables.

Concatenación:

.. code-block:: javascript

    > var messageCount = 3;
    > 'You have ' + messageCount + ' messages'
    'You have 3 messages'

    > var str = '';
    > str += 'Multiple ';
    > str += 'pieces ';
    > str += 'are concatenated.';
    > str
    'Multiple pieces are concatenated.'


Metodos de cadenas:

.. code-block:: javascript

    > 'abc'.slice(1)  // copia una cadena
    'bc'
    > 'abc'.slice(1, 2)
    'b'

    > '\t xyz  '.trim()  // elimina espacios en blanco
    'xyz'

    > 'mjölnir'.toUpperCase()
    'MJÖLNIR'

    > 'abc'.indexOf('b')  // encuentra una cadena
    1
    > 'abc'.indexOf('x')
    -1

Condicionales
~~~~~~~~~~~~~

La sentencia `if` tiene una clausula `then` y una opcional `else`.

.. code-block:: javascript

    if (myvar === 0) {
        // then
    }

    if (myvar === 0) {
        // then
    } else {
        // else
    }

    if (myvar === 0) {
        // then
    } else if (myvar === 1) {
        // else-if
    } else if (myvar === 2) {
        // else-if
    } else {
        // else
    }

    if (x < 0) return -x;


.. code-block:: javascript

    switch (fruit) {
        case 'banana':
            // ...
            break;
        case 'apple':
            // ...
            break;
        default:  // los demas casos
            // ...
    }

El operador despues del `case` puede ser cualquier expresión: Se compara via ===
con el parametro del `switch`


Ciclos
~~~~~~

.. code-block:: javascript

    for (var i=0; i < arr.length; i++) {
        console.log(arr[i]);
    }

.. code-block:: javascript

    var i = 0;
    while (i < arr.length) {
        console.log(arr[i]);
        i++;
    }

.. code-block:: javascript

    do {
        // ...
    } while (condition);


* `brake` sale del ciclo

* `continue` comienza una nueva iteración


Funciones
~~~~~~~~~

.. code-block:: javascript

    function add(param1, param2) {
        return param1 + param2;
    }

.. code-block:: javascript

    > add(6, 1)
    7
    > add('a', 'b')
    'ab'

Otra manera de definir la funcion es:

.. code-block:: javascript

    var add = function (param1, param2) {
        return param1 + param2;
    };


Una funcion de espresión produce un valor y puede ser usado para pasar directamente funciones como argumentos a otras funciones:


.. code-block:: javascript

    someOtherFunction(function (p1, p2) { ... });


La declaración de funciones es movida al inicio del "bloque" actual:

.. code-block:: javascript

    function foo() {
        bar();  // OK
        function bar() {
            ...
        }
    }

La asignacion de variables no lo es

.. code-block:: javascript

    function foo() {
        bar();  // Not OK, bar is still undefined
        var bar = function () {
            // ...
        };
    }

La vsariable especial `arguments`

.. code-block:: javascript

    > function f() { return arguments }
    > var args = f('a', 'b', 'c');
    > args.length
    3
    > args[0]  // read element at index 0
    'a'


Agregar JavaScript a HTML
~~~~~~~~~~~~~~~~~~~~~~~~~


n between the <body> tags add a button like this:

.. code-block:: html

    <button onclick="sayHello('world')">Enviar</button>

*Linking to the JavaScript File*

When you click on the "Click Me" button, nothing happens yet but we want to make it so that clicking on this button will trigger a JavaScript function called sayHello.

In between the <head> tags add start and ending script tags like: <script></script>

Now add the attribute to <script> called type like type="text/javascript". This tells the web browser that the script we are linking to is JavaScript.

Lastly tell the browser where the JavaScript file is by adding a source attribute which looks like src="script.js". This is the directory path of the script.js file. For this exercise, our script is in the same directory as the html file so we just need to put the name of the file inside the src attribute.

.. code-block:: html

    <head>
        <script type="text/javascript" src="script.js"/>
    </head>

*Say Hello with JavaScript*

Now we have a script in place. Let's add the sayHello function to it.

In the Functions with JavaScript course you learned about variables in functions.

Our sayHello function has one parameter and its code will be a simple alert that will produce a pop-up when you click on the "Click Me" button. An alert can be used to display immediate messages in the web browser.

In this exercise the parameter will be sent by the onClick event inside the parenthesis like onclick="sayHello('world').

JavaScript events are actions that can be detected by JavaScript. onclick is an example of an event. Here's a list of other events.

.. code-block:: javascript

    function sayHello() {

    }

*Writing to the Page*

When HTML is rendered in a browser, the browser stores the mark-up in the DOM (Document Object Model). JavaScript can be used to change or add to the HTML that is in the DOM.

.. code-block:: javascript

    function sayHello(name) {
        alert ("Hello " + name);
    }

.. code-block:: html

    <html>
    <head>
        <script type="text/javascript" src="script.js"></script>
    </head>

    <body>

    <button onclick="sayHello('world')">Click Me</button>

    </body>

    </html>


In the HTML tab, below the <button> code, add start and ending <div> tags.

Add an attribute to the <div> as id="result".

In the JavaScript tab, inside the sayHello function, replace the alert code with: document.getElementById("result").innerHTML = 'Hello ' + name + '!';

Click on the result tab, click on the "Click Me" button and see that your hello message is now displayed below the button!

.. code-block:: html

    <html>
    <head>
        <script type="text/javascript" src="script.js"></script>
    </head>

    <body>

    <button onclick="sayHello('world')">Click Me</button>
    <div id="result"></div>
    </body>

    </html>


.. code-block:: javascript

    function sayHello(name){
        document.getElementById("result").innerHTML = 'Hello ' + name + '!';
    }


*Adding More Values and More DIVS*

In the previous exercise we wrote to one <div>. In this exercise, let's add another one and let's also add another parameter to your sayHello function.


In the JavaScript tab, in the sayHello function, add another parameter called name2. Add a comma between the parameters.

Now that the sayHello function expects two parameters. Add a second value to the onClick event in the HTML. This can be any word you'd like.

While on the HTML tab, add a second <div> with an id attribute of result2. Now you have a <div> for each value that will be submitted to the function.

In the JavaScript tab, add a second line of code that writes the parameter name2 and uses the result2 id.

When you click on "Click Me" in the Results tab, you should see the values submitted in the onClick are printing to the DOM in their own <div>s just as you specified. Nice job!



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



http://www.codecademy.com/courses/html-javascript-css/0/4
https://speakerdeck.com/ariya/javascript-and-the-browser-under-the-hood
