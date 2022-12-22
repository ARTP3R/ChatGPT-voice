import speech_recognition as sr
import pyttsx3

# Inicializar el motor de voz
engine = pyttsx3.init()

# Configurar la velocidad y el tono de la voz
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

# Inicializar el reconocedor de voz
r = sr.Recognizer()

while True:
  # Escuchar la pregunta del usuario
  with sr.Microphone() as source:
      print('Hable ahora:')
      audio = r.listen(source)

  # Intentar reconocer el texto de la pregunta
  try:
      question = r.recognize_google(audio, language='es-ES')
      print(f'Pregunta: {question}')

      # Hacer la pregunta al Assistant
      answer = assistant.ask(question)
      print(f'Respuesta: {answer}')

      # Reproducir la respuesta fonéticamente
      engine.say(answer)
      engine.runAndWait()

  except Exception as e:
      print(e)
      print('Lo siento, no pude entender lo que dijiste. Por favor, vuelve a intentarlo.')
