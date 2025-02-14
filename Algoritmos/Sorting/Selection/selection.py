# Como você pode ver, o código é devéras semelhante de relance ao Bubble Sort, no entanto,
# No Selection Sort a gente coloca a variavel min_val

# Velocidade: O(N^2)
# Memória: O(1)

def selection_sort(array):

    for x in range(len(array)):
        
        # A gente atribui a variavel o valor de X pois X é o índice de um valor que a
        # gente vai iterando da esquerda pra direita:
        #
        # 1: [1, 2, 3], 2: [1, 2, 3], 3: [1, 2, 3]
        #     x                x                x
        #
        # permitindo o acesso a variavel nessa posição

        min_val = x

        for k in range(x, len(array)):

            # O motivo pelo qual a gente coloca esse loop é porque a gente precisa achar
            # um valor menor que o valor na posição X do array.
            # Por isso a gente procura da posição X até o fim (x, len(array))

            # E se o valor na posição K for menor que o valor na posição 
            # min_val (que na primeira iteração de K, X <==> min_val), min_val deixa de ser
            # X e se torna K:
            #
            # x = 5, min_val = 5, k = 7
            # x = 5, min_val = 5, k = 11
            # x = 5, min_val = 5, k = 9
            # x = 5, min_val = 2, k = 2
            # x = 5, min_val = 2, k = 4

            if array[k]<array[min_val]:
                min_val = k
        
        # E por fim, a gente troca os valores das posições min_val e X de lugar
        # O motivo pelo qual não há nenhum condicional pra verifica se são o mesmo número,
        # é porque se X e min_val não são o mesmo número, tem que troca de qualquer forma,
        # e se for, não vai fazer diferença trocar eles, os dois são o mesmo número

        array[x], array[min_val] = array[min_val], array[x]
        print(array)

arr = [8, 2, 4, 7, 1, 3, 9, 6, 5]
print(arr)
selection_sort(arr)
