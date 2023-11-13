from player import playerclass


class templateField:
    def __init__(self):
        self.price = 10000
        self.rent = 500
        self.houseRentMultiplier = 1, 5
        self.maxhouses = 3
        self.houses = 0
        self.owner = 0

    def getMenuOptions(self):
        returnList = []
        if self.owner == 0:
            returnList.append({"OptionText": "Buy Field", "OptionFunction": "buyField"})

    def buyField(self, buyingPlayer):
        if self.owner == 0:
            if buyingPlayer.money >= self.price:
                buyingPlayer.money = buyingPlayer.money - self.price
                self.owner = buyingPlayer.nr

    def buyHouse(self, buyingPlayer):
        if self.owner == buyingPlayer.nr:
            if self.houses != self.maxhouses:
                self.houses = self.houses + 1
                self.rent = self.rent * self.houseRentMultiplier

    def landOnField(self, landedPlayer):
        if self.owner != 0:
            if self.owner != landedPlayer.nr:
                landedPlayer.money = landedPlayer.money - self.rent


print("Test")
