# Ja a busca binária, ela divide primeiro o array, e então verifica se 
# o item do meio é o que ta procurando
#
# Exemplo (procurando 7):
# [1, 3, 5, 7, 9]
# [1, 3], [7, 9]
# [7] Item encontrado

# Óbviamente, o array deve estar organizado de maior pra menor ou vice versa

# Velocidade: O(log n)
# Memória: O(N)

def binary_search(array, target):

    if len(array) <= 1 or array == []:
        return "Target not found"

    mid = len(array)//2

    if array[mid] == target:
        return f"Target found at position {mid}"
    else:
        if target > array[mid]:
            return binary_search(array[mid:], target)
        else:
            return binary_search(array[:mid], target)
    
    


arr = [1, 3, 5, 9, 15, 17, 21, 44]

print(binary_search(arr, 17))
print(binary_search(arr, 21))
print(binary_search(arr, 5))
print(binary_search(arr, 45))

arr1 = [1, 3, 5, 9, 15, 17, 21, 44]

# Test cases for elements in the middle, edges, and non-existent values
print(binary_search(arr1, 17))  # Elemento encontrado! (Present, near the end)
print(binary_search(arr1, 1))   # Elemento encontrado! (Present, first element)
print(binary_search(arr1, 44))  # Elemento encontrado! (Present, last element)
print(binary_search(arr1, 9))   # Elemento encontrado! (Present, middle element)
print(binary_search(arr1, 45))  # Elemento não existe. (Not present)
print(binary_search(arr1, 0))   # Elemento não existe. (Not present, less than min)
print(binary_search(arr1, 22))  # Elemento não existe. (Not present, between values)

# Edge case: single-element array
arr2 = [10]
print(binary_search(arr2, 10))  # Elemento encontrado! (Present, only element)
print(binary_search(arr2, 5))   # Elemento não existe. (Not present, out of bounds)

# Edge case: empty array
arr3 = []
print(binary_search(arr3, 10))  # Elemento não existe. (Array is empty)
