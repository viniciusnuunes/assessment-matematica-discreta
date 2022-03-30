from itemEntrega import ItemEntrega
from local import Local
from caminhao import Caminhao

listaDeLocais = []
listaDeItens = []
listaDeCaminhoes = []
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
        # associar o item ao local
        for i in listaDeItens:
            x = i.get()
            print(f'[ID: {x[0]}] - {x[1]}')

        idItemEntrega = input('Selecione o ID do Item a ser associado: ')

        for i in listaDeLocais:
            x = i.get()
            print(f'[ID: {x[0]}] - {x[1]}')

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

    elif opcao == '5':
        # associa Local ao Caminhão
        for i in listaDeLocais:
            x = i.get()
            print(f'[ID: {x[0]}] - {x[1]}')

        idLocal = input(
            'Selecione o ID do Local a ser associado ao Caminhão: ')

        for i in listaDeCaminhoes:
            x = i.get()
            print(f'[ID: {x[0]}] - {x[1]}')

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
    elif opcao == '9':
        for i in listaDeItens:
            x = i.get()
            print(x)

        for i in listaDeLocais:
            x = i.get()
            print(x)

        for i in listaDeCaminhoes:
            x = i.get()
            print(x)

        print(listaDeItens)
        print(listaDeLocais)
        print(listaDeCaminhoes)
    else:
        print(f'Opção {opcao} não é válida')
