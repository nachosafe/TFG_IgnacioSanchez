# Preguntas de Traumatología - Chatbot

Este proyecto es un chatbot web desarrollado en Python para responder preguntas frecuentes de pacientes en un hospital de traumatología. El sistema utiliza técnicas de procesamiento de lenguaje natural (NLP) para comparar las preguntas de los pacientes con un archivo de texto que contiene preguntas y respuestas predefinidas.

## Características

- **Procesamiento de Lenguaje Natural**: Usa spaCy y TF-IDF para procesar y comparar preguntas de los usuarios con las preguntas y respuestas almacenadas en un archivo de texto.
- **Interfaz Web Interactiva**: La aplicación tiene un front-end amigable que permite a los usuarios interactuar con el chatbot y recibir respuestas de manera dinámica.
- **Funcionalidad de Traductor**: Soporte para traducir preguntas en inglés al español antes de procesarlas.
- **Manejo de Sesiones**: Solo los usuarios autenticados pueden acceder a la página principal y utilizar el chatbot.

## Estructura del Proyecto

- `preguntasTraumatologia.py`: Código principal que contiene la lógica para el procesamiento de preguntas y respuestas usando técnicas de NLP.
- `templates/`: Carpeta que contiene las plantillas HTML (`index.html`, `login.html`) para la interfaz de usuario.
- `static/`: Carpeta que contiene archivos estáticos como estilos CSS e imágenes.
  - `style.css`: Archivo de estilo que define la apariencia de la aplicación web.
  - `doctor-avatar.png`: Imagen del avatar del médico que aparece junto a los mensajes del chatbot.
- `preguntas.txt`: Archivo de texto que contiene preguntas y respuestas predefinidas en formato plano.

## Instalación

1. **Clonar el repositorio**:
    ```bash
    git clone https://github.com/usuario/preguntas-traumatologia.git
    cd preguntas-traumatologia
    ```

2. **Crear un entorno virtual**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa: venv\Scripts\activate
    ```

3. **Instalar dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Ejecutar la aplicación**:
    ```bash
    python app.py
    ```

5. **Abrir en el navegador**:
    - Accede a `http://localhost:5000` para ver la aplicación en acción.

## Uso

1. **Iniciar Sesión**: Los usuarios deben iniciar sesión con su código para acceder al chatbot.
2. **Interacción con el Chatbot**: Escribe una pregunta en el cuadro de texto y presiona "Enviar". El chatbot responderá basado en la pregunta más similar almacenada en el archivo `preguntas.txt`.
3. **Retroalimentación**: Después de recibir una respuesta, puedes indicar si la respuesta fue útil o no.

## Personalización

### Añadir Nuevas Preguntas y Respuestas

Para añadir nuevas preguntas y respuestas, simplemente edita el archivo `preguntas.txt` y sigue el formato de pregunta-respuesta:

¿Pregunta 1?
Respuesta 1
¿Pregunta 2?
Respuesta 2


### Modificar la Apariencia

Puedes ajustar la apariencia de la aplicación editando el archivo `style.css` en la carpeta `static`.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue los pasos a continuación:

1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza los cambios necesarios y haz commit (`git commit -m 'Añadir nueva característica'`).
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.


