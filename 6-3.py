#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RetailItem

class CashRegister():
    
    def __init__(self, item_list = []):
        
        self.list = item_list
        self.sum = 0
        
    def purchase_item(self):
        n_item = input("New item>")
        n_units = input("How many units>")
        n_price = input("Price>")
        self.list.append(RetailItem.RetailItem(n_item, n_units, n_price))
        return self.list
    
    def get_total(self):
        for item in self.list:
            self.sum += float(item.get_units()) * float(item.get_price())
        return format(self.sum, '.2f')
    
    def show_items(self):
        for item in self.list:
            print(item)
        
    def clear(self):
        self.list = []

def main():
    
    items = CashRegister()
    
    while True:
        print("===== Menu =====" \
              "\n#1 Add an item to your cart." \
              "\n#2 Empty your cart." \
              "\n#3 Check out." \
              "\n================")
        order = input(">")
        
        if order == "1":
            items.purchase_item()
        elif order == "2":
            items.clear()
            print("Your items have been cleared")
        elif order == "3":
            items.show_items()
            print("The total price is %s." % items.get_total())
            break
        else:
            print("Invalid input.")
            
main()
            
        