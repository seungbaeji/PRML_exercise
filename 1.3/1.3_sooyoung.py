# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 20:58:30 2017

@author: Sooyong Lee
"""

from enum import Enum

class Box(object):
    def __init__(self, color, prob):
        self.color = color
        self.prob = prob
        self.num_item = [0] * 4

    def insert_item(self, type, num):
        self.num_item.insert(type, num)

    def get_item_num(self, type):
        return self.num_item[type]
    
    def get_total_items(self):
        self.sum = 0
        for num in self.num_item:
            self.sum += num
        return self.sum

class ProbabilityCalculator(object):
    def __init__(self, Boxes):
        self.boxes = Boxes
        
    def get_item_probability(self, item_type):
        
        self.item_prob = 0.0
        for box in self.boxes:
            self.item_prob += (box.get_item_num(item_type)/box.get_total_items())*box.prob

        return self.item_prob

    def get_conditional_probability_given_item(self, box, item_type):
        self.prob_item_box = box.get_item_num(item_type)/box.get_total_items()
        self.prob_item = self.get_item_probability(item_type)
        
        return (self.prob_item_box*box.prob)/self.prob_item

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
print("Probability of selecting an apple: %f" % calculator.get_item_probability(Item.apple.value))
print("Probability that an item is from green box given the item is orange: %f" 
      % calculator.get_conditional_probability_given_item(green_box, Item.orange.value) )