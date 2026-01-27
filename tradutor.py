pt = ["bom dia", "boa tarde", "boa noite", "Olá"]
ig = ["good morning", "good afternoon", "good night", "Hello"]

#vetor pra olhar as palavras
while True:
 #pede pro usuario digitar 
 T = input("Digite a palavra: ")

 if T in pt: 
  #vai comparando com oq foi digitado e printa
  indice = pt.index(T)
  print(f"\n Tradução: {ig[indice]}")
 else:
  print("Palavra não registrada")
