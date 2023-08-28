# Extracción de Datos mediante Scrapy
# Universidad técnica particular de Loja UTPL

1. **Introducción**
   
En el marco del presente proyecto, se llevó a cabo la extracción de datos informativos de cada carrera ofrecida por la Universidad Técnica Particular de Loja.

Utilizando la poderoza herramienta de **Beautiful Soup**, con la cual se exploró en url como **https://www.utpl.edu.ec**, con el propósito de recopilar información relevante para un análisis posterior.

La información contiene una variedad de campos, incluidos nombres de la carrera, número de ciclos, título, modalidad,detalles de la carrera, materias, ciclo, campo ocupacional entre otros.

El desafío enfrentado en el proceso de scrapear los datos se pudó observar la irregularidad en algunos campos de distintas carreras es decir en la variabilidad de la estructura de las páginas HTML. Por ende se realizó una documentación para tener constancia de los errores o datos faltantes en algunos campos.

3. **Herramientas utilizadas**
   
Para el proceso de extracci´ñon de datos se hizo uso de varias herramientas y un proceso especifico para garantizar una recopilación precisa y estructurada de la información.

*. Exploración con Beautiful Soup
   Inicialmente se utilizó la biblioteca en Python para explorar la estructura HTML de las paginas del sitio WEb UTPL para cada carrera, lo que permitió identificar los elementos y atributos relevantes que contenían la información deseada.
   
*. Desarrollo de arañas Scrapy Personalizadas

   Luego de comprender la estructura HTML de cada página, se procedio a desarrollar arañas Scrapy personalizadas para cada modalidad.
   
   Debido a que cada integrante utilizó distintas herramientas para scrapear, se procedio a combinar y unificar el código en una única araña Scrapy con BeatifulSoup.
   
*. Guardado de Datos en un Archivo CSV

   Una vez que los datos son extraídos, procesados y estructurados, fueron guardados en un archivo CSV para su fácil manejo y análisis posterior.

*. Python

   Este lenguaje de programación proporcionó la flexibilidad necesaria para adaptar el proceso según nuestros requerimientos.
   
5. **Datos extraídos**
6. **Resultados y conclusiones**
7. **Trabajo a futuro**
8. **Referencias**
