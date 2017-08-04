import numpy as np
import matplotlib.pyplot as plt

class drink:
    def __init__(self, name, color, temperature):
        self.name = name
        self.color = color
        self.temperature = temperature

    def shoutout(self):
        print "I love", self.name, "!"


chicha = drink('chicha', 'purple', 'cold')
chicha.shoutout()


class beverage(drink):
    def shoutout(self):
        print self.name, "is too cold!"


coke = beverage('coke', 'dark', 'cold')
coke.shoutout()
