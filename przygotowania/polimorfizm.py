class Figura:

    def oblicz_pole(self):
        pass

class Kwadrat(Figura):

    def __init__(self, bok):
        self.bok = bok

    def oblicz_pole(self):
        return self.bok * self.bok

class Trojkat(Figura):

    def __init__(self, a, h):
        self.a = a
        self.h = h

    def oblicz_pole(self):
        return 0.5 * self.a * self.h

figury = [Kwadrat(5), Trojkat(2, 3)]
sum = 0
for f in figury:
    sum += f.oblicz_pole()

print(sum)