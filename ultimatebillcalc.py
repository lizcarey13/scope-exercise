bill_amount, dine_number, tip_amount, number_of_people = 0, 0 , 0, 0
calculated_tip_amount, total_bill, amt_per_person = 0, 0, 0


def prompt_user():
    global bill_amount, dine_number, number_of_people, tip_amount
    bill_amount = int(raw_input("how much is your bill not including tip? "))
    dine_number = raw_input("did you dine alone? (y/n) ")
    if dine_number == 'no':
        number_of_people = int(raw_input("how many people were at dinner? "))
    tip_amount = raw_input('Is 18% tip ok? (y/n) ')
    if tip_amount == 'no':
        tip_amount = float(raw_input('how much do you want to leave for tip? '))
    else:
        tip_amount = .18
def calculate_bill():
    global bill_amount, tip_amount, calculated_tip_amount, number_of_people, amt_per_person
    calculated_tip_amount = tip_amount * bill_amount
    total_bill = bill_amount + calculated_tip_amount
    print total_bill
    if number_of_people == True:
        amt_per_person = total_bill / number_of_people

def display_bill_amounts():
    global bill_amount, tip_amount, total_bill, amt_per_person
    print "bill amount: ", bill_amount, "tip amount: ", tip_amount, "total bill: ", total_bill, "amt per person: ", amt_per_person

prompt_user()
calculate_bill()
display_bill_amounts()