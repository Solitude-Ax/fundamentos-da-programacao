class Queue_Node:

    def __init__(self, data):
        
        self.data = data
        self.next = None

class Notification(Queue_Node):
    
    def __init__(self, data:str, type_notification = "system", time_sent = "00:00"):
        super().__init__(data)
        self.type_notification = type_notification or "system"
        self.time_sent = time_sent or "00:00"

class Queue:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_queue(self, notification_data:str, type_notification:str = None, time_sent:str = None):

        if type(notification_data) == str or type(notification_data) == int:
            notification_node = Notification(notification_data, type_notification, time_sent)
        elif type(notification_node) != Notification:
            return
        
        if not self.head:
            self.head = self.tail = notification_node
            return
        
        self.tail.next = notification_node
        self.tail = self.tail.next

        #head exits (first entry)
        #tail enters (last entry)

    def pop_head(self) -> Queue_Node:

        returning_node = self.head
        self.head = self.head.next

        return returning_node
        #return returning_node.data

    def show_queue_contents(self):

        node = self.head
        queue_representation = []

        while node:
            queue_representation.append(str(node.data))
            node = node.next
        
        print(" -> ".join(queue_representation))
        print(end="\n")

class Notification_Bar(Queue):

    def __init__(self):
        super().__init__()
    
    def send_notifications(self):
        
        while self.head:
            notification = self.pop_head()
            print(f"Nova notificação!\n\n{notification.data}\nHorário enviado: {notification.time_sent} | Tipo de notificação: {notification.type_notification}\n")

noti_bar = Notification_Bar()

noti_bar.insert_queue("Gatinha_123 mandou uma mensagem", "Redes Sociais", "12:37")
noti_bar.insert_queue("Banana prata está em promoção! Venha aproveitar agora.", "Mercado", "9:48")
noti_bar.insert_queue("Mãe: Já comprasse a ração do cachorro?", "Mercado", "14:05")
noti_bar.insert_queue("Netflix: Nova temporada de sua série favorita está disponível!", "Entretenimento", "8:15")
noti_bar.insert_queue("Seu pacote foi entregue!", "Compras Online", "10:30")
noti_bar.insert_queue("Alerta de chuva forte na sua região. Tome cuidado!", "Clima", "17:00")
noti_bar.insert_queue("Gasolina subiu novamente! Confira os preços na sua região.", "Notícias", "12:10")
noti_bar.insert_queue("Pai: Leva o carro para lavar, por favor.", "Tarefas", "08:50")


noti_bar.show_queue_contents()
noti_bar.send_notifications()
noti_bar.show_queue_contents()
noti_bar.insert_queue("abc")
noti_bar.show_queue_contents()