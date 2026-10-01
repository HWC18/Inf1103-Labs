compiled_list = []

def get_valid_input():
    while True:
        product_name = input("Enter the product name (type 'quit' to quit): ")
        if  product_name.replace(' ','').isalpha() == False:
            print('invalid input, please try again')
            continue
        elif product_name.strip().lower() == 'quit':
            return 'quit'
        else:
            while True:
                product_amount = input("Enter the product amount (type 'quit' to quit): ")
                if product_amount.strip().lower() == 'quit':
                    return 'quit'
                elif product_amount.isdigit() == False or int(product_amount) <= 0:
                    print('invalid input, please try again')
                    continue
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
    if len(compiled_list) != 0:
            new_product_id = int(compiled_list[-1][0]) + 1
    temp_product_info = [new_product_id,product_name,product_amount]
    compiled_list.append(temp_product_info)
    return compiled_list

def save_order(compiled_list):
    for list in compiled_list:
        list[0] = str(list[0])
        list[2] = str(list[2])
        with open('inventory.txt', 'a') as file:
            line = f"\n{list[0]}, {list[1]}, {list[2]}"
            file.write(line)


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
        try:
            save_order(finalised_order)
            print('Order saved to inventory.txt')
            break
        except NameError:
            break
    else:
        order_list.append(list(new_order))
        finalised_order = process_order(order_list[0][0],order_list[0][1])
        
