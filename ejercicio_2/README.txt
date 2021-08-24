README.TXT

EJERCICIO 2

a) Ejecución del programa desde AWS Lambda

1.- Abrir la consola de AWS
2.- Elegir el servicio Lambda
3.- Crear una nueva funcion (desde cero)
4.- Seleccionar tiempo de ejecución Python 3.9
5.- En el codigo fuente insertar el contenido del archivo "lambda_function.py" (59 lineas)
6.- Seleccionar la opcion DEPLOY.
7.- Crear una capa (cualquier nombre) y subir el archivo "PYTHON.ZIP" de la carpeta "LAYER" con tiempo de ejecución Python 3.9
8.- Agregar la capa creada a la función Lambda.
9.- Seleccionar la opcion DEPLOY nuevamente.
10.- Configurar un Test Event (con cualquier nombre y con opciones por defecto).
11.- Ejecutar el Test Event creado
12.- Revisar los resultados de ejecución despues de los 15 minutos requeridos


b) Ejecución del programa desde Python (Visual Studio Code)

1.- Abrir el archivo "python_function.py"
2.- Validar dependencias de los modulos requeridos y que deben estar instalados en el entorno de desarrollo (requests, pymysql).
3.- Ejecutar el programa "python_function.py" previamente abierto.
4.- Verificar la ejecución del programa en el terminal y su finalización luego de los 15 minutos requeridos.

NOTA IMPORTANTE:

Los datos de la base de datos son los siguientes:

HOSTNAME: 	ejercicio2-instancia.cryssnu9ajdn.us-east-2.rds.amazonaws.com
PORT: 		3306 
USERNAME:	ejercicio2admin
PASSWORD:	8XLY3NHHU6WH6ODZMCDj
SCHEMA:		ejercicio2db
TABLE:		ejercicio2_table
