#welcome to the tip calculator!
#what was the total bill? $150
#how much tip would like to give? 10,12, or 15? 12
#how many people split the bill?5
#each person shoud pay: $33.60
print("welcome to the tip calculator!")
bill=float(input("what was the total bill"))
tip=int(input("how much tip would like to give"))
split_people=int(input("how many people split the bill?"))
tip_as_percentage = tip / 100
total_tip_amount = tip_as_percentage * bill
total_bill = bill + total_tip_amount
bill_per_person = total_bill / split_people
final_amount = round(bill_per_person, 2)
print(f"each person should pay : ${final_amount:}")#aome times python will be removes unneccesary 0's 
#if we want exactly 2 decimals use .2f after final_amount:.2f