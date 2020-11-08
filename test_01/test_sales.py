from sales import shopping_receipt, shopping_basket, shopping_item, roundup_taxes
import unittest


class sales_test(unittest.TestCase):

    # test zero
    def test_unittest(self):       
        self.assertEqual(1, 1)

    # test round function
    def test_round_function (self):

        self.assertEqual (roundup_taxes(16.68), 16.7)
        self.assertEqual (roundup_taxes(16.5), 16.5)
        self.assertEqual (roundup_taxes(16.63), 16.65)
        self.assertEqual (roundup_taxes(16.71), 16.75)
        self.assertEqual (roundup_taxes(16.70), 16.7)

    # test total sales testcase basket 1
    def test_sales_taxes_basket_1 (self):

        item1 = shopping_item()
        item1.name = "The call of the wild"
        item1.price = 12.49py
        item1.category = "books"

        item2 = shopping_item()
        item2.name = "Nevermind"
        item2.price = 14.99
        item2.category = "music CD"

        item3 = shopping_item()
        item3.name = "chocolate bar"
        item3.price = 0.85
        item3.category = "food"

        # create new shopping basket
        sb = shopping_basket ()
        sb.addItem (item1)
        sb.addItem (item2)
        sb.addItem (item3)

        # create new receipt
        sr = shopping_receipt(sb)
        sb.print_items ()

        self.assertNotEqual (sr.shopping_basket, None)
        self.assertEqual(len(sr.shopping_basket.items), 3)

        sr.print_receipt_details ()
        self.assertEqual(sr.get_taxes (), 1.5)

    # test total cost testcase basket 1
    def test_total_cost_basket_1 (self):

        item1 = shopping_item()
        item1.name = "The call of the wild"
        item1.price = 12.49
        item1.category = "books"

        item2 = shopping_item()
        item2.name = "Nevermind"
        item2.price = 14.99
        item2.category = "music CD"

        item3 = shopping_item()
        item3.name = "chocolate bar"
        item3.price = 0.85
        item3.category = "food"

        # create new shopping basket
        sb = shopping_basket ()
        sb.addItem (item1)
        sb.addItem (item2)
        sb.addItem (item3)

        # create new receipt
        sr = shopping_receipt(sb)
        sb.print_items ()

        self.assertNotEqual (sr.shopping_basket, None)
        self.assertEqual(len(sr.shopping_basket.items), 3)

        sr.print_receipt_details ()

        self.assertEqual(sr.get_total (), 29.83)

    # test add items to shopping basket
    def test_add_items_to_shoppingbasket (self):

        item1 = shopping_item()
        item1.name = "The call of the wild"
        item1.price = 12.491
        item1.category = "books"

        item2 = shopping_item()
        item2.name = "Nevermind"
        item2.price = 14.991
        item2.category = "music CD"

        b = shopping_basket ()
        b.addItem (item1)
        b.addItem (item2)

        self.assertEqual(len(b.items), 2)

    # test add shopping basket to receipe
    def test_add_shoppingbasket_to_receipe (self):

        item1 = shopping_item()
        item1.name = "The call of the wild"
        item1.price = 12.491
        item1.category = "books"

        item2 = shopping_item()
        item2.name = "Nevermind"
        item2.price = 14.991
        item2.category = "music CD"

        # create new shopping basket
        sb = shopping_basket ()
        sb.addItem (item1)
        sb.addItem (item2)

        # create new receipt
        r = shopping_receipt(sb)

        self.assertNotEqual (r.shopping_basket, None)
        self.assertEqual (len(r.shopping_basket.items), 2)

    # test sales taxes testcase basket 2 
    def test_sales_taxes_basket_2 (self):

        item1 = shopping_item()
        item1.name = "box of chocolates"
        item1.price = 10.00
        item1.category = "food"
        item1.imported = True

        item2 = shopping_item()
        item2.name = "bottle of perfume"
        item2.price = 47.50
        item2.category = "generic"
        item2.imported = True

        # create new shopping basket
        sb = shopping_basket ()
        sb.addItem (item1)
        sb.addItem (item2)

        # create new receipt
        sr = shopping_receipt(sb)
        sb.print_items ()

        self.assertNotEqual (sr.shopping_basket, None)
        self.assertEqual(len(sr.shopping_basket.items), 2)

        sr.print_receipt_details ()
        self.assertEqual(sr.get_taxes(), 7.65)

    # test total cost testcase basket 2
    def test_total_cost_basket_2 (self):

        item1 = shopping_item()
        item1.name = "box of chocolates"
        item1.price = 10.00
        item1.category = "food"
        item1.imported = True

        item2 = shopping_item()
        item2.name = "bottle of perfume"
        item2.price = 47.50
        item2.category = "generic"
        item2.imported = True

        # create new shopping basket
        sb = shopping_basket ()
        sb.addItem (item1)
        sb.addItem (item2)

        # create new receipt
        sr = shopping_receipt(sb)
        sb.print_items ()

        self.assertNotEqual (sr.shopping_basket, None)
        self.assertEqual(len(sr.shopping_basket.items), 2)

        sr.print_receipt_details ()
        self.assertEqual(sr.get_total (), 65.15)

    # test sale taxes testcase basket 3
    def test_sale_taxes_basket_3 (self):

        item1 = shopping_item()
        item1.name = "bottle of perfume"
        item1.price = 27.99
        item1.category = "generic"
        item1.imported = True

        item2 = shopping_item()
        item2.name = "bottle of perfume"
        item2.price = 18.99
        item2.category = "generic"
        item2.imported = False

        item3 = shopping_item()
        item3.name = "packet of headache pills"
        item3.price = 9.75
        item3.category = "medicalproducts"
        item3.imported = False

        item4 = shopping_item()
        item4.name = "box of chocolates"
        item4.price = 11.25
        item4.category = "food"
        item4.imported = True


        # create new shopping basket
        sb = shopping_basket ()
        sb.addItem (item1)
        sb.addItem (item2)
        sb.addItem (item3)
        sb.addItem (item4)

        # create new receipt
        sr = shopping_receipt(sb)
        sb.print_items ()

        self.assertNotEqual (sr.shopping_basket, None)
        self.assertEqual(len(sr.shopping_basket.items), 4)

        sr.print_receipt_details ()
        self.assertEqual(sr.get_taxes(), 6.70)

        # test sale taxes testcase basket 3
    
    # test total cost testcase basket 3
    def test_total_cost_basket_3 (self):

        item1 = shopping_item()
        item1.name = "bottle of perfume"
        item1.price = 27.99
        item1.category = "generic"
        item1.imported = True

        item2 = shopping_item()
        item2.name = "bottle of perfume"
        item2.price = 18.99
        item2.category = "generic"
        item2.imported = False

        item3 = shopping_item()
        item3.name = "packet of headache pills"
        item3.price = 9.75
        item3.category = "medicalproducts"
        item3.imported = False

        item4 = shopping_item()
        item4.name = "box of chocolates"
        item4.price = 11.25
        item4.category = "food"
        item4.imported = True


        # create new shopping basket
        sb = shopping_basket ()
        sb.addItem (item1)
        sb.addItem (item2)
        sb.addItem (item3)
        sb.addItem (item4)

        sb.print_items ()

        # create new receipt
        sr = shopping_receipt(sb)

        self.assertNotEqual (sr.shopping_basket, None)
        self.assertEqual(len(sr.shopping_basket.items), 4)

        sr.print_receipt_details ()
        self.assertEqual(sr.get_total(), 74.68)

    # test sale taxes testcase basket 3
    def test_sale_taxes_basket_4 (self):

        item1 = shopping_item()
        item1.name = "bottle of perfume"
        item1.price = 27.99
        item1.quantity = 2
        item1.category = "generic"
        item1.imported = True

        item2 = shopping_item()
        item2.name = "bottle of perfume"
        item2.price = 18.99
        item2.category = "generic"
        item2.imported = False

        item3 = shopping_item()
        item3.name = "packet of headache pills"
        item3.price = 9.75
        item3.quantity = 2
        item3.category = "medicalproducts"
        item3.imported = False

        item4 = shopping_item()
        item4.name = "box of chocolates"
        item4.price = 11.25
        item4.category = "food"
        item4.imported = True


        # create new shopping basket
        sb = shopping_basket ()
        sb.addItem (item1)
        sb.addItem (item2)
        sb.addItem (item3)
        sb.addItem (item4)

        # create new receipt
        sr = shopping_receipt(sb)
        sb.print_items ()

        self.assertNotEqual (sr.shopping_basket, None)
        self.assertEqual(len(sr.shopping_basket.items), 4)

        sr.print_receipt_details ()
        self.assertEqual(sr.get_taxes(), 10.9)

        # test sale taxes testcase basket 3
    
    # test total cost testcase basket 3
    def test_total_cost_basket_4 (self):

        item1 = shopping_item()
        item1.name = "bottle of perfume"
        item1.price = 27.99
        item1.quantity = 2
        item1.category = "generic"
        item1.imported = True

        item2 = shopping_item()
        item2.name = "bottle of perfume"
        item2.price = 18.99
        item2.category = "generic"
        item2.imported = False

        item3 = shopping_item()
        item3.name = "packet of headache pills"
        item3.price = 9.75
        item3.quantity = 2
        item3.category = "medicalproducts"
        item3.imported = False

        item4 = shopping_item()
        item4.name = "box of chocolates"
        item4.price = 11.25
        item4.category = "food"
        item4.imported = True


        # create new shopping basket
        sb = shopping_basket ()
        sb.addItem (item1)
        sb.addItem (item2)
        sb.addItem (item3)
        sb.addItem (item4)

        sb.print_items ()

        # create new receipt
        sr = shopping_receipt(sb)
        
        self.assertNotEqual (sr.shopping_basket, None)
        self.assertEqual(len(sr.shopping_basket.items), 4)

        sr.print_receipt_details ()
        self.assertEqual(sr.get_total(), 116.62)

if __name__ == '__main__':
    unittest.main()