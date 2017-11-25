# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 20:58:30 2017

@author: Sooyong Lee
@commenter_1: Seungbae Ji
"""

from enum import Enum


class Box(object):
    def __init__(self, color, prob):
        self.color = color
        self.prob = prob
        self.num_item = [0] * 4

    # public method
    def insert_item(self, type, num):
        self.num_item.insert(type, num)

    # public method
    def get_item_num(self, type):
        return self.num_item[type]

    # public method
    def get_total_items(self):
        self.sum = 0
        for num in self.num_item:
            self.sum += num
        return self.sum


class ProbabilityCalculator(object):
    def __init__(self, Boxes):
        self.boxes = Boxes

    # public method
    def get_item_probability(self, item_type):
        self.item_prob = 0.0
        for box in self.boxes:
            self.item_prob += (box.get_item_num(item_type) /
                               box.get_total_items()) * box.prob

        return self.item_prob

    # public method
    def get_conditional_probability_given_item(self, box, item_type):
        self.prob_item_box = box.get_item_num(
            item_type) / box.get_total_items()
        self.prob_item = self.get_item_probability(item_type)

        return (self.prob_item_box * box.prob) / self.prob_item


"""
Commenter_1: Seungbae Ji

Naming
1. Python 문서 일부에서 under score(_)를 속성명 앞에 붙이는 것을 protected attribute로 부룸.
2. 하지만 실제로 Python에서 보호해 주지는 않음. 이는 개발자들이 보편적으로 따르는 관례.
3. 클래스 외부에서 _가 붙은 속성에 접근하지 않는 것은 파이썬 프로그래머 사이에서 일종의 금기.
REF. Fluent Python


Under score
1. 인터프리터(Interpreter)에서 마지막 값을 저장할 때
2. 값을 무시하고 싶을 때 (흔히 “I don’t care”라고 부른다.)
3. 변수나 함수명에 특별한 의미 또는 기능을 부여하고자 할 때
4. 국제화(Internationalization, i18n)/지역화(Localization, l10n) 함수로써 사용할 때
5. 숫자 리터럴값의 자릿수 구분을 위한 구분자로써 사용할 때
REF.https://mingrammer.com/underscore-in-python

import 대비.
1. Python에서 import를 하게되면, import한 파일을 전체적으로 실행.
2. Python의 파일은
Python에서는 indent로 파일의 우선순위를 결정하여 읽어들임.
REF. https://stackoverflow.com/questions/419163/what-does-if-name-main-do

기타.
1. PEP8에서는 space 4개로 indentation level이 결정된다고 규정.
2. space bar와 tab과는 구분되며, tab은 사이즈 변경이 가능해서 space bar와 섞어 사용하면 안됨.
3. Pycharm에서는 tab을 space 4개로 자동 변경해 주는 기능을 적용.
4. Atom과 Spyder에서 제공하는지는 확인이 필요(다음주 확인해 오겠음)
REF. https://www.python.org/dev/peps/pep-0008/
"""

if __name__ is "__main__":
    red_box = Box("red", 0.2)
    blue_box = Box("blue", 0.2)
    green_box = Box("green", 0.6)

    Item = Enum('Item', 'apple, orange, lime')

    red_box.insert_item(Item.apple.value, 3)
    blue_box.insert_item(Item.apple.value, 1)
    green_box.insert_item(Item.apple.value, 3)
    red_box.insert_item(Item.orange.value, 4)
    blue_box.insert_item(Item.orange.value, 1)
    green_box.insert_item(Item.orange.value, 3)
    red_box.insert_item(Item.lime.value, 3)
    blue_box.insert_item(Item.lime.value, 0)
    green_box.insert_item(Item.lime.value, 4)

    Boxes = []
    Boxes.append(red_box)
    Boxes.append(blue_box)
    Boxes.append(green_box)

    calculator = ProbabilityCalculator(Boxes)
    print("Probability of selecting an apple: %f" %
          calculator.get_item_probability(Item.apple.value))
    print("Probability that an item is from green box given the item is orange: %f"
          % calculator.get_conditional_probability_given_item(green_box, Item.orange.value))
