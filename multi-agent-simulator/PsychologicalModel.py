import random
from math import tanh

class AbstractModel():
    '''
    this class provides an abstract model of person's psychological model to decide whether to buy a product.
    '''

    def __init__(self, market, product):
        self.market = market
        self.product = product

    def purchaseProbability(self):
        pass
    
class SimpleInnovatorModel(AbstractModel):
    '''
    Innovators purchase a product with a certain probability (free parameter).
    '''
    def __init__(self, market, product, purchaseProbability):
        self.__purchaseProbability = purchaseProbability

    def purchaseProbability(self):
        return self.__purchaseProbability
        
class SimpleEarlyAdopterModel(AbstractModel):
    '''
    Early Adopters decide to purchase based on advertisement and market NPS score. 
    '''
    def __init__(self, market, product, coefNPS, coefAdvertise):
        self.market = market
        self.product = product
        self.coefNPS = coefNPS
        self.coefAdvertise = coefAdvertise

    def purchaseProbability(self):
        return tanh(self.coefNPS * self.market.NPS + self.coefAdvertise * self.product.advertise())