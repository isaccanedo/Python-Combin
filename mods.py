from random import shuffle
import pickle

APOSTAS = []

'''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'''
''' Recebe 15 valores informados manualmente, salvando-os como uma aposta.              '''
'''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'''


def informar_valores_manualmente():
    
    manual = []
    
    wh = 0
    while wh != 15:
        
        print('')
        print('  > Informe um Valor Desejado:')
        print('')
        xf = int(input('  > '))
        print('')
        print('  |----------------------------------------------------------|')
 
        if xf < 1:
                    
            print('')
            print('  |||||||||||||||||||||||||||||||||||||')
            print('  ERRO: VALOR INFORMADO É INFERIOR A 01')
            print('  |||||||||||||||||||||||||||||||||||||')
            print('')
            print('  |----------------------------------------------------------|')
                    
        elif xf > 25:
                    
            print('')
            print('  |||||||||||||||||||||||||||||||||||||')
            print('  ERRO: VALOR INFORMADO É SUPERIOR A 25')
            print('  |||||||||||||||||||||||||||||||||||||')
            print('')
            print('  |----------------------------------------------------------|')
                        
        else:
                
            co = manual.count(xf)
                    
            if co == 0:
                        
                wh = wh + 1
                    
                manual.append(xf)
                list.sort(manual)
                
                print('')
                print('  VALOR INSERIDO COM SUCESSO | SUA APOSTA:')
                print('')
                print(' ', manual)
                print('')
                print('  |----------------------------------------------------------|')
            
            else:
                        
                print('')
                print('  |||||||||||||||||||||||||||||||||||||')
                print('  ERRO: VALOR INFORMADO JÁ FOI INSERIDO')
                print('  |||||||||||||||||||||||||||||||||||||')
                print('')
                print('  |----------------------------------------------------------|')

    list.sort(manual)
    APOSTAS.append(manual)              


'''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'''
''' Cria 15 valores gerados aleatoriamente, salvando-os como uma aposta, (B: random).   '''
'''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'''


def gerar_valores_aleatoriamente():
    
    random = []
    
    for i in range(25):
        
        i = i + 1
        
        random.append(i)
    
    for i in range(2):
    
        shuffle(random)
    
    for i in range(10):
        
        del random[0]
        
    list.sort(random)
    APOSTAS.append(random)
    
    print('')
    print('  APOSTA GERADA COM SUCESSO | SUA APOSTA:')
    print('')
    print(' ', random)
    print('')
    print('  |----------------------------------------------------------|')


'''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'''
''' Elimina uma aposta salva escolhida manualmente.                                     '''
'''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'''


def eliminar_aposta():
    
    le = len(APOSTAS)
    
    print('')
    print('  > Informe o Número da Aposta a Ser Eliminada:')
    print('')
    xf = int(input('  > '))
    print('')
    print('  |----------------------------------------------------------|')
                
    if xf < 1:
                    
        print('')
        print('  |||||||||||||||||||||||||||||||||||||')
        print('  ERRO: VALOR INFORMADO É INFERIOR A 01')
        print('  |||||||||||||||||||||||||||||||||||||')
        print('')
        print('  |----------------------------------------------------------|')
                    
    elif xf > le:
                    
        print('')
        print('  |||||||||||||||||||||||||||||||||||||')
        print('  ERRO: VALOR INFORMADO É SUPERIOR A', le)
        print('  |||||||||||||||||||||||||||||||||||||')
        print('')
        print('  |----------------------------------------------------------|')
                    
    else:
                    
        el = xf - 1
                    
        print('')
        print('  APOSTA ESCOLHIDA COM SUCESSO | APOSTA ELIMINADA:')
        print('')
        print(' ', APOSTAS[el])
        print('')
        print('  |----------------------------------------------------------|')
        
        del APOSTAS[el]


'''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'''
''' Elimina todas as apostas salvas.                                                    '''
'''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'''


