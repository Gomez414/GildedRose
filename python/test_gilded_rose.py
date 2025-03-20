"""
test_gilded_rose.py
Abe Gomez
<abraham.gomez@student.cune.edu

The file tests the upgrade quality cases for the Gilded Rose Inn.

"""



# -*- coding: utf-8 -*-
import unittest

from my_gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_normal_update_quality(self):
        """
        Test to see if the normal item updates correctly for one day.
        
        """

        # Arrange

        og_items = [Item("+5 Dexterity Vest", sell_in=10, quality=20)]
        items = [Item("+5 Dexterity Vest", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)

        # Act
        print(items)
        gilded_rose.update_quality()
        print(items)

        # Assert

        self.assertEqual(len(items), len(og_items))

        for expected_item, actual_item in zip(og_items, items):
            self.assertEqual(expected_item.sell_in - 1, actual_item.sell_in)
            self.assertEqual(expected_item.quality - 1, actual_item.quality)


    def test_normal_update_quality_expired(self):
        """
        Test to see if the normal item updates correctly after sell_in is 0.

        """
        # Arrange

        og_items = [Item("+5 Dexterity Vest", sell_in=0, quality=20)]
        items = [Item("+5 Dexterity Vest", sell_in=0, quality=20)]
        gilded_rose = GildedRose(items)

        # Act
        print(items)
        gilded_rose.update_quality()
        print(items)

        # Assert

        self.assertEqual(len(items), len(og_items))

        for expected_item, actual_item in zip(og_items, items):
            self.assertEqual(expected_item.sell_in - 1, actual_item.sell_in)
            self.assertEqual(expected_item.quality - 2, actual_item.quality)


    def test_aged_brie_update_quality(self):
        """
        Test to see if Aged_Brie updates correctly after one day.
        
        """
        # Arrange

        og_items = [Item(name="Aged Brie", sell_in=2, quality=0)]
        items = [Item(name="Aged Brie", sell_in=2, quality=0)]
        gilded_rose = GildedRose(items)

        # Act
        print(items)
        gilded_rose.update_quality()
        print(items)

        # Assert

        self.assertEqual(len(items), len(og_items))

        for expected_item, actual_item in zip(og_items, items):
            self.assertEqual(expected_item.sell_in - 1, actual_item.sell_in)
            self.assertEqual(expected_item.quality + 1, actual_item.quality)


    def test_aged_brie_update_quality_expired(self):
        """
        Test to see if aged brie updates correctly after sell_in is 0.
        
        """
        # Arrange

        og_items = [Item(name="Aged Brie", sell_in=0, quality=0)]
        items = [Item(name="Aged Brie", sell_in=0, quality=0)]
        gilded_rose = GildedRose(items)

        # Act
        print(items)
        gilded_rose.update_quality()
        print(items)

        # Assert

        self.assertEqual(len(items), len(og_items))

        for expected_item, actual_item in zip(og_items, items):
            self.assertEqual(expected_item.sell_in - 1, actual_item.sell_in)
            self.assertEqual(expected_item.quality + 2, actual_item.quality)


    def test_aged_brie_update_quality_max_quality(self):
        """
        Test to see if aged brie update correctly when quality is 50.
        
        """
        # Arrange

        og_items = [Item(name="Aged Brie", sell_in=0, quality=50)]
        items = [Item(name="Aged Brie", sell_in=0, quality=50)]
        gilded_rose = GildedRose(items)

        # Act
        print(items)
        gilded_rose.update_quality()
        print(items)

        # Assert

        self.assertEqual(len(items), len(og_items))

        for expected_item, actual_item in zip(og_items, items):
            self.assertEqual(expected_item.sell_in - 1, actual_item.sell_in)
            self.assertEqual(expected_item.quality, actual_item.quality)


    def test_sulfuras_update_quality(self):
        """
        Test to see if sulfuras updates correctly after one day.
        
        """
        # Arrange

        og_items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]
        gilded_rose = GildedRose(items)

        # Act
        print(items)
        gilded_rose.update_quality()
        print(items)

        # Assert

        self.assertEqual(len(items), len(og_items))

        for expected_item, actual_item in zip(og_items, items):
            self.assertEqual(expected_item.sell_in, actual_item.sell_in)
            self.assertEqual(expected_item.quality, actual_item.quality)


    def test_backstage_update_quality(self):
        """
        Test to see if backstage passes update correctly after one day (sell_in > 10).
        
        """
        # Arrange

        og_items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)]
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)]
        gilded_rose = GildedRose(items)

        # Act
        print(items)
        gilded_rose.update_quality()
        print(items)

        # Assert

        self.assertEqual(len(items), len(og_items))

        for expected_item, actual_item in zip(og_items, items):
            self.assertEqual(expected_item.sell_in - 1, actual_item.sell_in)
            self.assertEqual(expected_item.quality + 1, actual_item.quality)


    def test_backstage_update_quality_10(self):
        """
        Test to see if backstage passes update correctly after one day (sell_in between 11 and 5).
        
        """
        # Arrange

        og_items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=48)]
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=48)]
        gilded_rose = GildedRose(items)

        # Act
        print(items)
        gilded_rose.update_quality()
        print(items)

        # Assert

        self.assertEqual(len(items), len(og_items))

        for expected_item, actual_item in zip(og_items, items):
            self.assertEqual(expected_item.sell_in - 1, actual_item.sell_in)
            self.assertEqual(expected_item.quality + 2, actual_item.quality)


    def test_backstage_update_quality_5(self):
        """
        Test to see if backstage passes update correctly after one day (sell_in between 5 and 0).
        
        """
        # Arrange

        og_items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=47)]
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=47)]
        gilded_rose = GildedRose(items)

        # Act
        print(items)
        gilded_rose.update_quality()
        print(items)

        # Assert

        self.assertEqual(len(items), len(og_items))

        for expected_item, actual_item in zip(og_items, items):
            self.assertEqual(expected_item.sell_in - 1, actual_item.sell_in)
            self.assertEqual(expected_item.quality + 3, actual_item.quality)


    def test_backstage_update_quality_expired(self):
        """
        Test to see if backstage passes update correctly after one day (sell_in is 0).
        
        """
        # Arrange

        og_items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=48)]
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=48)]
        gilded_rose = GildedRose(items)

        # Act
        print(items)
        gilded_rose.update_quality()
        print(items)

        # Assert

        self.assertEqual(len(items), len(og_items))

        for expected_item, actual_item in zip(og_items, items):
            self.assertEqual(expected_item.sell_in - 1, actual_item.sell_in)
            self.assertEqual(expected_item.quality - 48, actual_item.quality)


    def test_backstage_update_quality_max_quality(self):
        """
        Test to see if backstage passes update correctly when quality is 50.
        
        """
        # Arrange

        og_items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=50)]
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=50)]
        gilded_rose = GildedRose(items)

        # Act
        print(items)
        gilded_rose.update_quality()
        print(items)

        # Assert

        self.assertEqual(len(items), len(og_items))

        for expected_item, actual_item in zip(og_items, items):
            self.assertEqual(expected_item.sell_in - 1, actual_item.sell_in)
            self.assertEqual(expected_item.quality, actual_item.quality)


    def test_conjured_update_quality(self):
        """
        Test to see if conjured items update correctly after one day.
        
        """
        # Arrange

        og_items = [Item(name="Conjured Mana Cake", sell_in=3, quality=6)]
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=6)]
        gilded_rose = GildedRose(items)

        # Act
        print(items)
        gilded_rose.update_quality()
        print(items)

        # Assert

        self.assertEqual(len(items), len(og_items))

        for expected_item, actual_item in zip(og_items, items):
            self.assertEqual(expected_item.sell_in - 1, actual_item.sell_in)
            self.assertEqual(expected_item.quality - 2, actual_item.quality)


    def test_conjured_update_quality_expired(self):
        """
        Test to see if conjured items update correctly when sell_in is 0.
        
        """
        # Arrange

        og_items = [Item(name="Conjured Mana Cake", sell_in=0, quality=6)]
        items = [Item(name="Conjured Mana Cake", sell_in=0, quality=6)]
        gilded_rose = GildedRose(items)

        # Act
        print(items)
        gilded_rose.update_quality()
        print(items)

        # Assert

        self.assertEqual(len(items), len(og_items))

        for expected_item, actual_item in zip(og_items, items):
            self.assertEqual(expected_item.sell_in - 1, actual_item.sell_in)
            self.assertEqual(expected_item.quality - 4, actual_item.quality)


if __name__ == '__main__':
    unittest.main()
