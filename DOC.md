# Informe Académico
Proyecto de Sistemas de Bases de Datos II, Tema Skyrim, Equipo #3:

- Eduardo García Maleta
- Carlos Luis Águila Fajardo
- Ricardo Piloto Marín

## 1. Introducción
El proyecto desarrolla una base de datos sobre el videojuego The Elder Scrolls V: Skyrim, donde los desarrolladores podrán tener una productiva forma de interactuar con la plataforma. Detallamos las diferentes funciones de nuestra plataforma y de cómo ha sido gestionado su desarrollo.

El cliente hizo la petición de una plataforma amigable, con funciones como: saber la raza de las bestias que más han participado en batallas; los diez jugadores con mayor cantidad de batallas ganadas; las batallas de mayor duración; los jugadores que mayor cantidad de puntos de daño han ocasionado en todas las batallas efectuadas; los tipos de daño de los cinco hechizos más empleados en batallas; los hechizos más conocidos y los menos usados por los jugadores. Todos estos requisitos fueron transformados a requerimientos más concretos y fueron desarrollados en la base de datos junto a la aplicación web como interfaz del usuario.

## 2. Análisis de requerimientos
El elemento central del proyecto es una base de datos relacional creada mediante la herramienta Django a partir de SQLite. EL desarrollo se basa para el almacenamiento de:

- Datos de los jugadores.
- Datos sobre criaturas del juego. 
- Información sobre los posibles eventos del juego (batallas, ataques de criaturas, acciones, etc).

También se puede acceder a ciertos datos representativos variables sin tiempo de espera adicional:

- Las bestias y jugadores que han participado en determinadas batallas.
- Conocer los hechizos más o menos usados.
- Saber sobre Batallas más o menos duraderas.
- Los participantes con mayor cantidad de batallas ganadas ordenados ascendentemente.
- Los participantes que mayor cantidad de puntos de daño han ocasionado en todas las batallas efectuadas.

Es necesario utilizar SQLite, por la disponibilidad para dar mantenimiento y la familiaridad del cliente. La interfaz del usuario tiene un desempeño con características lo más familiar posibles para los usuarios, esto facilitará la experiencia en el uso de otras aplicaciones web y/o de escritorio del mismo tipo. Como requisito personal del cliente, se adjuntará una sólida documentación para la administración y mantenimientos de la base de datos, así como un manual de usuario de forma offline.

## 3. Solución Propuesta 
La arquitectura que ha sido utilizada es Cliente-Servidor, donde el software se organiza en dos partes independientes. Tomada esta arquitectura por su sencillez, fácil manejo y mantenimiento, pues las responsabilidades están repartidas de forma modular, lo cual es posible arreglar o reemplazar un servidor, mientras que los clientes no se afectan. 

Las tecnologías que fueron utilizadas tienen un buen acoplamiento con este paradigma de Cliente-Servidor. También fue escogida ya que esta arquitectura es una estándar debido a que el modelo es muy popular y funcional en Web, sobre todo para la gestión de datos.

Entre las tecnologías utilizadas: SQLite como sistema gestor de Base de Datos (esto fue un cambio pq al inicio se dijo que se usaría MySQL), y también Python con Django como entorno para el desarrollo de la Aplicación Web. Adicional a esto, por su buen acoplamiento con Django, fue utilizado Bootstrap para la interfaz de usuario.

La solución parte de un esquema relacional, esquema que se encuentra en TERCERA FORMA NORMAL (3FN) porque está en 2Fn, 1FN y cada uno de sus determinantes constituye una llave candidata. Se cumple la propiedad
de Join sin pérdida de información PLJ en las parejas de relaciones a las
que se les va a hacer, así como la PPDF, por tanto, podemos asegurar que el diseño es teóricamente correcto.

Luego de tener un diseño correcto se desarrolló la lógica de la solución con Django, primero haciendo un modelado correcto del esquema con los Models en Django, estableciendo cada entidad, atributo y relación necesaria partir del esquema relacional. Luego se trabajó en el esqueleto de la aplicación web y su home page, así como en cada uno de los respectivos formularios; y para finalizar, una revisión de esta aplicación.

Luego, para hacer más amigable la interfaz, se utilizó Bootstrap, una colección acoplable de archivos predefinidos de CSS y JavaScript (.css, .js) creada para facilitar el trabajo de frontend de los desarrolladores al implementar servicios web. Esto nos permitió concentrarnos mucho más en la parte lógica del servicio, dígase, el lado del servidor, garantizando que la parte estética estuviera fácilmente accesible al comenzar a desarrollarla.

## 4. Resultados obtenidos 
La plataforma es capaz de mostrar, añadir, organizar, eliminar y modificar la Base de Datos. Al instante del usuario realizar una determinada consulta, la aplicación web enviará la solicitud, luego, la vista obtiene los datos a partir del modelo, seguidamente la vista llama a la plantilla y finalmente la plantilla muestra la respuesta a la solicitud en la aplicación web.

Por petición del cliente, para que cualquier empleado, independientemente de su sistema operativo, pueda acceder a los datos, se desarrolló una aplicación web accesible desde cualquier navegador moderno y, por tanto, desde cualquier dispositivo de escritorio independientemente del sistema, autorizado previamente por los administradores.

Se ha logrado una interfaz simple y minimalista para todo el que tenga acceso a visualizar los datos. Adicionalmente, se pide que las medidas de seguridad sean implementadas de manera lo menos molesta posible, es decir, no más que un requerimiento de usuario/contraseña.

## 5. Conclusiones
Nuestro proyecto desarrolló una base de datos sobre el videojuego The Elder Scrolls V: Skyrim, donde los desarrolladores podrán tener una productiva forma de interactuar con la plataforma. Se logró cumplir con todos los objetivos y requerimientos pedidos por el cliente, así como con una interfaz amigable y sencilla para cualquier tipo de usuario.

## 6. Bibliografía Libros de texto, sitios visitados, manuales de ayuda de los lenguajes y plataformas utilizadas
- Documentación oficial de Python (ver. 3.9.1)
- Documentación oficial de Django (ver. 3.0)
- Documentación oficial de Bootstrap (ver. 5.0)
- Tutorial de inicio en Django: [LINK](https://developer.mozilla.org/es/docs/Learn/Server-side/Django/)