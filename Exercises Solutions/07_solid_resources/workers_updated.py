from abc import ABC, abstractmethod
import time


class Work:
    @abstractmethod
    def work(self):
        pass


class Eat:
    @abstractmethod
    def eat(self):
        pass


class Worker(Work, Eat):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Work, Eat):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(Work):

    def work(self):
        print("I'm a robot. I'm working....")


class Manager:

    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        pass


class WorkManager:

    def set_worker(self, worker):
        assert isinstance(worker, Work), f"`worker` must be of type {Work}"

        self.worker = worker

    def manage(self):
        self.worker.work()


class BreakManager(Manager):

    def set_worker(self, worker):
        assert isinstance(worker, Eat), f"`worker` must be of type {Eat}"

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")


