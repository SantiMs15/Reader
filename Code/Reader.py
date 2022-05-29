import pyttsx3
import PyPDF2
libro = open('pnl_cast.pdf','rb')
PdfReader = PyPDF2.PdfFileReader(libro)
paginas = PdfReader.numPages
print(paginas)
speaker = pyttsx3.init()
speaker.say('Haciendo tarea en la casa desde hace 3 días')
speaker.runAndWait()
