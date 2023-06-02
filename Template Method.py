from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self):
        self._step1()
        self._step2()
        self._step3()

    @abstractmethod
    def _step1(self):
        pass

    @abstractmethod
    def _step2(self):
        pass

    @abstractmethod
    def _step3(self):
        pass

class ConcreteClass(AbstractClass):
    def _step1(self):
        print("Step 1")

    def _step2(self):
        print("Step 2")

    def _step3(self):
        print("Step 3")

concrete = ConcreteClass()
concrete.template_method()  # Step 1\nStep 2\nStep 3
