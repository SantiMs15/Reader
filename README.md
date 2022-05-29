Contextualización del proyecto.

Nuestro proyecto consiste en la creación de un programa que sea capaz de interpretar cantidad de páginas y emitir audio de la lectura de archivos pdf,
en este caso son libros de diferentes generos literarios que se encuentran en una determimnada carpeta en el equipo.

Para ello el programa en primera instancia preguntará el genero del libro y según la respuesta procedera a dar la información del libro e iniciara su lectura. 

Estructura del proyecto:

Los libros se encuentran en la carpeta "libros" del repositorio.

Argumentos:
a(str): Genero de libro a solicitar

Returns:
Descripción del libro: Título del libro (str) y cantida de páginas que lo integran (int).
Audio: Lectura del libro según el genero elegido.

Librerías.

Para la realización de este proyecto fue necesaria la instalación de dos librerías: 

pyttsx3: Esta es una librería text-to-speech, es decir, que su función es convertir texto a audio, es indispensable para nuestro código ya que al tratarse de un
audiolibro pues necesitamos hacer esta conversión, usamos esta librería principalmente porque se trata de un convertidor offline, es decir, que funciona sin estar
conectado a una red y por su sencillez a la hora de aplicarla y entender su funcionamiento. Esta librería es la que hace que nuestro programa hable.

Código para agregar pyttsx3 a VisualStudioCode: pip install pyttsx3
Documentación completa de la librería pyttsx3: https://pyttsx3.readthedocs.io/en/latest/

PyPDF2: Esta es una librería de interpretación y de edición de archivos PDF, especificamente, esta librería nos permite fusionar, recortar y transformar 
las páginas de los archivos PDF que se especifiquen en el código. Es de código abierto por lo que todos pueden colaborar para agregar funciones y/o arreglar posibles
errores en su funcionamiento. Esta librería es la que le indica a nuestro programa que contenido y como tiene que leer dicho contenido de los documentos.

Código para agregar PyPDF2 a VisualStudioCode: pip install PyPDF2
Documentación completa de la librería PyPDF2: https://pypdf2.readthedocs.io/en/latest/

