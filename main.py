from itemEntrega import ItemEntrega
from local import Local
from caminhao import Caminhao


# itemEntrega = ItemEntrega()
# local = Local()

# def menuItem():
#     print('---------- Menu De Itens ----------')
#     print('1 - Inserir Item')
#     print('2 - Remover Item')
#     print('3 - Verificar Item no Topo')
#     print('4 - Exibir a lista de Itens')
#     print('0 - Voltar ao menu anterior')
#     print('--------------------')

#     opcao = input('Opção escolhida -> ')

#     try:
#         opcao = int(opcao)
#     except:
#         print('Utilize somente números')
#         menuItem()

#     if opcao == 0:
#         return
#     elif opcao == 1:
#         id = str(input('Informe um Identificador para o item: '))
#         nome = str(input('Informe o nome do item à ser inserido: '))
#         itemEntrega.inserir(id, nome)

#     elif opcao == 2:
#         id = str(input('Informe o ID do item à ser removido: '))
#         try:
#             itemEntrega.remover(id)
#         except Exception as e:
#             print(e)

#     elif opcao == 3:
#         topo = itemEntrega.topo()
#         print(topo)

#     elif opcao == 4:
#         listaVolumes = itemEntrega.mostrarItens()
#         print(listaVolumes)
#     else:
#         print(f'Opção {opcao} não é válida')
#         menuItem()

#     menuItem()


# def menuEntrega():
#     print('---------- Menu De Entregas ----------')
#     print('1 - Inserir ponto de Entrega')
#     print('2 - Remover ponto de Entrega')
#     print('3 - Associar um Ponto de Entrega a um Item')
#     print('4 - Exibir a lista de Entregas')
#     print('0 - Voltar ao menu anterior')
#     print('--------------------')

#     opcao = input('Opção escolhida -> ')

#     try:
#         opcao = int(opcao)
#     except:
#         print('Utilize somente números')
#         menuEntrega()

#     if opcao == 0:
#         return
#     elif opcao == 1:
#         id = str(input('Informe um Identificador para o ponto de entrega: '))
#         nome = str(input('Informe o nome do ponto de entrega à ser inserido: '))
#         local.inserir(id, nome)

#     elif opcao == 2:
#         id = str(input('Informe o ID do item à ser removido: '))
#         try:
#             local.remover(id)
#         except Exception as e:
#             print(e)

#     elif opcao == 3:
#         locais = local.mostrarLocais()
#         for i in locais:
#             print(f'ID: [{i[0]}] - {i[1]}')
#         idLocal = input('Informe o ID do Local para iniciar a associação: ')

#         itens = itemEntrega.mostrarItens()
#         for i in itens:
#             print(f'ID: [{i[0]}] - {i[1]}')
#         idItemEntrega = input('Informe o ID do Item a ser associado: ')

#         local.associar(idLocal, idItemEntrega)

#     elif opcao == 4:
#         listaEntregas = local.mostrarLocais()
#         print(listaEntregas)
#     else:
#         print(f'Opção {opcao} não é válida')
#         menuEntrega()

#     menuEntrega()

sair = False

while not sair:
    print('---------- Menu Principal ----------')
    print('1 - Inserir Ponto de Entrega')
    print('2 - Inserir Item de Entrega')
    print('3 - Inserir Caminhão')
    print('4 - Associar item a ponto de entrega')
    print('5 - Associar ponto de entrega a caminhão')
    print('6 - Realizar entregas')
    print('0 - Sair')
    print('--------------------')

    opcao = input('Opção escolhida -> ')

    try:
        opcao = int(opcao)
    except:
        print('Utilize somente números')
        continue

    if opcao == 0:
        sair = True
        print('Programa finalizado')
        continue
    elif opcao == 1:
        local = Local()

        id = str(input('Informe um Identificador para o ponto de entrega: '))
        nome = str(input('Informe o nome do ponto de entrega à ser inserido: '))
        local.inserir(id, nome)
    elif opcao == 2:
        itemEntrega = ItemEntrega()

        id = str(input('Informe um Identificador para o item: '))
        nome = str(input('Informe o nome do item à ser inserido: '))
        itemEntrega.inserir(id, nome)
    elif opcao == 3:
        caminhao = Caminhao()

        placa = str(input('Informe a placa do Caminhão: '))
        itemEntrega.inserir(placa)
    elif opcao == 9:
        itemEntrega = ItemEntrega()

        print(itemEntrega.mostrarItens())
    else:
        print(f'Opção {opcao} não é válida')
        continue
