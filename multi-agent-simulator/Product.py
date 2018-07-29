class Product:
    '''
    Product class provides People advertise.
    this also provides purchasers product satisfaction.
    product satisfaction increases NPS score of purchasers.
    '''

    def __init__(self, advertisingBudget):
        self.advertisingBudget = advertisingBudget
    
    def __str__(self):
        pass
    
    def advertise(self):
        return self.advertisingBudget
    