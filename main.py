import itemEntrega

sair = False
itemEntrega = itemEntrega.ItemEntrega()

def menuVolume():
    print('---------- Menu De Volumes ----------')
    print('1 - Inserir Volume')
    print('2 - Remover Volume')
    print('3 - Verificar Volume no Topo')
    print('4 - Exibir a lista de Volumes')
    print('0 - Voltar ao menu anterior')
    print('--------------------')

    opcao = input('Opção escolhida -> ')

    try:
        opcao = int(opcao)
    except:
        print('Utilize somente números')
        menuVolume()

    if opcao == 0:
        return
    elif opcao == 1:
        id = str(input('Informe um Identificador para o item: '))
        item = str(input('Informe o nome do item à ser inserido: '))
        itemEntrega.inserir(id, item)

    elif opcao == 2:
        id = str(input('Informe o ID do item à ser removido: '))
        try:
            itemEntrega.remover(id)
        except Exception as e:
            print(e)

    elif opcao == 3:
        topo = itemEntrega.topo()
        print(topo)

    elif opcao == 4:
        listaVolumes = itemEntrega.mostrarItens()
        print(listaVolumes)
    else:
        print(f'Opção {opcao} não é válida')
        menuVolume()

    menuVolume()


while not sair:
    print('---------- Menu Principal ----------')
    print('1 - Administrar Volumes')
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
        menuVolume()
    else:
        print(f'Opção {opcao} não é válida')
        continue
