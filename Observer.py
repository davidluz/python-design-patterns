class Observer:
    def update(self, subject):
        print('Observer: Subject {} has data {}'.format(subject.name, subject.data))

class Subject:
    def __init__(self, name):
        self._observers = []
        self._name = name
        self._data = 0

    @property
    def name(self):
        return self._name

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

subject = Subject("Subject1")
observer = Observer()

subject.attach(observer)
subject.data = 123  # Observer: Subject Subject1 has data 123

