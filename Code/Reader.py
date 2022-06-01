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
    libro=open('D:\Proyectos\Reader\libros\HG.pdf','rb')
    PdfReader=PyPDF2.PdfFileReader(libro)
    paginas=PdfReader.numPages
    print(f'Estas escuchando Hansel y Gretel de los Hermanos Grimm. Nro de páginas:{paginas}')
    speaker=pyttsx3.init()
    for paginas in range (3, paginas):
        page=PdfReader.getPage(3)
        text=page.extract_text()
        speaker.say(text)
        speaker.runAndWait()

#Drama
if a=="drama":
    libro=open('D:\Proyectos\Reader\libros\Divina.pdf','rb')
    PdfReader=PyPDF2.PdfFileReader(libro)
    paginas=PdfReader.numPages
    print(f'Estas escuchando La Divina Comedia de Dante Aligheri. Nro de páginas:{paginas}')
    speaker=pyttsx3.init()
    for paginas in range (0, paginas):
        page=PdfReader.getPage(0)
        text=page.extract_text()
        speaker.say(text)
        speaker.runAndWait()

#Romance
if a=="romance":
    libro=open('D:\Proyectos\Reader\libros\LBB.pdf','rb')
    PdfReader=PyPDF2.PdfFileReader(libro)
    paginas=PdfReader.numPages
    print(f'Estas escuchando La Bella y la Bestia de Jeanne Marie Leprince De Beaumont. Nro de páginas:{paginas}')
    speaker=pyttsx3.init()
    for paginas in range (3, paginas):
        page=PdfReader.getPage(3)
        text=page.extract_text()
        speaker.say(text)
        speaker.runAndWait()

#Ciencia ficcion
if a=="historia":
    libro=open('D:\Proyectos\Reader\libros\Guerra.pdf','rb')
    PdfReader=PyPDF2.PdfFileReader(libro)
    paginas=PdfReader.numPages
    print(f'Estas escuchando Neuromante de William Gibson. Nro de páginas:{paginas}')
    speaker=pyttsx3.init()
    for paginas in range (3, paginas):
        page=PdfReader.getPage(3)
        text=page.extract_text()
        speaker.say(text)
        speaker.runAndWait()