import itertools
from typing import List


class Flask:
    id_iter = itertools.count()

    def __init__(self, initial=None):
        if initial is None:
            initial = [0, 0, 0, 0]
        self.id = next(self.id_iter)
        self.container = initial

    def __getitem__(self, key) -> int:
        return self.container[key]

    def __setitem__(self, key, value) -> None:
        self.container[key] = value

    @property
    def container(self) -> List[int]:
        return self.__container

    @container.setter
    def container(self, val) -> None:
        self.__container = val

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, val) -> None:
        self.__id = val

    def is_empty(self) -> bool:
        return self.container[0] == 0

    def empty_last(self, index=None) -> int or None:
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

    def is_full(self) -> bool:
        return self.container[3] != 0

    def pour_to(self, to_flask: 'Flask', self_last_index=None, to_flask_last_index=None) -> None:
        to_index = to_flask.get_last_index() + 1 if to_flask_last_index is None else to_flask_last_index
        if to_index == 4:
            return
        to_flask[to_index] = self.empty_last(self_last_index)

    def get_last_index(self) -> int:
        for i in range(4)[::-1]:
            if self.container[i] != 0:
                return i
        return -1
