import pyttsx3
import requests
from bs4 import BeautifulSoup

# Obtener el texto del sitio web
url = 'https://www.ejemplo.com/texto-web'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
text = soup.get_text()

# Inicializar el motor de voz
engine = pyttsx3.init()

# Configurar la velocidad y el tono de la voz
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

# Reproducir el texto fonéticamente
engine.say(text)
engine.runAndWait()
