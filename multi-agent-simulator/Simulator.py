import Market
import Person
import Product

class Simulator:
    '''
    a Simple Multi-agent Simulator
    the Simulator has a Market, People, and a Product
    the Simulator reads parameter settings from YAML file.
    '''

    def __init__(self, params):
        advertisingBudget = params['AdvertisingBudget']
        marketNPS = params['MarketNPS']
        self.product = Product.Product(advertisingBudget)
        self.market = Market.Market(self.product, marketNPS)

        self.population = params['Population']
        self.innovators = int(self.population * params['Innovators'])
        self.earlyAdopters = self.population - self.innovators
        purchaseProbability = params['PurchaseProbability']
        coefAdvertise = params['CoefficiencyOfAdvertisement']
        coefNPS = params['CoefficiencyOfNPS']
        self.people = [Person.Innovator(self.market, self.product, purchaseProbability) for i in range(self.innovators)] + [Person.EarlyAdopter(self.market, self.product, coefNPS, coefAdvertise) for i in range(self.earlyAdopters)]
        self.market.people = self.people

    def __str__(self):
        return "People: [Innovators: {0}, Early Adopters: {1}]".format(str(self.innovators), str(self.earlyAdopters))
    
    def run(self, step):
        print("step,total,innovator,earlyAdopter")
        for i in range(step):
            self.market.purchase()
            print("{0},{1},{2},{3}".format(i, self.market.totalSales(), self.market.innovatorSales(), self.market.earlyAdopterSales()))
