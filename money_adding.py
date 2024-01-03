class Money:
    def __init__(self, cost):
        self.cost = cost

    def adding(self, amount):
        self.cost += amount
        return self.cost

