import weakref

class ObjectPlus:

    extents = []

    def __init__(self):
        ObjectPlus.extents.append(weakref.proxy(self))

