print("\t\t\tPRODUCT_MANAGER_PROJECT\n\n\n")

menu="""
        menu

        press 1 for product manager
        press 2 for customer

"""
# take one dictionary for product items
product = {}

# flag for multiple inputs

status = True
while status:
    print(menu)
    choice = int(input("Enter your choice : "))
    if choice == 1:
        spec = {}
        product_name = input("Enter product name : ")
        product_qty = int(input("Enter product qty : "))
        product_price = int(input("Enter product price : "))

        if product_name in product.keys():
            old_qty = product[product_name]['qty']

            spec['qty'] = old_qty + product_qty
            spec['price'] = product_price

            product[product_name] = spec
            print("-----> already exist",product)

        else:
            spec['qty'] = product_qty
            spec['price'] = product_price

            product[product_name] = spec

            print(product)

    else:
        for k in product.keys():
            print(f"{k} = Rs. {product[k]['price']}" )

    ch = input("do you want to add more products : ")
    if ch == 'no':
        status = False

    

