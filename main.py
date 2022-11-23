#meu primeiro projeto python!!
#

#print() = comando de saida
print("alo mundo")
# quando quiser guardar uma string (frase)
nome = "marcela"
#quando quiser guardar um numero inteiro
idade = 23
#exibir o meu nome (que esta dentro da variável nome)
print(nome)

#quando quiser exibir a frase "minha idade é"complementado com o conteúdo da variável idade
#print ("meu nome é " +nome)
print("minha idade é:" + str(idade))
print(f"minha idade é: {idade}")
print("minha idade é: {}".format(idade))

#quando quiser exibir "meu nome é... e tenho ...anos..." trocando pelas variáveis nome e idade
print("meu nome é {} e tenho {} anos".format(nome, idade))

print("alo mundo")


#comando de saída..exibir na tela

print (f"Boa noite, seu nome é {nome}")
#exiba "Sua idade é ..."
print("Sua idade é {}".format(idade))

#e se eu quisesse mostrar o DOBRO da idade informada?
dobro = idade*2
print("O dobro da idade informada é {}".format(dobro))

#Estrutura condicional - o famoso "SE" (if)
#Se a pessoa for maior de idade, mostre "Você é maior de idade, ótimo! Já pode beber ou dirigir"
if idade >= 18:
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir")
else:
  print("Você é xóven ainda, xóven ainda...")

#E se eu quisessem perguntar o gênero (M = Masculino e F = Feminino)
#Mostre (...e você também precisa/precisou prestar o serviço militar obrigatório)
genero = input("Informe o gênero M=Masculino, F=Feminino, O=Outros: ")
if idade >= 18 and genero == "M":
  print(
    "... e você também precisa/precisou prestar o serviço militar obrigatório")

print("vai ser executada de qualquer jeito")
