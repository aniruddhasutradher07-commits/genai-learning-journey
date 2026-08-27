from threading import Lock

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_lock = Lock()
        self.bar_lock = Lock()
        self.bar_lock.acquire()

    def foo(self, printFoo):
        for _ in range(self.n):
            self.foo_lock.acquire()
            printFoo()
            self.bar_lock.release()

    def bar(self, printBar):
        for _ in range(self.n):
            self.bar_lock.acquire()
            printBar()
            self.foo_lock.release()