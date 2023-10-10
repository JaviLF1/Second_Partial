#https://replit.com/join/cywcgvfooa-javier-eduard38

#.Multiple Discounts Purchases

print('A=10%')
print('B=5%')
print('C=2%')

print('Enter the price of the product')
price=input()
print('Now the number you will get from that product')
num_of_units=input()
print('And now the typpe of product, A,B,C')
type_of_product=input()

if type_of_product=='A':
  discount=float(price)*float(0.10)
  final_price=(float(price)-float(discount))
  if float(num_of_units)>=10:
    new_discount=(final_price*.10)
    new_final_price=(final_price-new_discount)
    print('Your total price is',new_final_price)

  if float(num_of_units)<10:
    fp_discount=(float(final_price)*float(num_of_units))
    print('Your total price is',fp_discount)


  

if type_of_product=='B':
  discount=float(price)*float(0.05)
  final_price=(float(price)-float(discount))
  if float(num_of_units)>=10:
    new_discount=(final_price*.10)
    new_final_price=(final_price-new_discount)
    print('Your total price is',new_final_price)

  if float(num_of_units)<10:
    fp_discount=(float(final_price)*float(num_of_units))
    print('Your total price is',fp_discount)

if type_of_product=='C':
  discount=float(price)*float(0.02)
  final_price=(float(price)-float(discount))
  if float(num_of_units)>=10:
    new_discount=(final_price*.10)
    new_final_price=(final_price-new_discount)
    print('Your total price is',new_final_price)

  if float(num_of_units)<10:
    fp_discount=(float(final_price)*float(num_of_units))
    print('Your total price is',fp_discount)


#Calories Burned Calculator
print('Enter your weight')
weight=input()
print('Enter the duration of the exersice in minutes')
time=input()
print('Now, enter the ativity:Running, Swimming or Cycling')
activity=input()
if activity=='Running':
  calories=float(time)*float(11.4)
  print('You have burn',calories,'calories')

if activity=='Swimming':
  calories=float(time)*float(7)
  print('You have burn',calories,'calories')

if activity=='Cycling':
  calories=float(time)*float(8)
  print('You have burn',calories,'calories')


#Unit Conversion
print('Enter the unit you have: Meters,Centimeters or Milimeters ')
unit=input()
print('Ok, now the amount you have')
amount=input()
print('Now enter the unit you want to convert:Meters,Centimeters or Milimeters')
coverscion=input()

if unit=='Meters':
  if coverscion=='Centimeters':
    result=float(amount)*float(100)
    print('The result is',result,'cm')

  if coverscion=='Milimeters':
    result=float(amount)*float(1000)
    print('The result is',result,'mm')
