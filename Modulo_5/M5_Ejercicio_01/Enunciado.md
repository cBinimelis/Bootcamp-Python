# Sistema de invernaderos

La Region de Ovalle quiere desarrollar un sistema de gestión para todos los invernaderos de las diferentes comunidades, donde se cultivan distintas especies de plantas en condiciones controladas. Cada invernadero está equipado con sensores que miden variables ambientales (temperatura, humedad, luminosidad) y que permiten observar y registrar el crecimiento de cada planta a lo largo del tiempo.

## El sistema debe:

1. Registrar cada pyme que utiliza invernaderos para cultivo
2. La ubicación de cada invernadero debe ser detallada, incluso poder mostrarse en un mapa.
3. Almacenar información detallada sobre cada planta cultivada en cada
   invernadero(especie, fecha de plantación, características genéticas).
4. En los invernaderos existen secciones donde cada planta está ubicada.
   lo que permite monitores diferentes variables ambientales a traves de
   sensores en cada planta.
5. Cada planta tiene sus propias características que la identifican, asi como
   el tipo de variables a sensar
6. Guardar las lecturas de sensores cada 15 minutos para cada
   invernadero y planta
7. Permitir registrar y monitorear el uso de diferentes tratamientos
   aplicados (fertilizantes, productos para control de plagas, y nutrientes
   específicos). por invernadero y por planta.
8. cada invernadero tiene diferentes actuadores, que permiten regular la
   temperatura y humedad del ambiente, asi como el ph y humedad de
   piso, todo esto en cada sector de cada invernadero.
9. Se debe registrar los trabajadores de pyme, asi como los turnos e
   invernaderos que controlan, a fin de saber quien esta en cada turno al
   pendiente de los sensores y actuadores

## Tareas a Realizar

- Modelo entidad relacion del sistema, aplicando las tres formas
  normales, incluir relaciones y cardinalidad de las relaciones asi como el
  nombre de estas
- Poblar la base de datos con informacion
- Realizar las siguientes consultan en el lenguaje sql:
  - Determinar el promedio de temperatura y humedad de cada
    invernadero en los últimos 30 días, agrupando los resultados por
    invernadero y día, y ordenándolos de mayor a menor promedio de
    temperatura.
  - Listar el total de aplicaciones de cada tratamiento para cada
    especie de planta en un rango de fechas dado, con el porcentaje del
    total de aplicaciones realizadas a cada planta en comparación con el
    total general de esa especie.
  - Mostrar la evolución diaria del crecimiento promedio de cada
    planta para cada especie en el último año, tomando como criterio de
    crecimiento la altura registrada.
  - Listar los trabajadores que han trabajado en al menos dos
    invernaderos diferentes en el último año, las especies que le toco
    supervisar
