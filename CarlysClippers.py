# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 17:14:13 2021
You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block.
 Your job is to go through the lists of data that have been collected in the past couple of weeks. 
 You will be calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month.
@author: Sarp
"""
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price=0
for i in prices:
  total_price+=i
print('Total price:',total_price)
average_price=total_price/len(prices)
print('Average price:',average_price)
new_prices=[]
for x in prices:
   new_prices.append(x-5)
print('New prices:',new_prices)
total_revenue=0
for i in range(len(hairstyles)):
  total_revenue+=prices[i]*last_week[i]
print('Total revenue:',total_revenue)
average_daily_revenue=total_revenue/7
print('Average daily revenue:',average_daily_revenue)
cuts_under_30=[]

for k in range(len(new_prices)-1):
  if new_prices[k]<30:
    cuts_under_30.append(hairstyles[k])
print(cuts_under_30)
               
