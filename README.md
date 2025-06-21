## todo

## notes

<!-- En la sección 2.2.1, eliminaría el item de "metodoloxía" y todo lo que cuelta de él. No dice gran cosa ni aporta nada nuevo que no se vaya a discutir ya en estado del arte. -->

<!-- Por otra parte, en la sección 2.2.1, falta un párrafo al final contextualizando, dentro de todo esa variedad de formas de registro y opciones, dónde se centra o donde encaja el presente trabajo. -->

<!-- En general, la colocación de las figuras es bastante deficiente. Mi recomendación es que hagas lo siguiente:
        Las figuras y flotantes se deben definir justo despues de donde son citadas por primera vez. Puede incluso ser en el medio de un párrafo, simplemente poniendo lineas vacías que empiezan con %
        Siempre con la opción [tbp]. Es decir, que lo coloque cuanto antes arriba de la página, sino abajo, y solo si no se puede al final del capítulo en página de figuras. Para que esto funcione bien, es importante hacer lo de antes, para que haya suficiente texto entre definiciones de figuras, y que las figuras estén definidas lo antes posible.
        Compilar varias veces para que se ajuste el documento -->

<!-- En 2.2.2.1, en la descripción de métodos FBR, tanto FLANN como RANSAC no se ajustan a lo que ahí pones como "descripción". Son más bien matching, y están más relacionados con la estimación de la transofrmación que con la descripción. -->
<!-- 
En la sección 2.2.2.2, los primeros párrafos hacen básicamente referencia a métodos de regresión directa, y ese texto se debería encajar en el párrafo correspondiente. Eliminaría los métodos basados en GAN o los encajaría dentro del paradigma que corresponda. GAN es un método para hacer algo, no lo que hacer. -->

<!-- Falta discutir estado del arte en registro de retinas -->

<!-- Falta introducir registro basado en INR en algún punto del contexto -->

<!-- Falta una discusión de donde encaja el trabajo dentro de ese estado del arte -->

<!-- En el capítulo 3, la tabla 3.1 está claramente mal colocada. Parece definida como [h] (y no [tbp]) y en la sección de datasets, en lugar de hardware. No está citada en el texto. -->

<!-- El diagrama de gantt no está citado en el texto, y debería corresponder a la sección de planificación (si es que representa una planificación) o a la de seguimiento (si es que representa la ejecución). En cualquier caso, se debe citar para presentarlo y discutirlo. -->

<!-- El coste de 12€/h no está justificado. Con ese dinero no contratas ni a un empleado del hogar. Coste es coste, no lo que cobras neto asumiendo que todas las horas de la jornada son productivas. -->

<!-- En el capítulo 4, la sección 4.1 tiene que mejorar. El objetivo debe ser que el que lea esa sección pueda entender de forma general todo el trabajo que se ha realizado, por lo que debe identificar claramente todo lo que se ha realizado con un resumen intuitivo de cada parte. -->

<!-- La seccion 4.3.1 ventila en una frase procesos completos como el muestreo -->

<!-- La sección 4.5.1 no puede ser única. Debe haber una sección para cada una de las metodologías desarrolladas, dándole entidad y explicandolas correctamente, con todo lujo de detalles. -->

<!-- La sección 5.1, de forma similar a la 4.1 tiene que mejorar. De nuevo, el objetivo debe ser que al leer esa sección entiendas aproximadamente de que van todos los experimentos. Por lo tanto hay que añadir descripción y highlights de cada uno. Los detalles luego. -->

### Capítulo 2 - Contexto

<!-- Intentaría mejorar el contexto de registro, cubriendo bien todas sus tipologías -->
<!-- 
Intentaría mejorar el estado del arte, para cubrir métodos basados en optimización directa de similitud de imagen (IBR), y métodos basados en matching de caracteristicas (FBR), identificando sus partes.

Luego, revisaría los  métodos deep learning que substituyen módulos de IBR (similitud, optimizador, y sí, el modelo de transformación en sí, como IDIR), y  metodos deep learning que substituyen módulos de FBR (feature detector, feature descriptor, matching), y métodos deep learning de regresión directa o inferencia amortizada. Debe discutirse donde se encuadra el trabajo realizado en relación a estos médodos. El objetivo del estado del arte no es revisar todo, ni en detalle, sino simplificar "lo que hay", para que se entienda "donde encaja" tu trabajo. -->

