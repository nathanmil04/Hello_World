# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:03:48 2024

@author: nmilani

Group 35

Cooper Nathan Owen Quinn
"""
total_income = float(input('What is your annual income:'))
mfj = input('If you are married filing jointly, type Yes. Otherwise type No. Are you married filing jointly:')

if mfj == 'yes':
    partner_income = float(input("What is your partner's income:"))
    total_income += partner_income
    
if mfj == 'yes':
    if total_income <= 12420:
        state_tax = total_income * .044
    elif 12420 < total_income <= 62100:
        state_tax = 546.48 + (total_income - 12420) * .0482
    elif total_income > 62100:
        state_tax = 2941.06 + (total_income - 62100) * .057
else:
    if total_income <= 6210:
        state_tax = total_income * .044
    elif 6210 < total_income <= 31050:
        state_tax = 273.24 + (total_income - 6210) * .0482
    elif total_income > 31050:
        state_tax = 1470.53 + (total_income - 31050) * .057
        
if mfj == 'yes':
    std = 29200
else:
    std = 14600
    
tax_inc = total_income - std

if tax_inc < 0:
    fed_tax = 0
    
else:
    if mfj == 'yes':
        if tax_inc <= 23200:
            fed_tax = tax_inc * .1
        elif 23201 <= tax_inc <= 94300:
            fed_tax = 2320 + (tax_inc - 23200) * .12
        elif 94301 <= tax_inc <= 94301:
            fed_tax = 10852 + (tax_inc - 94300) * .22
        elif 201051 <= tax_inc <= 383900:
            fed_tax = 34337 + (tax_inc - 201050) * .24
        elif 383901 <= tax_inc <= 487450:
            fed_tax = 78221 + (tax_inc - 383900) * .32
        elif 487451 <= tax_inc <= 731200:
            fed_tax = 111357 + (tax_inc - 487450) * .35
        elif tax_inc >= 731201:
            fed_tax = 196669.5 + (tax_inc - 731200) * .37
    else:
        if tax_inc <= 11600:
            fed_tax = tax_inc * .1
        elif 11601 <= tax_inc <= 47140:
            fed_tax = 1160 + (tax_inc - 11600) * .12
        elif 47151 <= tax_inc <= 100525:
            fed_tax = 5426 + (tax_inc - 47150) * .22
        elif 100526 <= tax_inc <= 191950:
            fed_tax = 17168.5 + (tax_inc - 100525) * .24
        elif 191951 <= tax_inc <= 243725:
            fed_tax = 39110.5 + (tax_inc - 191950) * .32
        elif 243726 <= tax_inc <= 609350:
            fed_tax = 55678.5 + (tax_inc - 243725) * .35
        elif tax_inc >= 609351:
            fed_tax = 183647.25 + (tax_inc - 609350) * .37
            
total_tax = fed_tax + state_tax
print("Your state taxes are: $", round(state_tax))
print("Your federal taxes are: $", round(fed_tax))
print("Your total taxes are: $", round(total_tax))
            
            
            
            
            
            
            
            
            
            
            
            
            
