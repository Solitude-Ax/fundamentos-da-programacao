# Esse é o primeiro algoritmo que queria apresentar

# O algoritmo de busca linear, busca em uma lista de item em item até achar o que ta procurando
# Exemplo (procurando 7):
#     v                v                v                v
#    [1, 3, 5, 7], [1, 3, 5, 7], [1, 3, 5, 7], [1, 3, 5, 7]
# 
# Isso faz com que ele seja O(1) em memória (ele usa apenas a memória para guardar o array) e
# O(N) de velocidade (N sendo o tamanho do array, um array de 4 elementos teria 4 de "distancia")

# Velocidade: O(N)
# Memória: O(1)

arr = [1, 7, 99, 4, 18, 35, 84, 53, 15, 9]

def linear_search(searched_array, element_searched):

    for elm_id, element in enumerate(searched_array):
        
        if element == element_searched:
            return f"The element {element} was found in position {elm_id}!"
        
    return "The element does not exist in the array."

print(linear_search(arr, 1))
print(linear_search(arr, 9))
print(linear_search(arr, 18))
print(linear_search(arr, 54))