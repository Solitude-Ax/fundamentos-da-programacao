# O Bubble Sort, o mais ineficiente dos arrays de Ordenação,
# funciona na seguinte forma:
#
# O algoritmo vai iterando pela lista, e quando acha um valor,
# vai "arrastando" ele até o fundo, enquanto o próximo valor for menor que ele
#
# Ex:
# swaped = False
#
# [7, 5, 1, 3] 7 > 5 swaped = True
# [5, 7, 1, 3] 7 > 1
# [5, 1, 7, 3] 7 > 3
#  
# Como pode ver, a gente levou o 7 pro fundo: [5, 1, 3, 7], mas a lista ainda
# não tá organizada, por isso, a gente repete essa operação N vezes (N no caso é o tamanho da lista)
# 
# [5, 1, 3, 7] 5 > 1 swaped = True
# [1, 5, 3, 7] 5 > 3
# [1, 3, 5, 7] 5 < 7
#
# Aqui, a gente ja terminou de organizar a lista, mas o algoritmo ainda não sabe disso,
# e por isso, a gente usa a variavel swaped abaixo
#
# Quando na iteração em que a gente "arrasta" o número, a gente acabar trocando um valor de lugar,
# essa variavel fica True, e se tiver False, o algoritmo entende que a lsita ta organizada e acaba

#Velocidade: O(N^2)
# Memória: O(1)

def bubble_sort(array):

    for x in range(len(array)):

        swaped = False

        for k in range(x, len(array)):

            if array[k]<array[x]:
                array[k], array[x] = array[x], array[k]
                print(array)
                swaped = True
        if swaped == False:
            break

    return array
    
    
arr = [8, 2, 4, 7, 1, 3, 9, 6, 5]
print(arr)
print(bubble_sort(arr))

def recursividade():

    print("chamando função")
    recursividade()

