set_exemplo = set()
segundo_set = set()

for x in range(5):
    set_exemplo.add(x)

for x in range(5):
    segundo_set.add(100-x)

print(set_exemplo)

set_exemplo.add(4)

print(set_exemplo)

set_exemplo.discard(5)

print(set_exemplo)

set_exemplo.discard(4)

print(set_exemplo)

set_exemplo.add(4)

novo_set = set_exemplo.union(segundo_set)

print(novo_set)