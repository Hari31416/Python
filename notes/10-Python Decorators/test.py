def func1(func):
    def wrap_func():
        print("Hello There")

        func()

        print("How Civilised")

    return wrap_func


def func2():
    print("General Kenobi")


func2 = func1(func2)
func2()
