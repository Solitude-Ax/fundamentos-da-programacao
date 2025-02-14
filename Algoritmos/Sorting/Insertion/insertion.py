# Como você pode ver, esses 3 primeiros algorítmos de ordenação iniciantes possuem uma
# estrutura bastante parecida: Itera pela lista pra achar um valor menor que o valor que 
# você atualmente tem, de certa forma.

# Porémm, Insertion Sort é um pouco mais complexo e diferenciado dos outros 2

# Velocidade: O(N^2)
# Memória: O(1)

def insertion_sort(array):

    for x in range(len(array)):

        # Primeiramente, a gente começa criando uma variável que tem o valor de X. Porque?
        # Porque X é o valor que a gente cria enquanto itera pela lista, e a gente pode usar
        # isso pra iterar pela parte de trás pela lista:
        #
        # [1, 2, 3], x = 2, j = 2
        #        x
        #
        # [1, 2, 3], x = 2, j = 1
        #     J  x
        #
        # [1, 2, 3], x = 2, j = 0
        #  j     x

        # Já a variavel temp é porque o Array na posição X vai se tornar outro número, e por isso a
        # gente precisa de uma forma de guardar esse número pra usar depois

        j = x
        temp = array[x]

        # Aqui a gente itera pela Lista usando While. Porque While e não For Loop? Bem, com While,
        # a gente tem mais controle sobre o Loop, mas se quiser fazer funcionam com um For Loop
        # fique a vontade, eu não consegui

        while j > -1:

            # Então nós verificamos se o valor na posição J é maior que temp, e se esse for o caso,
            # o valor que vem depois do J se torna o J:
            #
            # [1, 5, 2], temp = 2
            #     j
            # [1, 5, 5], temp = 2
            #     j
            #
            # Mas porque que não da algum erro mecher com j + 1? Porque j + 1 é sempre um valor menor
            # que a própria lista, e porque é como se j + 1 fosse a sombra da nossa mira onde a gente 
            # quer botar a variavel temp
            #
            # [1, 5, 7, 2], temp = 2
            #        j  t
            # [1, 5, 7, 7], temp = 2
            #     j  t
            # [1, 5, 5, 7], temp = 2
            #  j  t

            # E também, como a gente construiu esse loop com base de que J deve ser maior que -1 pra
            # ele rodar, isso significa que nunca vai dar erro de pegar um valor que não existe no
            # array
            #
            # Só existem 2 coisas que podem acontecer pra acabar esse loop:
            #
            # 1: é encontrado uma variavel que é menor que temp:
            #
            # [1, 5, 5, 7], temp = 2
            #  j  t
            # [1, 2, 5, 7], temp = 2
            #  j  t
            #
            # 2: J vai pra fora do Array e o loop acaba:
            #
            #   [3, 5, 7, 1], j = 2
            #          j  t
            #   [3, 5, 7, 7], j = 1
            #       j  t
            #   [3, 5, 5, 7], j = 0
            #    j  t
            #   [3, 3, 5, 7], j = -1
            # j  t  

            if array[j] > temp:
                array[j+1] = array[j]
            elif array[j]<temp:
                array[j+1] = temp
                break
            j-=1
        
        # To do: botar descrição aqui
        # Por fim, caso tenha ou não acontecido o segundo caso acima, o código por precaução troca o J + 1 por temp,
        # e isso não da problema pois se tivesse sido encontrado um valor menor que temp, J teria parado


        array[j+1] = temp
        print(array)

    return array

arr = [8, 2, 4, 7, 1, 3, 9, 6, 5]
print(insertion_sort(arr))