<!-- Incorporaría la revisión de métodos aplicados a retina al estado del arte, y en términos de los conceptos introducidos para le contexto general. La idea identificar trabajos que han aplicado las ideas generales del punto anterior, sin entrar en pormenores. La idea es evidenciar que IDIR o similares no han sido aplicados, y que ahí es donde se enfoca este trabajo. -->

<!-- La sección IDIR, iría a trabajo realizado. Es parte del trabajo entender y adaptar el método base, por lo que debe ir allí. En este capítulo de contexto solo se debe introducir conceptualmente "para que se entienda". Los detalles técnicos van donde hacen falta y tienen sentido, que es en trabajo realizado -->

<!-- El capítulo debe cerrar con una buena sección de trabajo realizado, a modo de conclusión. Donde, de forma simplificada, se haga referencia a lo discutido anteriormente de manera general, ya que justifica proponer lo que se propone hacer. También se debe profundizar y hacer énfasis en todas las aportaciones realizadas, poniendolas en contexto. -->

### Capítulo 3 - Metodología y planificación

<!-- Falta identificar los conjuntos de datos públicos como rescursos -->
<!-- Incluiría un estimador de esfuerzo en las tareas y  -->
<!-- un diagrama de Gantt -->
<!-- Falta realizar estimación de costes planificados -->

<!-- Haría una sección de seguimiento de la planificación, y estimación de coste real, a modo de conclusión del capítulo. -->

### Capítulo 4 - Trabajo realizado

<!-- Este debe ser el capítulo más extenso de la memoria, junto con el de experimentos. De lo contrario, parecerá que el trabajo realizado son 5 páginas sin rellenar del todo. Hay espacio, así que hay que trabajar mucho más este capítulo. No te habíamos enviado comentarios antes con la esperanza de tener más material con el que trabajar (no podemos estar revisando memorias que están de forma evidente sin terminar, porque implicaría hacer 3 o cuatro iteraciones sobre cosas que, en el fondo, dependen completamente de ti). Lamentablemente este capítulo no ha avanzado nada. Evidentemente no está bien. ¿Refleja este capítulo todo lo que has hecho? -->

<!-- Estructura el trabajo realizado en varias partes, haciendo una buena introducción en el capítulo. Luego, haz una sección detallando cada una de las partes: Estudio de IDIR, Adaptación a 2D con retinas, replicación de resultados, diseño de experimentos y metodología de evaluación en retinas (incluyendo esquema general de entrenamiento, conjuntos de datos, y todo tipo de métricas de análisis en detalle). Es importante explicar bien todas las formas de presentar resultados que vas a usar y cómo se interpretan. Por último, secciones destinadas a describir metodologías de mejora desarrolladas por ti mismo (hay varias, como los métodos de muestreo etc.) -->

### Capítulo 5 - Experimentación y resultados

<!-- Igual que el capítulo 4, parece que no ha avanzado. -->
<!-- 
En la sección de vista general, debes describir los experimentos de forma simplificada, como te dijimos, motivando el por qué se hacen. -->

<!-- Eleva cada experimento a sección (no subsección colgando de experimentos), y organizalos en susbsecciones de resultados y discusión (no subsubsecciones). En general, lo que hay está escueto. -->

<!-- Hace falta una sección final de comparativa, que ponga de relieve las mejores solucione y destaque las aportaciones

Una sección resumen con las principales observaciones derivadas de las discusiones previas. -->

### Comentarios generales:
<!-- 
Referencias cruzadas a figuras. En general, las figuras flotantes (y tablas) deben dejarse libres sin forzar a (ni pretender) que se coloquen en una posición concreta. Luego, en el texto, se deben citar siempre, donde sean relevantes. Por ejemplo: "Como se puede ver en la figura \ref{fig:***}" sería correcto, mientras que "Como se puede observar en la siguiente figura: " no sería correcto (ya que asume que la figura tiene que estar ahí. La figura siempre debe estar definida después de su primera cita. Fíjate también que en las citas a figuras, tablas, ecuaciones, etc. debes escribir "la figura \ref", "la tabla \ref", "la ecuación \ref", y no simplemente \ref.

Citas a bibliografía, siempre dentro de la frase, antes del punto. -->
