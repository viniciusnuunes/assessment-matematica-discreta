from itemEntrega import ItemEntrega
from local import Local
from caminhao import Caminhao

listaDeLocais = []
listaDeItens = []
listaDeCaminhoes = []
sair = False


def associaItemAoLocal():
    for i in listaDeItens:
        print(i)

    idItemEntrega = input('Selecione o ID do Item a ser associado: ')

    for i in listaDeLocais:
        print(i)

    idLocal = input('Selecione o ID do Local para associar ao Item: ')

    idxItem = None

    for idx, l in enumerate(listaDeItens):
        x = l.get()
        if idItemEntrega == x[0]:
            idxItem = idx
            itemAssociar = l

    for idx, l in enumerate(listaDeLocais):
        x = l.get()
        if idLocal == x[0]:
            localAssociar = l

    localAssociar.associar(itemAssociar)
    listaDeItens.pop(idxItem)

    print('Item associado com sucesso ao Local')


def associaLocalAoCaminhao():
    for i in listaDeLocais:
        print(i)

    idLocal = input(
        'Selecione o ID do Local a ser associado ao Caminhão: ')

    for i in listaDeCaminhoes:
        print(i)

    placaCaminhao = input('Selecione a Placa do Caminhão: ')

    for idx, l in enumerate(listaDeLocais):
        x = l.get()
        if idLocal == x[0]:
            localAssociar = l

    for idx, c in enumerate(listaDeCaminhoes):
        x = c.get()
        if placaCaminhao == x[0]:
            caminhaoAssociar = c

    caminhaoAssociar.associarLocal(localAssociar)

    print('Local associado ao Caminhão com sucesso')


def realizarEntregas():
    for caminhao in listaDeCaminhoes:
        caminhao = caminhao.get()

        for local in caminhao.Locais:
            local = local.get()

            for item in local.ItensEntrega:
                item = item.get()

                caminhao.associarItemEntrega(item)

    print(listaDeCaminhoes)


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

    if opcao == '0':
        sair = True
        print('Programa finalizado')
    elif opcao == '1':
        id = str(input('Informe um Identificador para o ponto de entrega: '))
        nome = str(input('Informe o nome do ponto de entrega à ser inserido: '))

        local = Local(id, nome)
        listaDeLocais.append(local)
    elif opcao == '2':
        id = str(input('Informe um Identificador para o item: '))
        nome = str(input('Informe o nome do item à ser inserido: '))

        itemEntrega = ItemEntrega(id, nome)
        listaDeItens.append(itemEntrega)
    elif opcao == '3':
        placa = str(input('Informe a placa do Caminhão: '))

        caminhao = Caminhao(placa)
        listaDeCaminhoes.append(caminhao)
    elif opcao == '4':
        associaItemAoLocal()
    elif opcao == '5':
        associaLocalAoCaminhao()
    elif opcao == '6':
        realizarEntregas()
    elif opcao == '9':
        for i in listaDeItens:
            print(i)

        for i in listaDeLocais:
            print(i)

        for i in listaDeCaminhoes:
            print(i)

        print(listaDeItens)
        print(listaDeLocais)
        print(listaDeCaminhoes)
    else:
        print(f'Opção {opcao} não é válida')
