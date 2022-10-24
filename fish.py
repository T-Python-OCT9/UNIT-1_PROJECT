class fish:

    def __init__(self, name, deep, weight, quality, price):
        self.name = name
        self.deep = deep
        self.weight = weight
        self.quality = quality
        self.price = price

    def getName(self):
        return self.name

    def getDeep(self):
        return self.deep

    def getweight(self):
        return self.weight

    def getQuality(self):
        return self.quality

    def getprice(self):
        return self.price

    def fishReport(self):
        massge = "\nFish name: " + self.getName() + " live in Deepth of " + self.getDeep()+ " m weight is: " + self.getweight() + "Kg the qauality is: " + self.getQuality() + " the price is: " + self.getprice()+"\n"
        return massge