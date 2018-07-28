from abc import ABCMeata, abstractmethod

class Person(metaclass=ABCMeata):
    '''
    Person class is abstract class.
    this expands to Innovator and EarlyAdopter class.
    According "Diffusion of innovations" theory,
    People divided into 5 categories.
    Innovators, Early Adopters, Early Majority, Late Majority, Laggards
    This abstract class provides psychological model of Innovators and Early Adopters,
    and calculate purchase probability and the NPS score after purchase.
    '''

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def purchase(self):
        pass

    @abstractmethod
    def NPS(self):
        pass

class Innovator(Person):
    '''
    Innovators purchase a product with a certain probability.
    After purchase, they send a NPS score.
    '''

    def __init__(self):
        pass

    def __str__(self):
        pass

    def NPS(self):
        pass
    
    def purchase(self):
        pass

class EarlyAdopter(Person):
    '''

    '''
    def __init__(self):
        pass

    def __str__(self):
        pass

    def NPS(self):
        pass