class Post:

    def __init__(self, user, content):
        
        self.user = user
        self.content = content
        self.likes = 0
        self.views = 0
        self.shares = 0

    def __repr__(self):
        return f"Post de Usuario {self.user} \nConteúdo: {self.content}\n\nLikes: {self.likes} \nViews: {self.views} \nCompartilhamentos: {self.shares}\n\n"

    def edit_post(self, edited_content):
        self.content = edited_content
    
#    def delete_post(self):
 #       del self
    
    def increase_like(self, user):
        self.likes += 1
    
    def increase_view(self, user):
        self.views += 1
    
    def increase_share(self, user):
        self.shares += 1

class Usuario:
    
    user_id = 0

    def __init__(self, nome, sobrenome = None):

        Usuario.user_id += 1
        self.user_id = Usuario.user_id

        self.nome = nome
        self.sobrenome = sobrenome
        self.post_id = 0

        self.bloqueados = []
        self.amigos = []
        self.posts = {}
    
    def __eq__(self, other):
        return self.user_id == other
    
    def __hash__(self):
        return hash(self.user_id)

    def __repr__(self):
        if self.sobrenome:
            return f"{self.nome} {self.sobrenome}"
        else:
            return f"{self.nome}"
    
    def create_post(self, content):

        #while True:

        if not content:
            print("Desculpe, mas o post não deve estar vazio")
            return

        new_post = Post(self.__repr__(), content)
        self.posts[self.post_id] = new_post

        self.post_id += 1
        return new_post
    
    def edit_post(self, post_id, edited_content):

        if post_id in self.posts:
            post = self.posts[post_id]
        else:
            print("Post não existe")
            return

        if not edited_content:
            print("Post não deve estar vazio")
            return

        post.edit_post(edited_content)


    def delete_post(self, post_id):

        if post_id in self.posts:
            self.posts.pop(post_id)
    
    def show_all_posts(self):

        for post_id in self.post_id:
            print(self.posts[post_id])

class Graph:

    def __init__(self):
        
        self.graph = {}

    def create_Usuario(self, nome, sobrenome = None):
        
        return Usuario(nome, sobrenome)

    def add_Usuario(self, nome, sobrenome = None):
                
        usuario = self.create_Usuario(nome, sobrenome)

        self.graph[Usuario.user_id] = usuario

        return usuario

    def add_list_Usuarios(self, list_of_usuario):

        for usuario in list_of_usuario:
            self.add_Usuario(usuario)

    def add_usuario_friend(self, usuario, new_friend):

        graph = self.graph


        if type(usuario) == int:
            if graph[usuario]:
                usuario = graph[usuario]
            else:
                print("Usuario alvo não existe")
        else:
            print("Impossivel achar usuario alvo")
            return
        
        if type(new_friend) == int:
            if graph[new_friend]:
                new_friend = graph[new_friend]
            else:
                print("Usuario amigo não existe")
        
        else:
            print("Impossivel buscar usuario amigo")
            return

        if usuario in graph and new_friend in graph:

            if new_friend not in graph[usuario].amigos:
                graph[usuario].amigos.append(new_friend)

            if usuario not in graph[new_friend].amigos:
                graph[new_friend].amigos.append(usuario)

    def add_usuario_block(self, usuario, new_block):

        graph = self.graph


        if type(usuario) == int:
            if graph[usuario]:
                usuario = graph[usuario]
            else:
                print("Usuario alvo não existe")
        else:
            print("Impossivel achar usuario alvo")
            return
        
        if type(new_block) == int:
            if graph[new_block]:
                new_block = graph[new_block]
            else:
                print("Usuario bloqueado não existe")
        
        else:
            print("Impossivel buscar usuario bloqueado")
            return

        if usuario in graph and new_block in graph:

            if new_block not in graph[usuario].bloqueados:
                graph[usuario].bloqueados.append(new_block)

            if usuario not in graph[new_block].bloqueados:
                graph[new_block].bloqueados.append(usuario)
    
    def print_amigos_usuario(self):

        graph = self.graph

        for usuario_id in graph:
            usuario = graph[usuario_id]
            print(f"Amigos do usuario {usuario.nome}:", ", ".join(map(str, usuario.amigos)), f"| Numero de usuarios amigos: {len(usuario.amigos)}")
        
        print(end="\n")
    
    def print_bloqueados_usuario(self):

        graph = self.graph

        for usuario_id in graph:
            usuario = graph[usuario_id]
            print(f"Usuarios bloqueados por {usuario.nome}:", ", ".join(map(str, usuario.bloqueados)), f"| Numero de usuarios bloquados: {len(usuario.bloqueados)}")
        
        print(end="\n")

    def create_new_post(self, usuario_id, conteudo_post):

        graph = self.graph

        usuario = graph[usuario_id]

        print(usuario.create_post(conteudo_post))
        


