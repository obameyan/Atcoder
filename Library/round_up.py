# a/b の切り上げ
def round_up(a, b):
    """ a/b の切り上げ """
    c = (a + b - 1) / b
    return c


def floor(a, b):
    """floor(a/b) 整数値を返す"""
    c = (a - a % b)/b
    return c
