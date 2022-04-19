def incrementor(stride: int):
    def f(x: int):
        return x + stride

    return f
