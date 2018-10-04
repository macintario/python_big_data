import nltk as nl

#dnl.download()

texto= "Hola gran mundo bueno!!!"

print(texto.split())
bg = nl.ngrams(texto,4)
for x in bg:
    print(x)