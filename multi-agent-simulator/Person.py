import random

from PsychologicalModel import AbstractModel,SimpleInnovatorModel,SimpleEarlyAdopterModel

class Person():
    '''
    Person class is abstract class.
    this expands to Innovator and EarlyAdopter class.
    According "Diffusion of innovations" theory,
    People divided into 5 categories.
    Innovators, Early Adopters, Early Majority, Late Majority, Laggards
    This abstract class provides psychological model of Innovators and Early Adopters,
    and calculate purchase probability and the NPS score after purchase.
    '''

    def __init__(self, market, product):
        self.psyModel = AbstractModel(market, product)
        self.purchased = False
        self.NPS = None

    def __str__(self):
        "Class: " + self.__class__.__name__ + ", Model Class: " + self.psyModel.__class__.__name__ + ", purchased: " + self.purchased + ", NPS: " + self.NPS

    def purchase(self):
        if random.random() <= self.psyModel.purchaseProbability():
            self.purchased = True
            self.setNPS()


    def setNPS(self):
        if self.purchased == True:
            self.NPS = random.randint(0, 10)
        else:
            self.NPS = None

class Innovator(Person):
    '''
    Innovators purchase a product with a certain probability(free parameter).
    '''
    def __init__(self, market, product, purchaseProbability):
        self.psyModel = SimpleInnovatorModel(market, product, purchaseProbability)
        self.purchased = False
        self.NPS = None
                    
class EarlyAdopter(Person):
    '''
    Early Adopters do not purchase immediately. 
    They decide whether to purchase with reference to the market evaluation and product advertisement.
    '''
    def __init__(self, market, product, coefNPS, coefAdvertise):
        self.psyModel = SimpleEarlyAdopterModel(market, product, coefNPS, coefAdvertise)
        self.purchased = False
        self.NPS = None
