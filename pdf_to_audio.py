# pdf to audio book converter
import pyttsx3
import PyPDF2
file =open("climat.pdf",mode="rb")
pdf_reader=PyPDF2.PdfReader(file)
pages=len(pdf_reader.pages)
print(pages)
melo=pyttsx3.init()
page=pdf_reader.pages[9]
text=page.extract_text()
rate=melo.getProperty('rate')
melo.setProperty('rate',150)
melo.say(text)
melo.runAndWait()
