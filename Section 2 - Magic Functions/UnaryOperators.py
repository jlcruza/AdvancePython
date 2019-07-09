class x:
    def __init__(self, y):
        self.y = y

    def __neg__(self):
        return self.y

    def __pos__(self):
        return self.y

    def __invert__(self):
        return self.y


if __name__ == "__main__":
    obj1 = x(-2)
    print(-obj1.y)
    print(+obj1.y)
    print(~obj1.y)