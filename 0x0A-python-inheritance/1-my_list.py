#!/usr/bin/python3
"""Mylist subclass defination"""


class Mylist(list):
    def print_sorted(self):
        """print_sorted - sort all element in the list and print the result out
            self: get the list from the Base class
        """
        pass
        for i in range(len(self.list)):
            for j in range(1, len(self.list)):
                if self.list[i] > self.list[j]:
                    self.list[i] = self.list[i] ^ self.list[j]
                    self.list[j] = self.list[i] ^ self.list[j]
                    self.list[i] = self.list[i] ^ self.list[j]
                else:
                    continue
        print(self.my_list)
