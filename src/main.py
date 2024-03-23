from leituraArquivos import LeitorArquivo

nomeArquivo = input("Digite o nome do arquivo para teste: /'entrada.txt' ")
diretorio = f'testes/{nomeArquivo}'

iniciar = LeitorArquivo(diretorio)

iniciar.lerArquivo()