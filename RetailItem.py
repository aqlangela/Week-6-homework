#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class RetailItem():
    
    def __init__(self, description, units, price):
        self.description = description
        self.units = units
        self.price = price
        
    def get_dscrptn(self):
        return self.description
        
    def get_units(self):
        return self.units
        
    def get_price(self):
        return self.price
        
    def __str__(self):
        return 'Item Description: ' + self.description + \
               '\nNumber of Units: ' + self.units + \
               '\nPrice: $' + self.price
