class Iterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def __next__(self):
        if self.index < len(self.collection):
            result = self.collection[self.index]
            self.index += 1
            return result
        raise StopIteration

class Collection:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __iter__(self):
        return Iterator(self.items)

collection = Collection()
collection.add("Item 1")
collection.add("Item 2")
collection.add("Item 3")

for item in collection:
    print(item)  # Item 1\nItem 2\nItem 3
