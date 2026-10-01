Total_inventory = 0
Failed_entries = 0
Successful_entries = []
Units_processed = 0


def get_valid_input():
    user_input = input("Enter stock quantity or type 'quit to exit the program: ")
    if user_input.strip().lower() == "quit":
        return "quit"
    elif user_input.isdigit() == False or int(user_input) < 0 or int(user_input) > 500:
        print("Please provide a valid input")
    else:
        return user_input
    
def process_delivery(current_total,new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount / 10

def generate_report(total_units,failed_attempts):
    print("Failed Entries:", failed_attempts)
    print("Units Processed:", total_units)

def create_inventory():
    new_file = open('inventory.txt','a')
    new_file.close()

def load_inventory():
    with open("inventory.txt",'a+') as file:
        content = file.read()
        return content





print('Current Orders\n')
print(load_inventory())
user_input = get_valid_input()
    