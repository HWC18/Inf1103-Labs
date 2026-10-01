Total_inventory = 0
Failed_entries = 0
Units_processed = 0
compiled_list = []

def get_valid_input():
    while True:
        product_name = input("Enter the product name (type 'quit' to quit): ")
        
        if  product_name.replace(' ','').isalpha() == False:
            print('invalid input, please try again')
        elif product_name.strip().lower() == 'quit':
            return 'quit'
        else:
            while True:
        
                product_amount = input("Enter the product amount (type 'quit' to quit): ")

                if product_amount.strip().lower() == 'quit':
                    return 'quit'
                elif product_amount.isdigit() == 'quit' or int(product_amount) <= 0:
                    print('invalid input, please try again')
                else:
                    return product_name,product_amount

def process_order(product_name, product_amount): #use this function to compile user input into a list
    with open('inventory.txt','a+') as file:
        file.seek(0)
        last_line = ""
        for line in file:
            last_line = line
    clean_last_line = last_line.strip()
    product_id = clean_last_line.split(', ')[0]
    new_product_id = int(product_id) + 1
    print(new_product_id)
    print(product_name)
    print(product_amount)
    if len(compiled_list) != 0:
            new_product_id = int(compiled_list[-1][0]) + 1
    temp_product_info = [new_product_id,product_name,product_amount]
    compiled_list.append(temp_product_info)
    print(compiled_list)
        

    




def generate_report(total_units,failed_attempts):
    print("Failed Entries:", failed_attempts)
    print("Units Processed:", total_units)

def load_inventory():
    with open("inventory.txt",'a+') as file:
        file.seek(0)
        print("current orders:\n")
        print(file.read())


while True:
    load_inventory()
    order_list = []
    new_order = get_valid_input()
    if new_order == 'quit':
        break
    else:
        order_list.append(list(new_order))
        process_order(order_list[0][0],order_list[0][1])
        
