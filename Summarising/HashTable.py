from Summarising.referential_array import build_array
import numpy


class HashTable:
    def __init__(self, tablesize=399989):
        self.table_size = tablesize
        self.count = 0
        self.array = build_array(self.table_size)
        self.max = 0

    def hash_value(self, key):
        '''
        Computes the hash value

        :param key:
        :return h:
        :complexity O(len(key)) or O(k) however if where assuming the the words are not extremely long
          it can be be be computed to O(K)
        '''
        a = 101
        h = 0
        for c in str(key):
            h = (h * a + ord(c)) % self.table_size
        return h

    def __len__(self):
        return self.count

    def __setitem__(self, key, value):
        '''

        :param key:
        :param value:
        :complexity O(k) and worst O(N**2) if reset
        :return:
        '''
        start = self.hash_value(key)
        for offset in range(self.table_size):
            position = start + offset ** 2  # quadratic step
            if self.array[position] is None:
                self.array[position] = [key, value]
                return
            elif self.array[position][0] == key:
                self.array[position][1] = value
                return
                # Rehash
        self.rehash()
        self.__setitem__(key, value)

    def __getitem__(self, key):
        '''

        :param key:
        :return: O(N)
        '''
        start = self.hash_value(key)
        for offset in range(self.table_size):
            position = start + offset ** 2  # quadratic step
            if self.array[position] is None:
                return None
            if self.array[position][0] == key:
                return self.array[position][1]
                # raise KeyError("Key not found")
        return None

    def reset(self, tablesize):
        self.__init__(tablesize)

    def list_count(self):
        counter = []
        for i in range(self.table_size):
            if self.array[i] is not None:
                counter.append(self.array[i][1])
        return counter

    def rehash(self):
        '''
        o(N**2)
        :return:
        '''
        # Double all items

        new = HashTable(self.table_size * 2)
        for i in range(self.table_size):
            if self.array[i] is not None:
                item = self.array[i][0]
                value = self.array[i][1]
                new[item] = value
        self.reset(self.table_size * 2)
        for i in range(self.table_size * 2):
            if new.array[i] is not None:
                item = new.array[i][0]
                value = new.array[i][1]
                self.array[item] = value
                # Finished copying

    def __str__(self):
        ret = ""
        for i in range(self.table_size):
            if self.array[i] is not None:
                ret += self.array[i][0] + " repeated " + str(self.array[i][1]) + " times\n "
        return ret

    def word_barrier(self):
        lister = numpy.array(self.list_count())
        barrier = numpy.mean(lister, axis=0) + numpy.std(lister, axis=0)
        word_list = []
        for i in range(self.table_size):
            if self.array[i] is not None:
                if self.array[i][1] > barrier and len(self.array[i][0]) > 3:
                    word_list.append(self.array[i][0])
        return word_list
