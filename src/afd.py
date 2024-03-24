class AFD:
    def __init__(self, conjuntoEstados, alfabeto, transicoes, estadoInicial, estadosFinais):
        self.conjuntoEstados = conjuntoEstados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estadoInicial = estadoInicial
        self.estadosFinais = estadosFinais

    def ehValida(self, palavra):
        estadoAtual = self.estadoInicial

        for simbolo in palavra:
            transicaoExiste = False
            for transicao in self.transicoes:
                if transicao[0] == estadoAtual and transicao[1] == simbolo:
                    estadoAtual = transicao[2]
                    transicaoExiste = True
                    break

            if transicaoExiste == False:
                return False
                
                
        return estadoAtual in self.estadosFinais
           
