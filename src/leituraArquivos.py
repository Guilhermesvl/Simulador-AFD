#1. **Estados:** Um conjunto finito de estados.

#2. **Alfabeto:** Um conjunto finito de símbolos chamado de alfabeto.

#3. **Transições:** Uma função de transição que mapeia cada par (estado, símbolo) para outro estado.

#4. **Estado Inicial:** Um estado inicial, que é o estado em que o AFD começa a processar a entrada.

#5. **Estados de Aceitação:** Um conjunto de estados de aceitação, que indica os estados nos quais o AFD deve estar para aceitar uma cadeia.
def lerArquivo(nomeArquivo):
    with open(nomeArquivo, 'r') as arquivo:
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


conjuntoEstados, alfabeto, transicoes, estadoInicial, estadosFinais, numeroPalavras, palavras = lerArquivo('entrada.txt')

print("Conjunto de Estados:", conjuntoEstados)
print("Alfabeto:", alfabeto)
print("Transições:", transicoes)
print("Estado Inicial:", estadoInicial)
print("Estados Finais:", estadosFinais)
print("Número de Palavras:", numeroPalavras)
print("Palavras:", palavras)