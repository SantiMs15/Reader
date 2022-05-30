import pyttsx3
import PyPDF2

#Infantil
a=input("Escriba el genero del libro que desea escuchar: ")
if a=="infantil":
    libro = open('D:\Proyectos\Reader\libros\Caperucita.pdf','rb')
    PdfReader = PyPDF2.PdfFileReader(libro)
    paginas = PdfReader.numPages
    print(f'Estas escuchando Caperucita Roja. Nro de páginas: {paginas}')
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
    print(f'Estas escuchando La leyenda de la llorona. Nro de páginas: {paginas}')
    speaker = pyttsx3.init()
    for paginas in range(0, paginas):
        page = PdfReader.getPage(0)
        text = page.extract_text()
        speaker.say(text)
        speaker.runAndWait()

#Terror
if a=="terror":
    libro=open('D:\Proyectos\Reader\libros\it-eso.pdf','rb')
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
if a=="fantasia":
    libro=open('D:\Proyectos\Reader\libros\Percy_Jackson_rayo.pdf','rb')
    PdfReader=PyPDF2.PdfFileReader(libro)
    paginas=PdfReader.numPages
    print(f'Estas escuchando Percy Jackson el Ladron del rayo de Rick Riordan. Nro de páginas:{paginas}')
    speaker=pyttsx3.init()
    for paginas in range (2, paginas):
        page=PdfReader.getPage(2)
        text=page.extract_text()
        speaker.say(text)
        speaker.runAndWait()

#Drama
if a=="drama":
    libro=open('D:\Proyectos\Reader\libros\gray.pdf','rb')
    PdfReader=PyPDF2.PdfFileReader(libro)
    paginas=PdfReader.numPages
    print(f'Estas escuchando El retrato de Dorian Gray de Oscar Wilde. Nro de páginas:{paginas}')
    speaker=pyttsx3.init()
    for paginas in range (4, paginas):
        text=page.extract_text()
        speaker.say(text)
        speaker.runAndWait()

#Romance
if a=="romance":
    libro=open('D:\Proyectos\Reader\libros\Orgullo_P.pdf','rb')
    PdfReader=PyPDF2.PdfFileReader(libro)
    paginas=PdfReader.numPages
    print(f'Estas escuchando Orgullo y Prejuicio de Jane Austen. Nro de páginas:{paginas}')
    speaker=pyttsx3.init()
    for paginas in range (0, paginas):
        page=PdfReader.getPage(0)
        text=page.extract_text()
        speaker.say(text)
        speaker.runAndWait()

#Ciencia ficcion
if a=="scifi":
    libro=open('D:\Proyectos\Reader\libros\mancerneuro.pdf','rb')
    PdfReader=PyPDF2.PdfFileReader(libro)
    paginas=PdfReader.numPages
    print(f'Estas escuchando Neuromante de William Gibson. Nro de páginas:{paginas}')
    speaker=pyttsx3.init()
    for paginas in range (4, paginas):
        page=PdfReader.getPage(4)
        text=page.extract_text()
        speaker.say(text)
        speaker.runAndWait()