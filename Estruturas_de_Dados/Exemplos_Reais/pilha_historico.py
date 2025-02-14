class Stack_Node:

    def __init__(self):
        self.next = None
    
class Return_Stack:

    def __init__(self):
        self.head = None
    
    def insert_stack(self, stack_node:Stack_Node):

        stack_node.next = self.head
        self.head = stack_node

    def pop_first(self) -> Stack_Node:

        returning_node = self.head
        self.head = self.head.next

        return returning_node

    def show_stack_contents(self):

        node = self.head
        stack_representation = []

        while node:
            stack_representation.append(node.nome)
            node = node.next
        
        while node:
            if node.next:
                print(f"{node.nome}", end=" <- ")
            else:
                print(f"{node.nome}")
            node = node.next
        
        print(" <- ".join(stack_representation))
        print(end="\n")

class Website(Stack_Node):
    def __init__(self, nome, funcao, endereco):
        super().__init__()
        self.nome = nome
        self.funcao = funcao
        self.endereco = endereco

google = Website("Google", "Search Engine", "https://www.google.com")
youtube = Website("YouTube", "Video Sharing Platform", "https://www.youtube.com")
github = Website("GitHub", "Code Hosting Platform", "https://www.github.com")
wikipedia = Website("Wikipedia", "Online Encyclopedia", "https://www.wikipedia.org")
reddit = Website("Reddit", "Social News and Discussion", "https://www.reddit.com")
amazon = Website("Amazon", "Online Shopping", "https://www.amazon.com")
stack_overflow = Website("Stack Overflow", "Programming Q&A", "https://stackoverflow.com")
netflix = Website("Netflix", "Streaming Service", "https://www.netflix.com")

return_stack = Return_Stack()

return_stack.show_stack_contents()

return_stack.insert_stack(google)

return_stack.show_stack_contents()

return_stack.insert_stack(youtube)

return_stack.show_stack_contents()

return_stack.insert_stack(github)

return_stack.show_stack_contents()

return_stack.pop_first()
return_stack.insert_stack(wikipedia)

return_stack.show_stack_contents()

return_stack.pop_first()
return_stack.pop_first()
return_stack.insert_stack(reddit)

return_stack.show_stack_contents()

return_stack.pop_first()
return_stack.insert_stack(amazon)
return_stack.insert_stack(stack_overflow)
return_stack.insert_stack(netflix)

return_stack.show_stack_contents()

return_stack.pop_first()

return_stack.show_stack_contents()