# INPUT
# Get number of hours worked per day from user.
# Get hourly pay from user
# Both floats must not be negative. Hours worked can not be over 24hrs a day and the number inputed must be a float.
def get_hours_worked_per_day():
     while True:
          try:
               user_daily_hours = float(input("Please provide the number of hours you work each day. "))
               if user_daily_hours <= 0 or user_daily_hours > 24:
                    print("ERROR: Please input a positive number greater than 0 but less than 24!")
                    continue
               else:
                    break
          except:
               print("ERROR: Please input a number and do not include any special characters!")
     return user_daily_hours
def get_hourly_pay():
     while True:
          try:
               user_hourly_pay = float(input("Please input your hourly wage. "))
               if user_hourly_pay <= 0:
                    print("ERROR: Please input a positive number!")
                    continue
               else:
                    break
          except:
               print("ERROR: Please input a number and do not include any special characters!")
     return user_hourly_pay
# PROCESSING
# Number of hours worked times hourly pay times 350 days times would be wage with no tax. Then this would be multiplied by 12 percent to find pay deducted by tax.
# The final wage would be the pre tax wage subtracted by the taxes deducted.
def wage_pre_taxes_calculator(user_hourly_pay, user_daily_hours):
     DAYS_WORKED_PER_YEAR = 350
     wage_pre_taxes = 350 * user_hourly_pay * user_daily_hours
     return wage_pre_taxes
def taxes_decuction_calculator(wage_pre_taxes):
     PERCENT_DEDUCTED_FOR_TAXES = 0.12
     taxes_deducted = wage_pre_taxes * PERCENT_DEDUCTED_FOR_TAXES
     return taxes_deducted
def wage_post_taxes_calulator(wage_pre_taxes, taxes_deducted):
     wage_post_taxes = wage_pre_taxes - taxes_deducted
     return wage_post_taxes
# OUTPUT
# User is given a statement that provides their hours worked, hourly wge, wage before tax, taxes paid, and final wage.
# All values must be printed with two decimal points and have a dollar sign if needed.
def main():
     user_daily_hours = get_hours_worked_per_day()
     user_hourly_pay = get_hourly_pay()
     wage_pre_taxes = wage_pre_taxes_calculator(user_hourly_pay, user_daily_hours)
     taxes_deducted = taxes_decuction_calculator(wage_pre_taxes)
     wage_post_taxes = wage_post_taxes_calulator(wage_pre_taxes, taxes_deducted)
     print(f"Pay Statement:\nHours Worked = {user_daily_hours:.2f}\nHourly Pay = ${user_hourly_pay:.2f}\nAnnual Pay Pre Taxes = ${wage_pre_taxes:.2f}\nTaxes Deducted = ${taxes_deducted:.2f}\nAnnual Pay Post Taxes = ${wage_post_taxes:.2f}")
     # Prompt user to run the program again.
    # do_again = input("Do you want to run another calculaton? (y/n): ")
     # Decided whether to run the program again or stop.
    # if do_again lower() == 
main()
# NOT FINISHED