def eliminar_todas_as_apostas():
    
    le = len(APOSTAS)

    for i in range(le):
                    
        del APOSTAS[0]
                
    print('')
    print('  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('  APOSTAS ELIMINADAS COM SUCESSO')
    print('  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('')
    print('  |----------------------------------------------------------|')


'''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'''
''' Imprime todas as apostas salvas.                                                    '''
'''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'''


def imprimir_lista_de_apostas():
    
    le = len(APOSTAS)
    
    for i in range(le):
                    
        print('')
        print('  APOSTA NÚMERO:', i + 1)
        print('')
        print(' ', APOSTAS[i])
        print('')
        print('  |----------------------------------------------------------|')


'''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'''
''' Recebe 15 valores informados manualmente, salvando-os como um resultado.            '''
'''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'''


def informar_resultado_manualmente():
    
    result = []
                
    wh = 0             
    while wh != 15:
                        
        print('')
        print('  > Informe um Valor do Resultado:')
        print('')
        xf = int(input('  > '))
        print('')
        print('  |----------------------------------------------------------|')
                        
        if xf < 1:
                            
            print('')
            print('  |||||||||||||||||||||||||||||||||||||')
            print('  ERRO: VALOR INFORMADO É INFERIOR A 01')
            print('  |||||||||||||||||||||||||||||||||||||')
            print('')
            print('  |----------------------------------------------------------|')
                            
        elif xf > 25:
                            
            print('')
            print('  |||||||||||||||||||||||||||||||||||||')
            print('  ERRO: VALOR INFORMADO É SUPERIOR A 25')
            print('  |||||||||||||||||||||||||||||||||||||')
            print('')
            print('  |----------------------------------------------------------|')
                                    
        else:
                            
            co = result.count(xf)
                    
            if co == 0:
                        
                wh = wh + 1
                    
                result.append(xf)
                list.sort(result)
                        
                print('')
                print('  VALOR INSERIDO COM SUCESSO | SEU RESULTADO:')
                print('')
                print(' ', result)
                print('')
                print('  |----------------------------------------------------------|')
            
            else:
                        
                print('')
                print('  |||||||||||||||||||||||||||||||||||||')
                print('  ERRO: VALOR INFORMADO JÁ FOI INSERIDO')
                print('  |||||||||||||||||||||||||||||||||||||')
                print('')
                print('  |----------------------------------------------------------|')

    return result


'''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'''
''' Cria 15 valores gerados aleatoriamente, salvando-os como um resultado, (B: random)  '''
'''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'''


def gerar_resultado_aleatoriamente():
    
    result = []

    for i in range(25):
                    
        i = i + 1
                        
        result.append(i)
    
    for i in range(2):
    
        shuffle(result)
                    
    for i in range(10):
                        
        del result[0]
                    
    list.sort(result)
                        
    print('')
    print('  RESULTADO GERADA COM SUCESSO | SEU RESULTADO:')
    print('')
    print(' ', result)
    print('')
    print('  |----------------------------------------------------------|')
    
    return result


'''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'''
''' Compara todas as apostas salvas com um resultado.                                   '''
'''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'''


def comparar_lista_de_apostas_com_resultado(result):
    
    le = len(APOSTAS)
     
    for i in range(le):
            
        ap = APOSTAS[i]
                
        ac = 0
                    
        for j in range(15):
                
            for k in range(15):
                    
                if ap[j] == result[k]:
                        
                    ac = ac + 1
                    
        nu = i + 1
        
        if ac == 13:
            
            pr = 20
            
        elif ac == 12:
            
            pr = 8
            
        elif ac == 11:
            
            pr = 4
            
        else:
            
            pr = 0
            
        if ac < 14:
        
            print('')
            print('  APOSTA NÚMERO:', nu, '| ACERTOS:', ac, '| PRÊMIO: R$', f'{pr:.2f}')
            print('')
            print(' ', ap)
            print('')
            print('  |----------------------------------------------------------|')
        
        else:
        
            print('')
            print('  APOSTA NÚMERO:', nu, '| ACERTOS:', ac, '| PRÊMIO: VERIFIQUE NO SITE')
            print('')
            print(' ', ap)
            print('')
            print('  |----------------------------------------------------------|')


'''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'''
''' Arquiva todas as apostas salvas, (B: pickle)                                        '''
'''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'''


def arquivar_apostas():
    
    try:
        
        with open('apostas.bin', 'wb') as arq:
            pickle.dump(APOSTAS, arq)
            
            print('')
            print('  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('  APOSTAS ARQUIVADAS COM SUCESSO')
            print('  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('')
            print('  |----------------------------------------------------------|')
    
    except Exception as e:
        
        print('')
        print('  |||||||||||||||||||||||||||||||||||||')
        print('  ERRO:', e)
        print('  |||||||||||||||||||||||||||||||||||||')
        print('')
        print('  |----------------------------------------------------------|')


'''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'''
''' Carrega todas as apostas arquivas, (B: pickle)                                      '''
'''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'''


def carregar_apostas():
    
    try:
        
        with open('apostas.bin', 'rb') as arq:
            global APOSTAS
            APOSTAS = pickle.load(arq)
            
            print('')
            print('  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('  APOSTAS CARREGADAS COM SUCESSO')
            print('  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('')
            print('  |----------------------------------------------------------|')

    except Exception as e:
        
        print('')
        print('  |||||||||||||||||||||||||||||||||||||')
        print('  ERRO:', e)
        print('  |||||||||||||||||||||||||||||||||||||')
        print('')
        print('  |----------------------------------------------------------|')


'''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'''
''' Confere o número de apostas salvas.                                                 '''
'''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'''


def teste_de_contagem():
    
    le = len(APOSTAS)
    
    return le


'''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'''
''' Printa uma mensagem informando que não há apostas salvas.                           '''
'''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'''


def teste_de_registro():
            
    print('')
    print('  |||||||||||||||||||||||||||||||||||||')
    print('  ERRO: NÃO EXISTEM APOSTAS REGISTRADAS')
    print('  |||||||||||||||||||||||||||||||||||||')
    print('')
    print('  |----------------------------------------------------------|')


'''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'''
''' Printa uma mensagem informando que não há comando correspondente a valor inserido. '''
'''¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'''


def teste_de_compatibilidade():

    print('')
    print('  |||||||||||||||||||||||||||||||||||||')
    print('  ERRO: VALOR INFORMADA É INCONCILIÁVEL')
    print('  |||||||||||||||||||||||||||||||||||||')
    print('')
    print('  |----------------------------------------------------------|')
