from ponto import Ponto

try:
    arquivo = open('arquivo_pontos.txt', 'r')
    lista_pontos = []

    for linha in arquivo:
        linha = linha.strip()

        dados_ponto = linha.split(' ')
        # print(dados_ponto)

        nome = dados_ponto[0]
        # print(nome)

        coordenadas = dados_ponto[1].split(',')
        # print(posicoes)

        x = coordenadas[0]
        y = coordenadas[1]

        novo_ponto = Ponto(nome, x, y)
        lista_pontos.append(novo_ponto)

    arquivo.close()

    print(f'PONTOS LIDOS A PARTIR DE {arquivo.name}')
    print('---------------------------------------------------')
    for ponto in lista_pontos:
        print(ponto.__str__())

except (FileNotFoundError):
    print('O arquivo com os pontos não existe!')
except (PermissionError):
    print('O acesso ao arquivo foi negado. Verifique suas permissões!')
except (IsADirectoryError):
    print('O caminho indicado para o arquivo é uma pasta e não um arquivo!')
except (OSError):
    print('Erro retornado pelo sistema operacional durante a execução')
except (Exception):
    print('ERRO CATASTRÓFICO! ENCERRANDO IMEDIATAMENTE')
