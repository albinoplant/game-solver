import itertools


class Flask:
    id_iter = itertools.count()

    def __init__(self, initial=None):
        if initial is None:
            initial = [0, 0, 0, 0]
        self.id = next(self.id_iter)
        self.container = initial

    def __getitem__(self, key):
        return self.container[key]

    def __setitem__(self, key, value):
        self.container[key] = value

    @property
    def container(self):
        return self.__container

    @container.setter
    def container(self, val):
        self.__container = val

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, val):
        self.__id = val

    def is_empty(self):
        return self.container[0] == 0

    def empty_last(self, index=None):
        if self.is_empty():
            return
        if index is not None and self.container[index] != 0:
            to_return = self.container[index]
            self.container[index] = 0
            return to_return
        else:
            for i in range(4)[::-1]:
                if self.container[i] != 0:
                    to_return = self.container[i]
                    self.container[i] = 0
                    return to_return

    def is_full(self):
        return self.container[3] != 0

    def get_last_index(self):
        for i in range(4)[::-1]:
            if self.container[i] != 0:
                return i
        return -1
