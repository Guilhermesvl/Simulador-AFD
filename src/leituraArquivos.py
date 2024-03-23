class LeitorArquivo:

    def __init__(self, nomeArquivo):
        self.nomeArquivo = nomeArquivo

    def lerArquivo(self):
        with open(self.nomeArquivo, 'r') as arquivo:
            #Lendo e divide as entradas do arquivo
            conjuntoEstados = arquivo.readline().strip().split(', ') 
            alfabeto = arquivo.readline().strip().split(', ')  

            transicoes = []
            formatoTransicoes = arquivo.readline().strip().split(' - ')
            for transicao in formatoTransicoes:
                transicao = tuple(transicao.strip('()').split(', '))
                transicoes.append(transicao)

            estadoInicial = arquivo.readline().strip()
            estadosFinais = set(arquivo.readline().strip().split(', '))
            numeroPalavras = int(arquivo.readline().strip())
            palavras = [linha.strip() for linha in arquivo.readlines()]

        return conjuntoEstados, alfabeto, transicoes, estadoInicial, estadosFinais, numeroPalavras, palavras


