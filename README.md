# Implementação de um Autômato Finito Determinístico
 
 ## Sobre o Projeto

Este é um projeto idealizado pelo Professor Rafael Durelli, docente da disciplina de Teoria da Computação da Universidade Federal de Lavras (UFLA), que aborda os seguintes requisitos:

#### Objetivo

O objetivo deste trabalho prático é realizar a implementação de um Autômato Finito Determinístico (AFD) capaz de reconhecer cadeias de símbolos conforme as especificações fornecidas.

#### Descrição do Problema

Um Autômato Finito Determinístico (AFD) é um modelo matemático abstrato de um sistema computacional que reconhece cadeias de símbolos de uma linguagem regular. Ele é composto por cinco elementos:

1. **Estados:** Um conjunto finito de estados.
2. **Alfabeto:** Um conjunto finito de símbolos chamado de alfabeto.
3. **Transições:** Uma função de transição que mapeia cada par (estado, símbolo) para outro estado.
4. **Estado Inicial:** Um estado inicial, que é o estado em que o AFD começa a processar a entrada.
5. **Estados de Aceitação:** Um conjunto de estados de aceitação, que indica os estados nos quais o AFD deve estar para aceitar uma cadeia.

#### Implementação do AFD

Os alunos devem implementar um AFD genérico que receba os cinco elementos mencionados acima como entrada e seja capaz de processar uma cadeia de entrada para determinar se ela é aceita ou rejeitada pelo AFD.


 ## Sobre a estrutura do arquivo

    Para que haja a simulação do Autômato Finito Determinístico (AFD), o arquivo deve estar formatado da seguinte forma:

1. **Estados:** devem ser listados separados por vírgula. Por exemplo: `q0, q1`;
2.  **Alfabeto:** deve ser listado separado por vírgula. Por exemplo: `a, b`;
3. **Transições:** devem ser apresentadas dentro de parênteses e separadas por " - ". Por exemplo: `(q0, a, q1) - (q1, b, q1)`;
4.  **Estado Inicial:** deve ser indicado. Por exemplo: `q0`;
5. **Estados de Aceitação:** devem ser listados separados por vírgula, quando houver mais de um. Por exemplo: `q0, q1`;
6. **Palavras:**  nas linhas subsequentes, as palavras a serem testadas devem ser fornecidas uma em cada linha;

        OBS. Caso queira simular seus próprios autômatos, verifique se o arquivo está no diretório apropriado e devidamente formatado.


 ## Como usar: 

 - Compile o arquivo `main.py`;
 - Digite o nome do arquivo que deseja testar. \<nome do arquivo\>**.txt**
        
        
    
- A saída do programa será "aceita" ou "rejeitada", para as palavras usadas no teste.

