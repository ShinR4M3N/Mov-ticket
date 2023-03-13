'''Movie theatre ticketing system- v1
Get category and number of tickets
Created by Isaac Shin
'''

# Component 1 - welcome screen and set up variables


def sell_ticket():
    print("********** Fanfare Movies - ticketing system **********\n")

    adult_tickets = 0
    child_tickets = 0
    student_tickets = 0
    gift_ticket = 0
    total_sales = 0
    tickets_sold = 0

    # Component 2 - Get category and number of tickets
    ticket_wanted = "Y"
    while ticket_wanted == "Y":
        ticket_type = input("What kind of ticket do you want: \n"
                            "\t 'A' for adult, or\n"
                            "\t 'S' for student, or\n"
                            "\t 'C' for child, or\n"
                            "\t 'G' for Gift voucher\n"
                            ">>").upper()

        ticket = ticket_type
        num_tickets = int(input(f"How many tickets do you want: "))

        print(f"\nYou have ordered {num_tickets} {ticket} tickets(s)!")
        ticket_wanted = input("Do you want to sell another ticket (Y/N): "
                              "").upper()


# Main routine
sell_ticket()
