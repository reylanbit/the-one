# Explicação dos Algoritmos de Ordenação

Este documento fornece uma breve explicação teórica sobre os algoritmos implementados no **SortViz**.

## 1. Bubble Sort (Ordenação por Bolha)
O Bubble Sort percorre a lista repetidamente, compara elementos adjacentes e os troca se estiverem na ordem errada. Os maiores elementos "flutuam" para o final da lista como bolhas.
- **Complexidade**: O(n²)
- **Estável**: Sim
- **Ideal para**: Fins didáticos e listas muito pequenas.

## 2. Selection Sort (Ordenação por Seleção)
Divide a lista em duas partes: a sublista de itens já ordenados e a sublista de itens restantes. Em cada passo, ele encontra o menor elemento da parte não ordenada e o coloca no início da parte não ordenada (trocando-o de lugar).
- **Complexidade**: O(n²)
- **Estável**: Geralmente não
- **Vantagem**: Realiza o número mínimo de trocas (O(n)).

## 3. Insertion Sort (Ordenação por Inserção)
Constrói a lista ordenada um item por vez. Ele pega um elemento da parte não ordenada e o "insere" na posição correta dentro da parte já ordenada, deslocando os elementos maiores.
- **Complexidade**: O(n²) no pior caso, O(n) se a lista já estiver quase ordenada.
- **Estável**: Sim
- **Ideal para**: Listas pequenas ou quase ordenadas.

## 4. Merge Sort (Ordenação por Intercalação)
Um algoritmo de "dividir para conquistar". Ele divide recursivamente a lista em duas metades até que cada sublista tenha apenas um elemento, e então combina (intercala) essas metades de forma ordenada.
- **Complexidade**: O(n log n)
- **Estável**: Sim
- **Desvantagem**: Requer memória extra proporcional ao tamanho da lista.

## 5. Quick Sort (Ordenação Rápida)
Também usa "dividir para conquistar". Escolhe um elemento como "pivô" e particiona a lista em duas sublistas: elementos menores que o pivô e elementos maiores. Em seguida, ordena as sublistas recursivamente.
- **Complexidade**: O(n log n) na média, O(n²) no pior caso (embora raro com bons pivôs).
- **Estável**: Não
- **Ideal para**: Alta performance na prática.
