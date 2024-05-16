logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
bid_dict = {}

def add_another_bid():
    name = input("What is your name?: ")
    price = int(input("What is your bid price?: $"))

    bid_dict[name] = price

def auction():
    print(logo)
    another_bid = True

    add_another_bid()

    while another_bid:
        is_bidder = input("Is there another bidder?: ")
        if is_bidder.lower() == 'no':
            another_bid = False

        elif is_bidder.lower() == 'yes':
            add_another_bid()
        
        else:
            print("No such value")
            break
                
auction()

highest_bid = 0
highest_name = ''
for i in bid_dict:
    if bid_dict[i] > highest_bid:
         highest_bid = bid_dict[i]
         highest_name = i


print(f"The winner is {highest_name} with a bid of {highest_bid}")
