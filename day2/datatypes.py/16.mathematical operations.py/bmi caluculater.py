#bmi calculater
#it is used in medicine to measure uderweight and over weight
#given weight=84
#height=1.65
#to calucualete bmi we have  a formula that is divide the weight by height squared
bmi = 84 / 1.65 ** 2 # or (1.65 * 1.65)
print(bmi)

print(int(bmi))
print(round(bmi))
#print(round(number, ndigits))#n digits means b=number of decimal places
print(round(bmi, 3))