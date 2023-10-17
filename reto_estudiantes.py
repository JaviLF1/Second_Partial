#https://replit.com/join/zwaixsaaci-javier-eduard38
print('Hello, Im discount checker, I will tell you how many of a discount you will get on your final purchase ')
print('Ok,first I need to know if you have a mambership card')
print('Type yes or no')
membercard=input()
print('Now put the amount of your purchase')
purchase=input()

if float(purchase)<100 and membercard=='no':
  print('OHLALA,it looks that there are no dicounts for this purchase')
  print('your final price will be',purchase)

if float(purchase)>=100 and membercard=='yes':
  discount1=float(purchase)*.10
  final1=int(purchase)-int(discount1)
  discount2=final1*.05
  final2=final1-discount2
  print('VAMOSSS, it look that you have recive 2 discounts, the fist one of a 10% discount for your purchase been more than 100, and the second, of 5% for having the membership card')
  print('Your final price is',final2)


if float(purchase)>=100 and membercard=='no':
  discount1=float(purchase)*.10
  final1=int(purchase)-int(discount1)
  print('Oh, it looks that there is a discount of 10% for purchising mor than 100 in the store')
  print('Your final price is',final1)

if float(purchase)<100 and membercard=='yes':
  discount1=float(purchase)*.05
  final1=float(purchase)-float(discount1)
  print('For having a mambership card we have a special gift to you, that is right a 5% dicount')
  print('So your final price is',final1)
