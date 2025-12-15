"""
Author: Ivanloe L. Manuel
Date written: 11/02/2025
Short Description: This program calculates and displays a monthly payment schedule for a TidBit Computer Store purchase plan.
"""
#Program: tidbit.py
#Programming Exercise 3.10

def main():
#Input:
    fltPurchasePrice = float(input("Enter the purchase price: "))

#Constants:
    ANNUAL_RATE = 0.12
    MONTHLY_RATE = ANNUAL_RATE / 12
    DOWNPAYMENT_RATE = 0.10
    TABLEFORMATSTRING = "%2d%15.2f%15.2f%17.2f%17.2f%17.2f"

#Initialize:
    monthlyPayment = 0.05 * fltPurchasePrice

#Variables:
    month = 1
    balance = fltPurchasePrice - (fltPurchasePrice * DOWNPAYMENT_RATE)

#Output:
    print("Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")

#Loop through payment:
    while balance > 0:
        if monthlyPayment > balance:
            monthlyPayment = balance
            interest = 0
        else:
            interest = balance * MONTHLY_RATE

        principal = monthlyPayment - interest
        remaining = balance - monthlyPayment

    #Display payment details:
        print(TABLEFORMATSTRING % (month, balance, interest, principal, monthlyPayment, remaining))

    #Update for next month
        balance = remaining
        month += 1

if __name__ == "__main__":

    main()
