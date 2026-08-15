from threading import Semaphore

class H2O:
    def __init__(self):
        self.hydrogenSemaphore = Semaphore(2)
        self.oxygenSemaphore = Semaphore(0)
        self.count = 0
        self.countLock = Semaphore(1)

    def hydrogen(self, releaseHydrogen):
        self.hydrogenSemaphore.acquire()
        releaseHydrogen()
        self.countLock.acquire()
        self.count += 1
        if self.count == 2:
            self.count = 0
            self.oxygenSemaphore.release()
        self.countLock.release()

    def oxygen(self, releaseOxygen):
        self.oxygenSemaphore.acquire()
        releaseOxygen()
        self.hydrogenSemaphore.release()
        self.hydrogenSemaphore.release()