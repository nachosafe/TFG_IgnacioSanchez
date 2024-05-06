from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy

# Cargar el modelo de spaCy para el procesamiento de lenguaje natural en español
nlp = spacy.load("es_core_news_sm")

# Lee el contenido del archivo "preguntas.txt" y extrae solo las partes entre '¿' y '?'
with open("preguntas.txt", "r", encoding="utf-8") as file:
    texto_preguntas = file.read()
    preguntas = [text.split('¿')[1].strip() for text in texto_preguntas.split('?') if '¿' in text]
    respuestas = [text.split('?')[1].strip() for text in texto_preguntas.split('¿') if '?' in text]

# Inicializa el lematizador de spaCy
def lemmatize_text(text):
    doc = nlp(text)
    return " ".join([token.lemma_.lower() for token in doc])

# Inicializa el vectorizador TF-IDF
vectorizer = TfidfVectorizer(tokenizer=word_tokenize, preprocessor=lemmatize_text, lowercase=False)
tfidf_matrix_general = vectorizer.fit_transform(preguntas)

# Función para calcular la similitud entre la pregunta del usuario y las preguntas generales
def buscar_respuestas(pregunta_usuario):
    tfidf_matrix_usuario = vectorizer.transform([pregunta_usuario])
    similarity_scores = cosine_similarity(tfidf_matrix_usuario, tfidf_matrix_general)
    sorted_indices = similarity_scores.argsort(axis=1)[:, ::-1]

    # Inicializar una lista para almacenar las respuestas
    respuestas_usuario = []

    # Agregar las respuestas más similares a la lista
    for index in sorted_indices[0][:3]:
        respuestas_usuario.append({
            "pregunta": preguntas[index],
            "respuesta": respuestas[index]
        })

    return respuestas_usuario