if __name__ == "__main__":

    franguinho = Graph()

    franguinho.add_Usuario("Marco")
    franguinho.add_Usuario("Aurelio")
    franguinho.add_Usuario("Roberto")
    franguinho.add_Usuario("Carlos")
    franguinho.add_Usuario("Tulio")

    # 1 M
    # 2 A
    # 3 R
    # 4 C
    # 5 T

    franguinho.add_usuario_friend(1, 4)
    franguinho.add_usuario_friend(4, 3)
    franguinho.add_usuario_friend(3, 2)
    franguinho.add_usuario_friend(3, 5)
    franguinho.add_usuario_friend(5, 1)

    franguinho.print_amigos_usuario()

    franguinho.add_usuario_block(1, 2)
    franguinho.add_usuario_block(1, 3)
    franguinho.add_usuario_block(2, 1)
    franguinho.add_usuario_block(2, 4)
    franguinho.add_usuario_block(2, 5)
    franguinho.add_usuario_block(3, 1)
    franguinho.add_usuario_block(5, 2)

    franguinho.print_bloqueados_usuario()

    franguinho.create_new_post(3, "Abc is a cool song!!!")


    # Hardcoded posts for user 0 (Marco)
    franguinho.create_new_post(5, "Marco postando algo interessante")
    franguinho.create_new_post(5, "O dia está ótimo para aprender!")
    franguinho.create_new_post(5, "Tem alguém mais aqui que ama pizza?")
    franguinho.create_new_post(5, "Café da manhã perfeito: pão e café!")
    franguinho.create_new_post(5, "Aprendendo Python todos os dias")

    # Hardcoded posts for user 1 (Aurelio)
    franguinho.create_new_post(1, "Aurelio está curtindo um filme legal")
    franguinho.create_new_post(1, "E aí, quem mais está ansioso para o fim de semana?")
    franguinho.create_new_post(1, "Hoje é dia de treino pesado")
    franguinho.create_new_post(1, "Dica de viagem: praia é tudo!")
    franguinho.create_new_post(1, "Preciso de dicas para melhorar meu projeto")

    # Hardcoded posts for user 2 (Roberto)
    franguinho.create_new_post(2, "Roberto postando sobre seu projeto de programação")
    franguinho.create_new_post(2, "Alguém já jogou aquele jogo novo?")
    franguinho.create_new_post(2, "Eu adoro a sensação de resolver um bug")
    franguinho.create_new_post(2, "O tempo está ótimo para uma caminhada")
    franguinho.create_new_post(2, "Quem mais é fã de música clássica?")

    # Hardcoded posts for user 3 (Carlos)
    franguinho.create_new_post(3, "Carlos está amando aprender novas linguagens")
    franguinho.create_new_post(3, "A melhor maneira de aprender é praticando")
    franguinho.create_new_post(3, "Alguém sabe como melhorar a performance em Python?")
    franguinho.create_new_post(3, "Dia de descanso, nada melhor!")
    franguinho.create_new_post(3, "Super empolgado para o projeto que vou começar")

    # Hardcoded posts for user 4 (Tulio)
    franguinho.create_new_post(4, "Tulio compartilhou um artigo interessante sobre IA")
    franguinho.create_new_post(4, "Aprender algo novo todos os dias!")
    franguinho.create_new_post(4, "Hoje é um ótimo dia para programar")
    franguinho.create_new_post(4, "Códigos limpos são códigos melhores!")
    franguinho.create_new_post(4, "Procurando dicas para otimizar o desempenho do meu app")
