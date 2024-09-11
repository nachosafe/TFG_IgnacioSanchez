from googletrans import Translator
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy

# Cargar el modelo de spaCy para el procesamiento de lenguaje natural en español
nlp = spacy.load("es_core_news_sm")
translator = Translator()

# Función para traducir preguntas de inglés a español
def translate_to_spanish(text):
    translated = translator.translate(text, src="en", dest="es")
    return translated.text

# Lee el contenido del archivo "preguntas.txt" y extrae las preguntas y respuestas
with open("preguntas.txt", "r", encoding="utf-8") as file:
    texto_preguntas = file.read()
    preguntas = [text.split('¿')[1].strip() for text in texto_preguntas.split('?') if '¿' in text]
    respuestas = [text.split('?')[1].strip() for text in texto_preguntas.split('¿') if '?' in text]

# Combinar preguntas y respuestas en un solo conjunto para comparación
combinado = [pregunta + " " + respuesta for pregunta, respuesta in zip(preguntas, respuestas)]

# Inicializa el lematizador de spaCy
def lemmatize_text(text):
    doc = nlp(text)
    return " ".join([token.lemma_.lower() for token in doc])

# Inicializa el vectorizador TF-IDF
vectorizer = TfidfVectorizer(tokenizer=word_tokenize, preprocessor=lemmatize_text, lowercase=False)
tfidf_matrix_general = vectorizer.fit_transform(combinado)

# Función para calcular la similitud entre la pregunta del usuario y las preguntas/respuestas generales
def buscar_respuestas(pregunta_usuario):
    pregunta_usuario_es = translate_to_spanish(pregunta_usuario)
    tfidf_matrix_usuario = vectorizer.transform([pregunta_usuario_es])
    similarity_scores = cosine_similarity(tfidf_matrix_usuario, tfidf_matrix_general)
    sorted_indices = similarity_scores.argsort(axis=1)[:, ::-1]

    respuestas_usuario = []
    for index in sorted_indices[0][:1]:
        respuestas_usuario.append({
            "pregunta": preguntas[index],
            "respuesta": respuestas[index]
        })



    return respuestas_usuario
