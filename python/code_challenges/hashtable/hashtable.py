from code_challenges.linked_list.linked_list import Linked_List

class Hashtable:
    def __init__(self, size=1024):
        self._size = size
        self._tables = [None] * size

    def hash(self, key):
        index = 0
        for char in key:
            index += ord(char)
        index *= 599
        index = index % self._size
        return index

    def set(self, key, value):
        index = self.hash(key)
        table = self._tables[index]
        if table is None:
            table = Linked_List()
            self._tables[index] = table
        current = table.head

        while current:
            candidate_leg = current.data
            if candidate_leg[0] == key:
                candidate_leg[1] = value
                return
            current = current.next

        leg = [key, value]
        table.insert(leg)

    def get(self, key):
        index = self.hash(key)
        table = self._tables[index]
        if table is not None:
            current = table.head
            while current:
                candidate_leg = current.data
                if candidate_leg[0] == key:
                    return candidate_leg[1]
                current = current.next
        raise KeyError(f"Key '{key}' not found in the hashtable.")

    def has(self, key):
        index = self.hash(key)
        table = self._tables[index]
        if table is not None:
            current = table.head
            while current:
                if current.data[0] == key:
                    return True
                current = current.next
        return False

    def keys(self):
        all_keys = []
        for table in self._tables:
            if table is not None:
                current = table.head
                while current:
                    all_keys.append(current.data[0])
                    current = current.next
        return all_keys