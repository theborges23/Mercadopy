from typing import List, Dict
from time import sleep

from Models.Produto import Produto
from Utils.helper import formata_float_str_moeda


produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('============================================')
    print('============== Bem vindo(a) ================')
    print('==============  Loja Teste  ================')
    print('============================================')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar produto')
    print('2 - Listar produto')
    print('3 - Comprar produto')
    print('4 - Visualizar Carrinho')
    print('5 - Fechar pedido')
    print('6 - sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte Sempre')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida!')
        sleep(1)
        menu()


def cadastrar_produto() -> None:
    print('Cadastro de Produto')
    print('===================')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    produto = Produto(nome, preco)
    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()


def listar_produto() -> None:
    if len(produtos) > 0:
        print('Listagem de produtos')
        print('====================')
        for produto in produtos:
            print(produto)
            print('-----------------')
            sleep(1)
    else:
        print('Ainda não existem produtos cadastrados!')
        sleep(2)
        menu()


def comprar_produto() -> None:
    pass


def visualizar_carrinho() -> None:
    pass


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f' Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('--------------------------------')
                sleep(1)
        print(f'A sua fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não existem produtos no carrinho!')
        sleep(2)
        menu()


def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo
            p = produto
    return p


if __name__ == '__main__':
    main()

