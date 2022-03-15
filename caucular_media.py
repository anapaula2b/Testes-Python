notas =[]
def caucularMedia(notas):
    media = (sum(notas))/2
    print(media)
    
nota = 0

for n in range(2):
    nota = int(input('Adicione uma nota '))
    notas.append(nota)
    
caucularMedia(notas)
    


