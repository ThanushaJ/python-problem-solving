#Print my Bill

prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {
    'apple': 1,
    'banana': 6}
bill = 0
for i in my_purchase:
    for j in prices:
        if i in j:
            bill += prices[j]*my_purchase[i]

print("your bill:  ", bill)