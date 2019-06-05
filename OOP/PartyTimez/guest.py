class Guest:
    def __init__(self, name, importance):
        self.name = name
        # 1 - 5
        self.importance = importance

    def __repr__(self):
        return f"Name: {self.name}, Importance: {self.importance}"

dummy = Guest("Devon", 1)
print(dummy)