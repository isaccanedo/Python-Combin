import mods as mod

def interface():

    op = -1
    while op != 0:

        print(''' 
      > 1 - Realizar Apostas | 4 - Comparar Apostas | 
      > 2 - Eliminar Apostas | 5 - Arquivar Apostas | 0 - Sair
      > 3 - Imprimir Apostas | 6 - Carregar Apostas | 
              ''')
        op = int(input('  > '))
        print('')
        print('  |----------------------------------------------------------|')

        if op == 0:

            print('')
            print('  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('  PROJETO FINALIZADO COM SUCESSO')
            print('  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('')
            print('  |----------------------------------------------------------|')

        elif op == 1:

            op1 = -1

            while op1 != 0:

                print('''
      > 0 - Voltar.
      > 1 - Informar Valores Manualmente
      > 2 - Gerar Valores Aleatoriamente
                      ''')
                op1 = int(input('  > '))
                print('')
                print(
                    '  |----------------------------------------------------------|'
                )

                if op1 == 0:

                    pass

                elif op1 == 1:

                    mod.informar_valores_manualmente()

                elif op1 == 2:

                    mod.gerar_valores_aleatoriamente()

                else:

                    mod.teste_de_compatibilidade()

        elif op == 2:

            le = mod.teste_de_contagem()

            if le == 0:

                mod.teste_de_registro()

            else:

                op2 = -1

                while op2 != 0:

                    print('''
      > 0 - Voltar
      > 1 - Eliminar Aposta
      > 2 - Eliminar Todas as Apostas
                          ''')
                    op2 = int(input('  > '))
                    print('')
                    print(
                        '  |----------------------------------------------------------|'
                    )

                    if op2 == 0:

                        pass

                    elif op2 == 1:

                        mod.imprimir_lista_de_apostas()

                        mod.eliminar_aposta()

                    elif op2 == 2:

                        mod.eliminar_todas_as_apostas()

                        op2 = 0

                    else:

                        mod.teste_de_compatibilidade()

        elif op == 3:

            le = mod.teste_de_contagem()

            if le == 0:

                mod.teste_de_registro()

            else:

                mod.imprimir_lista_de_apostas()

        elif op == 4:

            le = mod.teste_de_contagem()

            if le == 0:

                mod.teste_de_registro()

            else:

                op4 = -1

                while op4 != 0:

                    print('''
      > 0 - Voltar
      > 1 - Informar Resultado Manualmente
      > 2 - Gerar Resultado Aleatoriamente
                          ''')
                    op4 = int(input('  > '))
                    print('')
                    print(
                        '  |----------------------------------------------------------|'
                    )

                    if op4 == 0:

                        pass

                    elif op4 == 1:

                        result = mod.informar_resultado_manualmente()

                        mod.comparar_lista_de_apostas_com_resultado(result)

                    elif op4 == 2:

                        result = mod.gerar_resultado_aleatoriamente()

                        mod.comparar_lista_de_apostas_com_resultado(result)

                    else:

                        mod.teste_de_compatibilidade()

        elif op == 5:

            le = mod.teste_de_contagem()

            if le == 0:

                mod.teste_de_registro()

            else:

                mod.arquivar_apostas()

        elif op == 6:

            mod.carregar_apostas()

        else:

            mod.teste_de_compatibilidade()


interface()
