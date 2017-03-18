#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import pickle

# Bank account class
class Account():
    #Initializer
    def __init__(self, holder, acct_number, acct_type, balance):
        self.holder = holder
        self.acct_number = acct_number
        self.acct_type = acct_type
        self.balance = balance
        # C = Checking, S = Savings
        if self.acct_type == "C":
            self.rate = .08
        elif self.acct_type == "S":
            self.rate = .04
            
    # Setters for account holder & balance
    def set_holder(self, new_holder):
        self.holder = new_holder
        
    def set_balance(self, new_balance):
        self.balance = new_balance
        
    # Getters for account holder & balance
    def get_holder(self):
        return self.holder
        
    def get_balance(self):
        return self.balance
    
    # Simple & compound interest calculators
    def simple_interest(self, time):
        s_interest = int(self.balance) * (self.rate * time)
        return format(s_interest, '.3f')
        
    def compound_interest(self, time):
        c_interest = int(self.balance) * ((1 + self.rate) ** time) - self.balance
        return format(c_interest, '.3f')

    # Str() return function
    def __str__(self):
        return self.holder + "," + self.balance

# Customer class - contains an instance of the BankAccount class
class Customer():
    def __init__(self, name, acct_type, balance):
        self.name = name
        self.account = Account(self.name, random.randint(1,10000), acct_type, balance)
    def __str__(self):
        return self.name + str(self.account.get_balance())
        
def next_menu(customer, o):
    if o == "1":
        year = int(input("How many years>"))
        return "The simple interest is %d." % customer.account.simple_interest(year)
    elif o == "2":
        year = int(input("How many years>"))
        return "The compound interest is %d." % customer.account.compound_interest(year)
    elif o == "3":
        pass
    else:
        return "Invalid input."

def main():
    try:
        f = open("customers.dat", "rb")
        dic = pickle.load(f)
        f.close()
    except:
        dic = {}
    
    while True:
        print("===== Menu =====" \
              "\n#1 Look up an account." \
              "\n#2 Add a new account." \
              "\n#3 Change an account." \
              "\n#4 Delete an account." \
              "\n#5 Quit." \
              "\n================")
        order = input(">")
        
        if order == "1":
            check = input("Check a card holder>")
            if check in dic.keys():
                customer = dic[check]
                print("Balance:", customer.account.get_balance())
                print("=== Menu ===" \
                      "\n#1 Check simple interest." \
                      "\n#2 Check compound interest." \
                      "\n#3 Pass.")
                next_order = input(">")
                print(next_menu(customer, next_order))
            else:
                print("The account does not exist.")
                
        elif order == "2":
            print("You are creating a new account.")
            n_holder = input("Enter the name of the new card holder>")
            n_acct_type = input("Enter account type (C/S)>")
            n_balance = input("Enter balance>")
            
            dic[n_holder] = Customer(n_holder, n_acct_type, n_balance)
            print("A new account has been created.")
            
        elif order == "3":
            print("You are changing the information of an existing account.")
            check = input("Enter the name of a card holder>")
            if check in dic.keys():
                n_acct_type = input("Enter new account type (C/S)>")
                n_balance = input("Enter new balance>")
                dic[check] = Customer(check, n_acct_type, n_balance)
                print("The account has been changed.")
            else:
                print("The account does not exist.")
            
        elif order == "4":
            print("You are deleting an account.")
            try:
                check = input("Enter the name of a card holder>")
                del dic[check]
                print("The account has been deleted.")
            except:
                print("Invalid input.")
            
        elif order == "5":
            break
        
        else:
            print("Invalid input.")
    
    output = open("customers.dat", "wb")
    pickle.dump(dic, output)
    output.close()

main()
