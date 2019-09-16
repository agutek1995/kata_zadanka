class Figura():

    def pole(self):
        pass

class Kwadrat(Figura):

    def __init__(self,a):
        self.a=a

    def pole(self):
        return self.a**2

k=Kwadrat(5)
print(k.pole())