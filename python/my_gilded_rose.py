"""
my_gilded_rose.py
Abe Gomez
<abraham.gomez@student.cune.edu

The file upgrades item quality for the Gilded Rose Inn.

"""


# -*- coding: utf-8 -*-

class GildedRose(object):
    """ Initialize store items and sort by their types. """

    def __init__(self, items):
        """ Create the item as a class for its normal or special status. """

        self.items = items
        for i in range(len(items)):
            self.items[i] = self._create_item(self.items[i])

    def _create_item(self, item):
        """ Convert generic item to a special subclass. """

        if item.name == "Aged Brie":
            return AgedBrie(item.name, item.sell_in, item.quality)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePass(item.name, item.sell_in, item.quality)
        elif item.name == "Sulfuras, Hand of Ragnaros":
            return Sulfuras(item.name, item.sell_in, item.quality)
        elif item.name == "Conjured Mana Cake":
            return Conjured(item.name, item.sell_in, item.quality)
        return item
    
    def update_quality(self):
        """ Update the quality and sell_in of items. """

        for item in self.items:
            if isinstance(item, AgedBrie):
                item.update_quality()
            elif isinstance(item, BackstagePass):
                item.update_quality()
            elif isinstance(item, Sulfuras):
                item.update_quality()
            elif isinstance(item, Conjured):
                item.update_quality()
            else:
                item.sell_in -= 1
                if item.sell_in < 0:
                    item.quality -= 2
                else:
                    item.quality -= 1
                
                if item.quality < 0:
                    item.quality = 0

class Item:
    """ Initialize items and their characteristics. """

    def __init__(self, name, sell_in, quality):
        """ Create item characteristics. """

        self.name = name
        self.sell_in = sell_in
        self.quality = quality


    def __repr__(self):
        """ Format for a neat print. """

        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class AgedBrie(Item):
    """ Initialize item to have the updated status of Aged Brie. """

    def __init__(self, name, sell_in, quality):
        """ Ensure the Aged Brie item still has item characteristics. """

        super().__init__(name, sell_in, quality)

    def update_quality(self):
        """ Update Aged Brie by its special criteria. """

        self.sell_in -= 1
        
        if self.quality < 50:
            self.quality += 1
        if self.sell_in < 0:
            self.quality += 1
            
        self.quality = min(50, self.quality)

class BackstagePass(Item):
    """ Initialize item to have the updated status of a Backstage Pass. """

    def __init__(self, name, sell_in, quality):
        """ Ensure the Backstage Pass item still has item characteristics. """

        super().__init__(name, sell_in, quality)
    
    def update_quality(self):
        """ Update Backstage Pass by its special criteria. """

        self.sell_in -= 1

        if self.quality < 50:
            self.quality += 1
            if self.sell_in < 10:
                self.quality += 1
            
            if self.sell_in < 5:
                self.quality += 1

            if self.sell_in < 0:
                self.quality = 0
            
            if self.quality > 50:
                self.quality = 50
        
        else:
            self.quality = 50
            if self.sell_in < 0:
                self.quality = 0

class Sulfuras(Item):
    """ Initialize item to have the updated status of a Sulfuras. """

    def __init__(self, name, sell_in, quality):
        """ Ensure the Sulfuras item still has item characteristics. """

        super().__init__(name, sell_in, quality)

    def update_quality(self):
        """ Update Sulfuras by their special criteria. """

        pass

class Conjured(Item):
    """ Initialize item to have the update status of a Conjured item. """

    def __init__(self, name, sell_in, quality):
        """ Ensure the Conjured item still has item characteristics. """

        super().__init__(name, sell_in, quality)

    def update_quality(self):
        """ Update the Conjured items by their special criteria. """

        self.sell_in -= 1
        
        if self.quality < 50:
            self.quality -= 2
        if self.sell_in < 0:
            self.quality -= 2
        
        if self.quality < 0:
            self.quality = 0
            
        if self.quality > 50:
            self.quality = 50