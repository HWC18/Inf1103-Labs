Total_inventory = 0
Failed_entries = 0
Successful_entries = 0
Units_processed = 0
while True:
    print("Current Total Inventory:", Total_inventory)
    user_input = input("Enter stock quantity or type 'quit' to quit: ")

    if Total_inventory >= 500:
        print("Inventory has exceeded its limit")
        break
    elif user_input.strip().lower() == "quit":
        print("Failed Entries:", Failed_entries)
        print("Successful Entries:", Successful_entries)
        print("Units Processed:", Units_processed)
        break
    elif user_input.isdigit() == False or int(user_input) < 0 or int(user_input) > 500:
        print("Error: Please enter a valid amount")
        Failed_entries += 1
    else:
        Units_processed += int(user_input)
        Total_inventory += int(user_input)
        Successful_entries += 1
        