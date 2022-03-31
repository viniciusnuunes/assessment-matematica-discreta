from itemEntrega import ItemEntrega
from local import Local
from caminhao import Caminhao

listaDeLocais = [Local('777', 'Ministro Gabriel de Piza'),
                 Local('109', 'Elvira da Fonseca')]
listaDeItens = [ItemEntrega('1', 'celular'), ItemEntrega(
    '2', 'relogio'), ItemEntrega('3', 'mouse'), ItemEntrega('4', 'bolsa adidas')]
listaDeCaminhoes = [Caminhao('lll999'), Caminhao('mmm000')]
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
    idLocaisAssociados = []

    # buscando caminhões
    for c in listaDeCaminhoes:
        caminhao = c.get()

        # buscando os locais associados ao caminhão
        for local in caminhao[1]:
            l = local.get()

            # verificando se o Ponto de entrega possui itens
            if local.possuiItensEntrega():
                idLocaisAssociados.insert(0, l[0])

            # verificando os Itens que estão associados ao Local
            # que está associado à este caminhão e colocando-os
            # na caçamba
            for item in l[2]:
                c.associarItemEntrega(item)

    # Caso haja pontos de entrega cadastrados sem caminhão associado

    # Para cada ponto de entrega P, verifica que caminhão C
    # possui menos pontos de entrega, e aloca P a C
    tamanhoLocais = len(listaDeLocais)

    print(idLocaisAssociados)
    print(tamanhoLocais)

    # há locais (que possuem itens associados) sem caminhoes associados?
    # if len(idLocaisAssociados != len(tamanhoLocais)):
        # verificar qual caminhão tem menos ponto de entrega
        # aux =  0
        # caminhaoMaisVazio = None

        # for idx, caminhao in enumerate(listaDeCaminhoes):
        #     aux = caminhao.quantidadeItensEntrega()

    totalPontosVisitados = 0
    totalItensEntregues = 0

    for caminhao in listaDeCaminhoes:
        if caminhao.possuiLocais():            
            c = caminhao.get()
            print(f'Percurso do caminhão {c[0].upper()}')

            for local in c[1]:
                l = local.get()
                totalPontosVisitados += 1
                print(f'    Visitado o Ponto de Entrega {l[1].upper()}. Foram entregue os itens:')
                
                for item in l[2]:
                    i = item.get()
                    totalItensEntregues += 1
                    print(f'        {i[1]} - {l[1]}'.upper())
            
            print(f'Percurso do caminhão {c[0].upper()} finalizado')
            print('-----------------------------------------')
        else:
            print(f'Caminhão {caminhao.placa.upper()} não está associado a nenhum Local')

    print('-----------------------------------------')        
    print(f'Total de pontos de entrega: {str(totalPontosVisitados)}')
    print(f'Total de Itens entregues: {str(totalItensEntregues)}')
    print('ROTINA FINALIZADA')

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
