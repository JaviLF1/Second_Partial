#https://replit.com/join/thyvlgwhrw-javier-eduard38
def nutritionist():
  print('Hello Im nutrisionist bot')
  print('I will be healping you on your path of having I healthier life')
  print('But for that i will need you to give mi some values')
  print('First your age')
  age=input()
  print('Now your height in meters')
  height=input()
  print('Your weight in kilograms')
  weight=input()
  imc=float(weight)/float(height)**2
  print('And your physical activity, select the number of the option that best fits you')
  print('1.Sendentary,2.Moderate,3.Active')
  phyactivity=input()
  if float(age)<=float(18):
    print('We recomend a high carbohydrate diet')
  if float(age)>18 and float(age)<35:
    print('We recomend a high protein and lower carbohydrate diet')
  if float(age)>=35:
    print('We recomend a low shugar diet')

  if float(age)>=18 and float(age)<=30 and phyactivity=='1'or phyactivity=='2':
    print('You need aerobic exercises')

  if float(imc)<18 and phyactivity=='1':
    print('You need to consult a nutrisionist and increase your physical activity')

  if float(imc)>=18 and float(imc)<=25 and phyactivity=='2' or phyactivity=='3':
    print('You are in good condition')

  if float(imc)>25 and phyactivity=='1':
    print('You need to consult a nutrisionist,increase your physical activity and recude your weight')

  



nutritionist()
