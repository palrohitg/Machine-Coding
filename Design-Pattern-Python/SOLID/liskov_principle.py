# Liskov principle states that the child classes can be subsitute in place of the parent
# Parent Classes. 

#abstract methods which has the implementation of the other methods
from abc import ABC, abstractmethod 


class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass 
    
class Email(Notification):
    
    def __init__(self, email=None):
        self.email = email 
        
    def notify(self, message):
        print(f'Send "{message}" to {self.email}')


def SMS(Notification):
    
    def __init__(self, phone):
        self.phone = phone
        
    def notify(self, message):
        print(f'Send "{message}" to {self.phone}')
        
class Contact:
    
    def __init__(self, name, email, phone):
        self.name = name 
        self.email = email
        self.phone = phone
        

class NotificationMananger:
    
    def __init__(self, notification) -> None:
        self.notification = notification
        
    def send(self, message):
        self.notification.notify(message)
        
        
if __name__ == '__main__':
    contact = Contact("vikas", "vikas.@gmail.com", "124142141")
    
    sms_notification = SMS(contact.phone)
    email_notification = Email(contact.email)
    
    notification_manager = NotificationMananger(sms_notification)
    notification_manager.send("vikas hello") 
    
    notification_manager.notification = email_notification
    notification_manager.send("Hey John")