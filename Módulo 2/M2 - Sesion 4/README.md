# Módulo II - Sesión IV

## Agenda

- Atributos CSS más utilizados
- Media Query
- Ejercicios
- Práctica

### Atributos

Ir a la [página de W3Schools](https://www.w3schools.com/cssref/index.php) es la manera más rapida de acceder a los atributos del lenguaje, de todas maneras, hay algunas de uso bastante común.

- color
- background-color
- border
- font-family
- grid
- height
- margin
- padding
- opacity
- text-align

### Media Queries

Son reglas que nos permiten adaptar la pagina web para dispositivos moviles, tomando en cuenta la metodología de desarrollo Mobile First y sus convenciones.

- xs: Extra Small
- sm: Small
- md: Medium
- lg: Large
- xl: Extra Large
- xxl: Double Extra Large

---

## Responsividad y Mobile First

### ¿Qué es el diseño web responsivo?

El diseño web responsivo o "responsive web design" en inglés, se refiere a la adaptabilidad de una página en internet hacia los diferentes equipos desde los cuales pueda ser accedido. Por ejemplo, poder adaptarse a la pantalla de una tablet, laptop, smartphone, pantalla ancha, etc. Siempre comenzando su diseño con una pantalla de ordenador y luego adaptándolo a los distintos tamaños.

### ¿Por qué es importante la responsividad?

Hoy las personas realizan prácticamente todo usando su smartphone. Desde una compra, una hora médica, un video de entretenimiento o buscar información sobre algún tema específico, hasta estudiar en plataformas educativas. De hecho, ciertos estudios (estudios estadísticos: GSMA Intelligence DATA y Ericson Mobilitu Report Data) indican que alrededor del 55% de las visitas a páginas web se realizan a través de smartphone, lo que hace relevante para los sitios web tener su material adaptado para ser visitado a través de pantallas de celulares ya que, según este porcentaje, laptop y Tablet ya han sido desplazadas.

### ¿Qué es el Mobile First Design?

Mobile First en español significa "móvil primero" y se enfoca en diseñar primero el sitio web desde las pantallas móviles más pequeñas con el objetivo de crear la mejor experiencia de usuario para las personas que visitan web a través de teléfonos inteligentes. Crear primero el diseño para los dispositivos móviles puede ser más difícil que crear primero el diseño para dispositivos de escritorio, sin embargo, permite diseñar una experiencia móvil de calidad sin encontrarse limitado por el diseño web de escritorio terminado.

### Usando los Media Queries para desarrolar con Mobile First

Las Medias Queries son una de las principales novedades de CSS 3 y son útiles cuando deseamos modificar una página web en función del tipo de dispositivo o de características o parámetros específicos.

La ventaja principal de utilizar las Media Queries es que partimos de un único diseño principal que se irá adaptando y reajustando en función del navegador, el dispositivo, la pantalla o las preferencias del usuario.

```CSS
@media(min-width: 1200px){
    .primero{
        background-color: black;
    }
    .segundo{
        background-color: blanchedalmond;
    }
}
```

### Ventajas del diseño web responsivo

- Mejorar la experiencia del usuario
- Mejones pocisionamientos en buscadores
- Es práctico
- Los elementos se ajustan automáticamente para un desplazamiento vertical
- Las imágenes se adaptan al diseño
