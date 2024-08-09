Preguntas de Traumatología - Chatbot
Este proyecto es un chatbot web desarrollado en Python para responder preguntas frecuentes de pacientes en un hospital de traumatología. El sistema utiliza técnicas de procesamiento de lenguaje natural (NLP) para comparar las preguntas de los pacientes con un archivo de texto que contiene preguntas y respuestas predefinidas.

Características
Procesamiento de Lenguaje Natural: Usa spaCy y TF-IDF para procesar y comparar preguntas de los usuarios con las preguntas y respuestas almacenadas en un archivo de texto.
Interfaz Web Interactiva: La aplicación tiene un front-end amigable que permite a los usuarios interactuar con el chatbot y recibir respuestas de manera dinámica.
Funcionalidad de Traductor: Soporte para traducir preguntas en inglés al español antes de procesarlas.
Manejo de Sesiones: Solo los usuarios autenticados pueden acceder a la página principal y utilizar el chatbot.
Estructura del Proyecto
preguntasTraumatologia.py: Código principal que contiene la lógica para el procesamiento de preguntas y respuestas usando técnicas de NLP.
templates/: Carpeta que contiene las plantillas HTML (index.html, login.html) para la interfaz de usuario.
static/: Carpeta que contiene archivos estáticos como estilos CSS e imágenes.
style.css: Archivo de estilo que define la apariencia de la aplicación web.
doctor-avatar.png: Imagen del avatar del médico que aparece junto a los mensajes del chatbot.
preguntas.txt: Archivo de texto que contiene preguntas y respuestas predefinidas en formato plano.
Instalación
Clonar el repositorio:

bash
Copiar código
git clone https://github.com/usuario/preguntas-traumatologia.git
cd preguntas-traumatologia
Crear un entorno virtual:

bash
Copiar código
python -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate
Instalar dependencias:

bash
Copiar código
pip install -r requirements.txt
Ejecutar la aplicación:

bash
Copiar código
python app.py
Abrir en el navegador:

Accede a http://localhost:5000 para ver la aplicación en acción.
Uso
Iniciar Sesión: Los usuarios deben iniciar sesión con su código para acceder al chatbot.
Interacción con el Chatbot: Escribe una pregunta en el cuadro de texto y presiona "Enviar". El chatbot responderá basado en la pregunta más similar almacenada en el archivo preguntas.txt.
Retroalimentación: Después de recibir una respuesta, puedes indicar si la respuesta fue útil o no.
Personalización
Añadir Nuevas Preguntas y Respuestas
Para añadir nuevas preguntas y respuestas, simplemente edita el archivo preguntas.txt y sigue el formato de pregunta-respuesta:

Copiar código
¿Pregunta 1?
Respuesta 1
¿Pregunta 2?
Respuesta 2
Modificar la Apariencia
Puedes ajustar la apariencia de la aplicación editando el archivo style.css en la carpeta static.

Contribuciones
Las contribuciones son bienvenidas. Por favor, sigue los pasos a continuación:

Haz un fork del proyecto.
Crea una nueva rama (git checkout -b feature/nueva-caracteristica).
Realiza los cambios necesarios y haz commit (git commit -m 'Añadir nueva característica').
Haz push a la rama (git push origin feature/nueva-caracteristica).
Abre un Pull Request.
