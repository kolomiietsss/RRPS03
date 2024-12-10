class Strategy:
    def execute(self, data):
        pass

class StrategyA(Strategy):
    def execute(self, data):
        return sorted(data)

class StrategyB(Strategy):
    def execute(self, data):
        return sorted(data, reverse=True)

class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute_strategy(self, data):
        return self._strategy.execute(data)

# Приклад використання
data = [5, 2, 9, 1]
context = Context(StrategyA())
print(context.execute_strategy(data))  # [1, 2, 5, 9]

context.set_strategy(StrategyB())
print(context.execute_strategy(data))  # [9, 5, 2, 1]
