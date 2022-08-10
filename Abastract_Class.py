from abc import ABC,abstractclassmethod
#abstract class it has not defination


class computer(ABC):
    @abstractclassmethod
    def process(self):
        pass

class laptop(computer):
    def process(self,com):
        print('its running')
        

class whiteboard(computer):
    def write(self):
        print('its writing')

class programmer:
    def work(self,com):
        print('solving bugs')
        com.procces()

#com=computer()

#com.process()
com1=laptop()
prog1=programmer()
white=whiteboard

com1.process()
prog1.work(com1)

