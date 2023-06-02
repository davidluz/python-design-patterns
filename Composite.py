class Component:
    def __init__(self, name):
        self._name = name

    def component_function(self):
        print(f"{self._name}")

class Composite(Component):
    def __init__(self, name):
        Component.__init__(self, name)
        self._children = []

    def add(self, child):
        self._children.append(child)

    def component_function(self):
        print(f"{self._name}")
        for i in self._children:
            i.component_function()

sub1 = Composite("submenu1")
sub11 = Component("sub_submenu11")
sub12 = Component("sub_submenu12")

sub1.add(sub11)
sub1.add(sub12)

top = Composite("top_menu")

top.add(sub1)

top.component_function()  
