#------------------------------
# Message Class
#------------------------------

class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None
    
    def join_chatroom(self, chatroom):
        if self.chatroom:
            print(f"{self.username} is already in a chatroom.")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.username} joined the chatroom: {chatroom.name}")

    def leave_chatroom(self):
        if self.chatroom:
            self.chatroom.remove_user(self)
            print(f"{self.username} left the chatroom: {self.chatroom.name}")
            self.chatroom = None
        else:
            print(f"{self.username} is not in any chatroom.")

    def send_message(self, content):
        if not self.chatroom:
            print(f"{self.username} is not in any chatroom. Cannot send message.")
        else:
            self.chatroom.broadcast(self, content)  

    

class Message:
    message_counter = 1 #sample counter

    def __init__(self, sender: User, content: str):
        self.sender = sender
        self.content = content
        self.id = Message.message_counter
        Message.message_counter += 1   

    def __str__(self):
        return f"Message ID: {self.id}, From: {self.sender.username}, Content: {self.content}"  


class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = [] 
    
    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)
    
    def broadcast(self, sender, content):
        message = Message(sender, content)
        self.messages.append(message)
    
    def show_chat_history(self):
        print(f"\nChat history of {self.name}")
        for msg in self.messages:
            print(msg)
        print()

# Example usage:

if __name__ == "__main__":
    chatroom = ChatRoom("Python Lounge")
    
    user1 = User("Alice")
    user2 = User("Bob")
    user3 = User("Charlie")

    user1.join_chatroom(chatroom)
    user2.join_chatroom(chatroom)

    user1.send_message("Hello everyone!")
    user2.send_message("Hi Alice! How are you?")

    user3.join_chatroom(chatroom)
    user3.send_message("Hey folks, what's up?")

    chatroom.show_chat_history()

    user1.leave_chatroom()
    user2.leave_chatroom()  
    user3.leave_chatroom()  
