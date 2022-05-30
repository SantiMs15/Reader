import pyttsx3
import PyPDF2

#Infantil
a=input("Escriba el genero del libro que desea escuchar: ")
if a=="infantil":
    libro = open('D:\Proyectos\Reader\libros\Caperucita.pdf','rb')
    PdfReader = PyPDF2.PdfFileReader(libro)
    paginas = PdfReader.numPages
    print(f'Estas escuchando Caperucita Roja. Nro de paginas: {paginas}')
    speaker = pyttsx3.init()
    for paginas in range(2, paginas):
        page = PdfReader.getPage(2)
        text = page.extract_text()
        speaker.say(text)
        speaker.runAndWait()

#Novela
if a=="leyenda":
    libro = open('D:\Proyectos\Reader\libros\la_llorona.pdf','rb')
    PdfReader = PyPDF2.PdfFileReader(libro)
    paginas = PdfReader.numPages
    print(f'Estas escuchando La leyenda de la llorona. Nro de paginas: {paginas}')
    speaker = pyttsx3.init()
    for paginas in range(0, paginas):
        page = PdfReader.getPage(0)
        text = page.extract_text()
        speaker.say(text)
        speaker.runAndWait()

#Terror
if a=="terror":
    libro=open('C:\Reader project\Reader\libros\it-eso','rb')
    PdfReader=PyPDF2.PdfFileReader(libro)
    paginas=PdfReader.numPages
    print(f'Estas escuchanda It el payaso de Stephen King. Nro de paginas:{paginas}')
    speaker=pyttsx3.init()
    for paginas in range (0, paginas):
        page=PdfReader.getPage(0)
        text=page.extract_text()
        speaker.say(text)
        speaker.runAndWait()

#Fantasia
    libro=open()
    PdfReader=PyPDF2.PdfFileReader(libro)
    paginas=PdfReader.numPages
    print(f'Estas escuchando Percy Jackson el Ladron del rayo de Rick Riordan. Nro de paginas:{paginas}')
    speaker=pyttsx3.init()
    for paginas in range (0, paginas):
        page=PdfReader.getPage(0)
        text=page.extract_text()
        speaker.say(text)
        speaker.runAndWait()

#Drama
    libro=open()
    PdfReader=PyPDF2.PdfFileReader(libro)
    paginas=PdfReader.numPages
    print(f'Estas escuchando El retrato de Dorian Gray de Oscar Wilde:{paginas}')
    speaker=pyttsx3.init()
    for paginas in range (0, paginas):
        page=PdfReader.getPage(0)
        text=page.extract_text()
        speaker.say(text)
        speaker.runAndWait()

#Romance