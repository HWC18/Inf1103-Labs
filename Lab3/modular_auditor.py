Total_inventory = 0
Failed_entries = 0
Successful_entries = 0
Units_processed = 0

#take in user input
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

while True:
    print("Current Total Inventory:", Total_inventory)
    user_input = get_valid_input()
    if user_input == None:
        Failed_entries +=1
    elif user_input == "quit":
        generate_report(Units_processed,Failed_entries)
        break
    else:
        Total_inventory=process_delivery(Units_processed,int(user_input))
        Units_processed += int(user_input)
        print("Tax amount:", calculate_tax(int(user_input)))