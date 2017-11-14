# -*- coding: utf-8 -*-

class Box(object):

    def __init__(self, color):
        self._color = color
        self._fruits = {}

    def __repr__(self):
        fmt = "Box(color: {}, fruits: {})"
        return fmt.format(self._color, self._fruits)

    def set_fruites(self, fruits={}):
        """
        Put the fruits to the box
        :param fruits:
        return
        """
        assert (type(fruits) is dict), "Fruit must be '{type : nums}'"
        self._fruits.update(fruits)

        if


    def get_fruites(self, fruits):
        """

        """
        self._fruits.remove(fruits)
