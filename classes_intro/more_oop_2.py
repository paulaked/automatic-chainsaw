from more_oop import A

class B(A):
    def __init__(self):
        super().__init__()
        self.class_attribute = "this is class b"

    def class_b_method(self):
        return "this is class b method"

if __name__ == '__main__':
    print("Running more_oop_2 :" + __name__)