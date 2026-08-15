from threading import Semaphore

class Foo:
    def __init__(self):
        self.secondSemaphore = Semaphore(0)
        self.thirdSemaphore = Semaphore(0)

    def first(self, printFirst):
        printFirst()
        self.secondSemaphore.release()

    def second(self, printSecond):
        self.secondSemaphore.acquire()
        printSecond()
        self.thirdSemaphore.release()

    def third(self, printThird):
        self.thirdSemaphore.acquire()
        printThird()