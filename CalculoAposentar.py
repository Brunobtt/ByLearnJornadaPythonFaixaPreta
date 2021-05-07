# Codigo do Bin para identificar tempo restante para se aposentar

#funcao para calcular o tempo restante se for mulher
def se_mulher(idade_mulher): 
  mulher_idade_minina = 62
  restante = mulher_idade_minina - idade_mulher
  mostrar_tempo(restante)

#funcao para calcular o tempo restante se for homem
def se_homem(idade_homem): 
  homem_idade_minima = 65
  restante = homem_idade_minima - idade_homem
  mostrar_tempo(restante)

#funcao para mostrar o tempo restante  
def mostrar_tempo(resta): 
  print('Ainda faltam', resta, 'anos para voce se aposentar!')

print ('Ola, vamos descobrir quanto tempo ainda falta para voce se aposentar, para isso precisamos de algumas informacoes:')

#Coletando idade da pessoa
idade = int(input('Sua idade:')) 
sexo = str(input('Agora nos infome seu sexo, se for homem responda "H", se for mulher responda "M":')) #Coletando sexo da pessoa

#Se for mulher chama a funcao se_mulher, Se for homem chama a funcao se_homem
if sexo == 'M': 
  se_mulher(idade) 
else: 
  se_homem(idade) 
