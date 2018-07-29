class Market:
    '''
    Market class has People and a Product
    the Market accumulate Product's sales and NPS score.

    '''

    def __init__(self, product, marketNPS):
        self.product = product
        self.people = []
        self.NPS = marketNPS

    def __str__(self):
        pass

    def purchase(self):
        for p in self.people:
            p.purchase()
        
    def totalSales(self):
        return len([p for p in self.people if p.purchased == True])

    def innovatorSales(self):
        return len([p for p in self.people if p.purchased == True and p.__class__.__name__ == 'Innovator'])

    def earlyAdopterSales(self):
        return len([p for p in self.people if p.purchased == True and p.__class__.__name__ == 'EarlyAdopter'])

    def setNPS(self):
        respondents = 0
        promoters = 0
        detractors = 0
        for p in self.people:
            respondents += 1 if p.NPS is not None else 0
            promoters += 1 if p.NPS is not None and p.NPS >= 8 else 0
            detractors += 1 if p.NPS is not None and p.NPS <= 3 else 0
        
        self.NPS = (promoters - detractors) / respondents
