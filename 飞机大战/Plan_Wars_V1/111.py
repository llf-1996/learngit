class A:
    def __init__(self):
        #print(super())
        print("Enter A")
        print("Leave A")

    def show(self):
        print('a  show')

class B(A):
    def __init__(self):
        print("Enter B")
        #print(super())
        super().__init__()
        print("Leave B")
    def show(self):
        print('b  show')

# single = B()
# print(B.mro())
class C():
    def __init__(self):
        print("Enter C")
        print(super())
        super().__init__()
        print("Leave C")
    # def show(self):
    #     print('c  show')


class D(C, B):
    def __init__(self):
        print("Enter D")
        print(super())
        super().__init__()
        print("Leave D")
    def show(self):
        print('d  show')

d = D()
d.show()
print(D.mro())