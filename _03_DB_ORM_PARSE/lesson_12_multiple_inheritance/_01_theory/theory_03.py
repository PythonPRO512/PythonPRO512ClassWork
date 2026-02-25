"""
Проблема ромбов при множественном наследовании
"""


class A:
    def __init__(self):
        print(f'class - A')


class B(A):
    def __init__(self):
        print(f'class - B from')
        super().__init__()


class C(A):
    def __init__(self):
        print(f'class - C from')
        super().__init__()


# class D(C, A):
#     def __init__(self):
#         print('class D from: ')
#         super().__init__()

# class D(A, C):
#     def __init__(self):
#         print('class D from: ')
#         super().__init__()

# class D(B, C):
#     def __init__(self):
#         print('class D from: ')
#         super().__init__()

class DB(B):
    def __init__(self):
        print('class DB from')
        super().__init__()


if __name__ == '__main__':
    # d = D()
    db = DB()