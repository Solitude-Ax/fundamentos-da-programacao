class Folder:
    
    def __init__(self, name):
        self.name = name
        self.files = []
        self.folders = []
    
    def __str__(self):
        return f"TIPO: pasta NOME: {self.name} NUM DE ARQUIVOS: {len(self.files)}"
    
    def add_to_folder(self, items:list):
        
        for item in items:
            
            if type(item) == File: 
                self.files.append(item)
            elif type(item) == Folder:
                self.folders.append(item)
    
    def show_folder(self):
        print(f"Pasta: {self.name}")
        item_count = 1
        for folder in self.folders:    
            print(item_count, ":", folder)
            item_count += 1
        
        for file in self.files:
            print(item_count, ":", file)
            item_count += 1
        
        print(end="\n")
            
    def rename_folder(self, new_name):
        #print("Insira novo nome da pasta: ")
        #self.name = self.text_input()
        self.name = new_name
    
    def text_input(self):
        return input("Insira texto aqui:")
        
class File:
    
    def __init__(self, name:str, size:int):
        
        self.name = name
        self.size = size
    
    def __str__(self):
        
        return f"TIPO: arquivo NOME: {self.name}, TAMANHO: {self.size} kbs"

class Root_Folder(Folder):
    
    def __init__(self):
        super().__init__("root")

meme = File("Banana", 33)
jojo = File("mimimi", 425)
papa = File("Yipe Yieeei", 666)
rosa = File("falta de criatividade", 420)
funy = File("lol", 69)
kiki = File("hihi", 15)
bubu = File("boo", 100)
lulu = File("lala", 200)
gigi = File("gaga", 300)
momo = File("meme", 500)
nini = File("nana", 700)
toto = File("tata", 900)

pasta = Folder("Gincana")
pista = Folder("Corrida")
sala = Folder("Aula")
cozinha = Folder("Comida")

root_folder = Root_Folder()

pasta.add_to_folder([meme, jojo, funy, gigi])
pista.add_to_folder([pasta, papa, rosa])
sala.add_to_folder([bubu, lulu, momo])
cozinha.add_to_folder([pista, sala])
root_folder.add_to_folder([cozinha, nini, toto])

print(pasta, pista, sala, cozinha, root_folder)

pasta.show_folder()
pista.show_folder()
sala.show_folder()
cozinha.show_folder()
root_folder.show_folder()