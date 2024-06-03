Tarea 3
Este repositorio contiene ejercicios prácticos relacionados con la manipulación de estructuras de datos en Python mediante el uso de rutas web, parte de la asignatura de programación.

Contenido del Proyecto
El archivo principal es:

practica3.py: Contiene funciones para manipular diccionarios, conjuntos y tuplas a través de rutas web, así como ejemplos de uso de cada una de estas funciones.
Estructura de practica3.py
Rutas para Diccionarios
agregar_a_diccionario: Agrega una clave-valor a un diccionario.
eliminar_de_diccionario: Elimina una clave-valor de un diccionario.
modificar_diccionario: Modifica el valor de una clave en un diccionario.
combinar_diccionarios_route: Combina dos diccionarios.
Rutas para Conjuntos
agregar_a_conjunto: Agrega un elemento a un conjunto.
eliminar_de_conjunto: Elimina un elemento de un conjunto.
combinar_conjuntos_route: Combina dos conjuntos.
diferencia_conjuntos_route: Obtiene la diferencia entre dos conjuntos.
Rutas para Tuplas
agregar_a_tupla: Agrega un elemento a una tupla.
eliminar_de_tupla: Elimina un elemento de una tupla.
concatenar_tuplas_route: Concatena dos tuplas.
revertir_tupla_route: Revierte una tupla.
Rutas para Imprimir
imprimir_diccionario: Imprime un diccionario.
imprimir_tupla: Imprime una tupla.
imprimir_conjunto: Imprime un conjunto.
Ejemplos de Uso
Para probar las rutas, asegúrate de codificar los diccionarios, conjuntos y tuplas en formato JSON en la URL. Por ejemplo:

plaintext
Copiar código
http://127.0.0.1:5000/dict/agregar/{"a":1}/b/2
http://127.0.0.1:5000/set/agregar/[1,2,3]/4
http://127.0.0.1:5000/tuple/agregar/[1,2,3]/4
Contribuciones
Las contribuciones son bienvenidas. Puedes hacer un fork del repositorio, hacer tus cambios y enviar un pull request.

Contacto
Para cualquier duda o sugerencia, puedes contactarme en: a18490949@itmexicali.edu.mx

Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para obtener más información.
