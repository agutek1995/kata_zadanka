
class Punkt:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def opisz_mnie(self):
        print(f"jest punktem o współrzędnych: x = {self.x}, y = {self.y}")

p1 = Punkt(2, 6)
p2 = Punkt(3, 4)

p1.opisz_mnie()
p2.opisz_mnie()