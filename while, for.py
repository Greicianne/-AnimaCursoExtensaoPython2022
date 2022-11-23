print("aula 03")
contador = 1

#exibir um numero repetidamente
while(contador <= 10):
  print(contador)
  contador = contador+1 #contador += 1


#laço for (python for = for each)
fruta = "morango"
print(fruta)

fruta1 = "morango"
fruta2 = "laranja"
fruta3 = "pêra"

#lista 
frutas = ["morango", "laranja", "pêra"]
#mostrar todas
print(frutas)

#exibir apenas a 3a. fruta (uva)
print(frutas[2])

#exibir quantas frutas tem na minha lista?

print(len(frutas)) #length = tamanho

#quero incluir uma fruta nova
frutas.append("manga")

print(len(frutas)) #length = tamanho
print(frutas)

print(frutas[0]) 
print(frutas[1]) 
print(frutas[2]) 
print(frutas[3]) 
#print(frutas[4])

print("Exemplo das frutas com while..")

frutas.append("uva")

i=0 #(i de index)
while(i<len(frutas)):
  print(frutas[i])
  i = i + 1

print("Exemplo das frutas com o FOR")
for fruta in frutas:
  print(fruta)

#criaçoes de funçoes
preco = 1999.90
#calcular 5% de imposto, guardar na variavel imposto e exibir na tela
imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

#Criar uma funçao calcular_imposto() que calcula um imposto de 5% e retorna a quem pediu...

#Isto é a declaracao da funcao
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.07
  return imposto

#aqui é o uso... imposto a calcular.. e exibir na tela
preco = 299
imposto = calcular_imposto(preco)
print(f"esse aqui é com a funcao (7%) {imposto}")

#explicacao da variavel local x global
print(preco) #???
preco_produto =100
print(preco_produto) #??

#Agora calcular imposto a alíquota agora é 7%
valores = [1.99, 24.50, 78.27, 1515.5]
#Se eu quiser calcular o imposto destes quatro valores... e exbir na tela assim: "O imposto de... é..." (1o. preç, 2o. imposto)
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto(valor)}")
#Declarar uma fanção calcular_imposto_alíquotaque recebe dois parâmetros: o preço do produto e a alíquota de imposto a ser aplicada e retorna o imposto calculado. Se a alíquota nao for informada, utilize 7% como padrao.
def calcular_imposto_aliquota(valor, aliquota=7):
  imposto = valor * aliquota / 100
  return imposto

for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor)}")

for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 7)}")

#E se agora o imposto for 10%?
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 10)}")

