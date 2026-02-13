class Aritmetica:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self):
        return self.x + self.y

    def res(self):
        return self.x - self.y

    def mul(self):
        return self.x * self.y

    def div(self):
        return self.x / self.y

    def todo(self):
        print(f"El resultado de la suma: {self.sum()}")
        print(f"El resultado de la resta: {self.res()}")
        print(f"El resultado de la multiplicacion: {self.mul()}")
        print(f"El resultado de la division: {self.div()}")


if __name__ == "__main__":
    aritmetica1 = Aritmetica(5, 4)
    aritmetica1.todo()
