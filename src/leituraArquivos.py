class LeitorArquivo:

    def __init__(self, nomeArquivo):
        self.nomeArquivo = nomeArquivo
        self.conjuntoEstados = None
        self.alfabeto = None
        self.transicoes = None
        self.estadoInicial= None
        self.estadosFinais = None
        self.palavras = None

    def lerArquivo(self):
        with open(self.nomeArquivo, 'r') as arquivo:
            #Lendo e divide as entradas do arquivo
            self.conjuntoEstados = arquivo.readline().strip().split(', ') 
            self.alfabeto = arquivo.readline().strip().split(', ')  

            self.transicoes = []
            formatoTransicoes = arquivo.readline().strip().split(' - ')
            for transicao in formatoTransicoes:
                transicao = tuple(transicao.strip('()').split(', '))
                self.transicoes.append(transicao)

            self.estadoInicial = arquivo.readline().strip()
            self.estadosFinais = set(arquivo.readline().strip().split(', '))

            self.palavras = [linha.strip() for linha in arquivo.readlines()]


    def getConjuntoEstados(self):
        return self.conjuntoEstados

    def getAlfabeto(self):
        return self.alfabeto
    
    def getTransicoes(self):
        return self.transicoes
    
    def getEstadoInicial(self):
        return self.estadoInicial
    
    def getEstadosFinais(self):
        return self.estadosFinais
    
    def getPalavras(self):
        return self.palavras

       


