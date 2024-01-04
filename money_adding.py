class Money:
    def __init__(self):

        self.cost = 0

    def adding(self, amount):
        self.cost += amount
        return self.cost

    def __str__(self):
        return f'${self.cost:.2f}'
  