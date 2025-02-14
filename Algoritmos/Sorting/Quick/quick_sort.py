# Muito do que a gente falou sobre Merge Sort também cabe ao Quick Sort,
# visto que ambos usam recursividade, e portanto compartilham muitas características, mas
# também tem outras coisas interessantes a se falar, a primeira é que esse é o mais rápido dos algorítmos

# Algo também iteressante, é que o algorítmo é tão bom, que inputs gigantes como o circundade por comentários no fundo
# são processados em questão de segundos, mesmo em linguagens lentas como Python. Esse é o poder da Otimização

# Velocidade: O(n log n)
# Memória: O(N)

def quick_sort(array):

    # Em primeiro lugar, nesse algorítmo ao invés de retornanr quando o algoritmo tem tamanho 1,
    # a gente retorna quando ele tem tamanho 2, pois o algorítmo "não funciona" com arrays abaixo de 3 valores

    if len(array) < 2:
        return array

    #print(array)

    # Em primeiro lugar, a gente cria uma variável chamada de pivot, que vai ser o último valor do array

    pivot = len(array)-1

    # Em seguida, a gente cria outra variável, outra "flecha" que fica fora do array:
    #
    #   [2, 4, 1, 3], i = -1, pivot = 3
    # i           p

    i= -1

    for j in range(len(array)-1):

        # Então, a gente vai iterar pelo array, verificando se esse valor que a gente encontrou é menor
        # que o pivô, trocando o i e o j caso j seja menor que o pivô:
        #
        #   [2, 4, 1, 3], i = -1, j = 0, pivot = 3
        # i  j        p
        #   [2, 4, 1, 3], i = 0, j = 1, pivot = 3
        #    i  j     p
        #   [2, 4, 1, 3], i = 0, j = 2, pivot = 3
        #    i     j  p
        #   [2, 1, 4, 3], i = 1, j = 2, pivot = 3
        #       i  j  p

        if array[j] < array[pivot]:
            i += 1
            array[j], array[i] = array[i], array[j]
            print(array)
    
    # E por fim, a gente incrementa I denovo, e I e o Pivô trocam de lugar:
    #
    #   [2, 1, 4, 3], i = 1, j = 2, pivot = 3
    #       i  j  p
    #   [2, 1, 3, 4], i = 2, j = 2, pivot = 3
    #          i  p

    # E então, o pivô se torna I

    i += 1
    array[pivot], array[i] = array[i], array[pivot]
    pivot = i

    # Depois disso, a gente divide a lista no Pivô, sendo que valores a esquerda são
    # menores que o pivô e valores a direita são maiores

    ini_half = array[:pivot]
    end_half = array[pivot:]
    
    # E por fim, a gente usa a recursividade chamando a função com essas metades

    # Como pode ver no fim da função, o array é retornado, então a gente pode aribuir a essas variaveis
    # o array já organizado

    ini_half = quick_sort(ini_half)
    end_half = quick_sort(end_half)

    # E por fim, a gente junta essas metades organizadas, para então retornar ela

    array = ini_half + end_half

    return(array)

arr = [8, 2, 4, 1, 7, 3, 9, 6, 5]

print(quick_sort(arr))
print(quick_sort([12, 11, 13, 5, 6, 7]))

# ----------- # ----------- # ----------- # ----------- #

print(quick_sort([8, 2, 4, 7, 1, 3, 9, 6, 5, 55, 30, 48, 76, 92, 77, 99, 12, 15, 16, 24, 32, 58, 56, 735, 9297]))
print(quick_sort([8, 2, 4, 7, 1, 3, 9, 6, 5, 55, 30, 48, 76, 92, 77, 99, 12, 15, 16, 24, 32, 58, 56, 735, 9297]))
print(quick_sort([8, 2, 4, 7, 1, 3, 9, 6, 5, 55, 30, 48, 76, 92, 77, 99, 12, 15, 16, 24, 32, 58, 56, 735, 9297]))
print(quick_sort([8, 2, 4, 7, 1, 3, 9, 6, 5, 55, 30, 48, 76, 92, 77, 99, 12, 15, 16, 24, 32, 58, 56, 735, 9297]))
print(quick_sort([8, 2, 4, 7, 1, 3, 9, 6, 5, 55, 30, 48, 76, 92, 77, 99, 12, 15, 16, 24, 32, 58, 56, 735, 9297]))
print(quick_sort([8, 2, 4, 7, 1, 3, 9, 6, 5, 55, 30, 48, 76, 92, 77, 99, 12, 15, 16, 24, 32, 58, 56, 735, 9297]))

# ----------- # ----------- # ----------- # ----------- #

print(quick_sort([6, 1, 7, 4]))

print(quick_sort([5, 12, 17, 9, 3, 6, 4]))

quick_sort([2, 4, 1, 3])

#print(quick_sort([17, 71, 26, 31, 77, 36, 8, 37, 5, 50, 74, 46, 2, 77, 87, 55, 30, 48, 76, 92]))