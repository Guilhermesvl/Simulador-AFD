from leituraArquivos import LeitorArquivo
from afd import AFD

nomeArquivo = input("Digite o nome do arquivo para teste (entrada.txt): ")
diretorio = f'testes/{nomeArquivo}'

iniciar = LeitorArquivo(diretorio)
iniciar.lerArquivo()

conjuntoEstados = iniciar.getConjuntoEstados()
alfabeto = iniciar.getAlfabeto()
transicoes = iniciar.getTransicoes()
estadoInicial = iniciar.getEstadoInicial()
estadosFinais = iniciar.getEstadosFinais()

automato = AFD(conjuntoEstados, alfabeto, transicoes, estadoInicial, estadosFinais)

palavras = iniciar.getPalavras()


for palavra in palavras:
    resultado = automato.ehValida(palavra)
    if resultado == True:
        print(f"Palavra: {palavra} aceita" )
    else:
        print(f"Palavra: {palavra} rejeitada" )
