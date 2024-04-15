#!/usr/bin/python3
"""Mylist subclass defination"""


class Mylist(list):
    def print_sorted(self):
        """print_sorted - sort all element in the list and print the result out
            self: get the list from the Base class
        """
        pass
        for i in range(len(self.my_list)):
            for j in range(1, len(self.my_list)):
                if self.my_list[i] > self.my_list[j]:
                    self.my_list[i] = self.my_list[i] ^ self.my_list[j]
                    self.my_list[j] = self.my_list[i] ^ self.my_list[j]
                    self.my_list[i] = self.my_list[i] ^ self.my_list[j]
                else:
                    continue
        print(self.my_list)
