# score = 0
# heigt = 1.8
# iswinning = True
#
#
# print(f"your score is {score}")


# age = input("what is your age")
# age_as_int = int(age)
# year_reming = 90 - age_as_int
# days_reming = year_reming * 365
# weeks_reming = year_reming * 52
# month_reming = year_reming * 12
#
# print(month_reming)
#-------------------------------------------------------
#
# bill = float(input("whats is total? $"))
# tip = int(input("how much tip?"))
# pepole = int(input("how many pepole?"))
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / pepole
# final_amount = round(bill_per_person, 2)
# final_amount = "{:.2f}".format(bill_per_person)
# print(f"Each person pay {final_amount}")
#------------------------------------------------------

height = float(input("enter height"))
weight = float(input("enter weight"))

bmi = round(weight / height ** 2)
if bmi <18.5:
    print(f"your bmi {bmi}, you are underweight.")
elif bmi < 25:
    print(f"your bmi {bmi}, you have normal weight")
elif bmi < 30:
    print(f"your bmi {bmi}, you have over weight")
elif bmi < 35:
    print(f"your bmi {bmi}, you are obese")


#----------------------------------------------------------
