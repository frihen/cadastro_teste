# CÓDIGO PARA CADASTRO(arquivo teste para manipulação de dados com pandas)
import pandas as pd
import os

#FUNÇÃO CRIADA PARA CASO O VALOR INTEIRO SEJA DADO COMO NULO
def teste_numeros(numero, texto='Alguma pergunta'):
    while True:
        try:
            numero = int(input(texto))
        except:
            pass
        if numero != 0:    
            return numero

#DICIONARIO DE COLUNAS NECESSÁRIAS NA TABELA
dicionario = {
        'NOME':[],
        'IDADE':[],
        'ESCOLARIDADE':[],
        'SITUAÇÃO': [],
        'CIDADE':[],
        'ESTADO':[],
        'ESTADO CIVIL':[],
    }

#OPÇOES DE ESCOLARIDADE
escolaridades = ['Ensino Fundamental', 'Ensino Médio', 'Ensino Superior','Mestrado','Doutorado']
situacoes = ['Incompleto','Cursando','Completo']

#ENQUANTO O WHILE ESTIVER TRUE VAI RODAR O CODIGO
while True:
    print('CADASTRO UNICO, PARA TESTES COM MANIPULAÇÕES DE DADOS.')
    
#INICIO DO QUESTIONARIO PARA CADASTRO
    nome = input('Insira seu nome completo:\n\nR= ').upper()
    

    idade = 0
    idade = teste_numeros(idade, '\nInsira sua idade: (Somente números)\n\nR= ')
    

    print("""\nQual sua escolaridade? (1 - Ensino Fundamental, 2 - Ensino Médio,
3 - Ensino Superior, 4 - Mestrado, 5 - Doutorado) Escolha o número: """)
    esc = 0
    esc_escolaridade = teste_numeros(esc, '\nR= ')
    esc = escolaridades[esc_escolaridade-1]
    
    
    print("""\nQual a situação da sua escolaridade?(1 - Incompleto,
2 - Cursando, 3 - Completo) Escolha o número:""")
    sit = 0
    site = teste_numeros(sit,'\nR= ')
    sit = situacoes[site-1]


    cidade = input('\nInsira sua cidade natal:\n\nR= ').capitalize()
    estado = input('\nSigla do estado:\n\nR= ').upper()
    

    est_civ = input('\nQual seu estado civil atualmente?\n\nR= ').capitalize()


    dicionario['NOME'].append(nome)
    dicionario['IDADE'].append(idade)
    dicionario['ESCOLARIDADE'].append(esc)
    dicionario['SITUAÇÃO'].append(sit)
    dicionario['CIDADE'].append(cidade)
    dicionario['ESTADO'].append(estado)
    dicionario['ESTADO CIVIL'].append(est_civ)
    
    #FINAL DO CADASTRO
    df = pd.DataFrame(data=dicionario,index=list(range(1, 1+len(dicionario['NOME']))),columns=dicionario.keys())
    print('\n','CADASTRADO COM SUCESSO','\n')
    
    #CONDIÇÃO DE FINALIZAÇÃO DA LISTA
    print('Ainda deseja fazer algum cadastro nesta lista?')
    cond_while = input('S ou N?\n\nR= ').upper()
    
    #LIMPAR O TERMINAL APÓS USO.
    if cond_while[0] == 'N':
        os.system('cls') or None
        break
    else:
        os.system('cls') or None
        

salvar_arquivo = input('\nDeseja transformar esses dados em um arquivo csv?\nS ou N?\n\nR= ').capitalize()

#Caso escolha sim, o arquivo criará uma tabela em csv para analise.
if salvar_arquivo[0]=='S':
    nome_arquivo = input("\nQual nome você quer para seu arquivo?(Não é necessário colocar .csv no final)\n\nR= ")
    df.to_csv(f'{nome_arquivo}.csv',index=False)

print('\n',df)

