# -*- coding: utf-8 -*-


class Box(object):

    def __init__(self, color):
        self._color = color
        self._fruits = {}

    def __repr__(self):
        fmt = "Box(color: {}, fruits: {})"
        return fmt.format(self._color, self._fruits)

    def set_fruites(self, fruits={}):
        assert (type(fruits) is dict), "Fruit must be '{type : nums}'"
        self._fruits.update(fruits)
        return self._fruits


class Statistician(object):

    def __init__(self, boxes=[], probs=[]):
        assert (type(boxes) is list), "Boxes must be '[Box(1), Box(2), ...]'"
        assert (type(probs) is list), "probs must be '[prob of Box(1), prob of Box(2), ...]'"
        assert len(boxes) == len(probs)
        self._boxes = boxes
        self._probs = probs

    def __repr__(self):
        _info = [str(box) + "'s prob is " + str(prob)
                 for box, prob in zip(self._boxes, self._probs)]
        fmt = "Statistician({})"
        return fmt.format(_info)

    def calculate_prob(self, cate_prob):
        return None
