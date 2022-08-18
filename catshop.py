category = {'catId':[1,2,3],'catName':['food','clothing','toiletries'],
            'catDesc':['consumable non alcoholic goods','standard clothes','shampoos, deodorants and alike']}

products = {'prodId':[1,2,3], 'prodName':['testShampoo','testCrisps','testTshirt'],'price':[20,13,50],'catId':[3,1,2]}

customers = {'custId':[1,2,3],'custMail':['mail1@mail.com','mail2@hotmail.com','mail3@gmail.com'],
            'custPhoneNo':['07777777777','07666666666','07555555555'],
            'billAddress':['flat 12 3 random street, XX11XX','13a green street, XX34XX','big green house, AS12SE'],
            'location':['defaultCity','someTown','village34'],
            'country':['United Kingdom','Zanzibar','United Kingdom']}

ordersPlaced = {'ordId':[1,2,3],  
                'prodId':[2,3,1] , 
                'qty':[10,2,1],  
                'totalPrice':[130,100,200], 
                'custId':[2,3,1], 
                'status':['shipping','delivered','shipping']}

def insertInto(dict,key,data):
    dict[key].append(data)

def checkFields(dict,field,data):
    if data not in dict[field]:
        return True
    else:
        return False
def verifyNumber(number):
    if len(number) != 10 or str(number).isdigit()==False:
        return True
    else:
        return False
        

def verifyEmail(email):
    invalid = False
    #aaaa@jjjj.hhh
    l = email.split('@')
    print(l)
    if len(l)!=2:
        invalid = True
    else:
        #l[0] = 'jgjhg'
        #l[1] ='hhh.com'
        #      =['hhh' , 'com']
        t = ('co','com','org','in')
        for x in t:
            temp = l[1].split('.')
            if len(temp[0])>0  and temp[1]==x:
                invalid = False
                break
        else:
            invalid = True
    return invalid

def createCategory():
    newId = category['catId'][-1] +1
    newCatName = input('enter new category name: ')
    catDesc = input('enter category description: ')
    if checkFields(category,'catName',newCatName) == False:
        print('this category already exists!')
    else:
        category['catId'].append(newId)
        category['catName'].append(newCatName)
        category['catDesc'].append(catDesc)
        print('category created')

def createProduct():
    newId = products['prodId'][-1] +1
    newProdName = input('enter new product name: ')
    newProdPrice = int(input('enter product price: '))
    newProdCatId = input('enter product category: ')
    if checkFields(category,'catName',newProdCatId) == True:
        print('this category doesnt exist!')
    else:
        products['catId'].append(newId)
        products['prodName'].append(newProdName)
        products['price'].append(newProdPrice)
        products['catId'].append(newProdCatId)
        print('product created')

def createCust():
    newId = customers['custId'][len(customers['custId'])-1] +1
    newMail,   newPhoneNo = str(input('enter customer email and phone number, separated by a coma: ')).split(',')
    newAddress = input('enter the first line of address and postcode: ')
    newLoc = input('enter the city: ')
    newCountry = input('enter the country: ')
    if checkFields(customers,'custMail',newMail) == False:
        print('this customer already exists')
    else:
        checkMail = verifyEmail(newMail)
        if checkMail == True:
            while checkMail == True:
                newMail = input('please enter a valid email address')
                checkMail = verifyEmail(newMail)
        checkNum = verifyNumber(newPhoneNo)
        if checkNum == True:
            while checkNum == True:
                newPhoneNo = input('please enter a valid phone number')
                checkNum = verifyNumber(newPhoneNo)
        else:
            customers['custId'].append(newId)
            customers['custMail'].append(newMail)
            customers['custPhoneNo'].append(newPhoneNo)
            customers['billAddress'].append(newAddress)
            customers['location'].append(newLoc)
            customers['country'].append(newCountry)
            print('customer created')

def createOrder():
    newId = category['catId'][-1] +1
    newOrder = int(input('enter the product id: '))
    newQty = int(input('enter the quantity: '))
    newTotal = products['price'][products['prodId'].index(newOrder)]*newQty
    newCust = int(input('enter the customers id: '))
    newStatus = 'Shipping'

    ordersPlaced['ordId'].append(newId)
    ordersPlaced['prodId'].append(newOrder)
    ordersPlaced['qty'].append(newQty)
    ordersPlaced['totalPrice'].append(newTotal)
    ordersPlaced['custId'].append(newCust)
    ordersPlaced['status'].append(newStatus)

def display(table):
    for key, value in table.items() :
        print(key, value,end='\n')

adminDict = {'usernames':['user123', 'user321', '123'] ,
            'passwords':['pass123', 'pass321', '123']}

def verify(username, password):
    if username in adminDict['usernames'] and password in adminDict['passwords']:
        print('\n Access granted!')
        return True
    else:
        print('\n Access denied!\n Username or Password incorrect')
        return False

def get_sales_productID(prodId):
    
    prodId_list = ordersPlaced['prodId']
    # [0]
    index = [x for x in range(len(prodId_list)) if prodId_list[x] == prodId] 
    
    quantities = 0
    for i in index:
        quantities += ordersPlaced['qty'][i]

    index_to_get_name = products['prodId'].index(prodId)
    name_of_the_product = products['prodName'][index_to_get_name]
    total_price = quantities * products['price'][index_to_get_name]


    print(f"Product: {name_of_the_product} has number of items sold: {quantities} and total price of: {total_price}£")

    for i in range(75):
        print("-", end='')
    print("\n")

def get_sales_category(category_name):

    cat_index = category['catName'].index(category_name)

    cat_id = category['catId'][cat_index]

    index_in_cat_id_in_products_NOT_UNIQUE = products['catId'].index(cat_id)

    product_id = products['prodId'][index_in_cat_id_in_products_NOT_UNIQUE]

    get_sales_productID(product_id)

def get_sales_location(location_name):

    loc_index = customers['location'].index(location_name)

    cust_id = customers['custId'][loc_index]

    index_cust_id = ordersPlaced['custId'].index(cust_id)

    product_id = ordersPlaced['prodId'][index_cust_id]

    get_sales_productID(product_id)

def get_sales_price_range(low, high):
    for j in products['prodId']:
        prodId_list = ordersPlaced['prodId']
        # [0]
        index = [x for x in range(len(prodId_list)) if prodId_list[x] == j] 
        
        quantities = 0
        for i in index:
            quantities += ordersPlaced['qty'][i]

        index_to_get_name = products['prodId'].index(j)
        name_of_the_product = products['prodName'][index_to_get_name]
        total_price = quantities * products['price'][index_to_get_name]

        items_dict[name_of_the_product] = total_price
    
    low_to_high = {key: val for key, val in sorted(items_dict.items(), key = lambda ele: ele[1])}

    high_to_low = {key: val for key, val in sorted(items_dict.items(), key = lambda ele: ele[1], reverse = True)}

    if low:
        for key,value in low_to_high.items():
	        print( key, ':', value)
        print('\n')
        
    elif high:
        for key,value in high_to_low.items():
	        print( key, ':', value)
        print('\n')

      
while True:
    print("\n General Options:\n 1:Insert Category\n 2:Insert Products\n 3:Insert Customer Details\n 4:Place an order\n 5:Display all data\n 6:Admin\n 7:Exit\n")
    option = int(input("Please select an option"))
    if option == 1:
        createCategory()
        continue
    elif option == 2:
        createProduct()
    elif option == 3:
        createCust()
    elif option == 4:
        createOrder()
    elif option == 5:
        while True:
            print(' Display all entries in:\n1:Categories\n2:Products\n3:Customers\n4:Orders Placed\n5:Exit to General Options\n')
            display_opt = int(input('please select an option: '))
            if display_opt == 1:
                display(category)
            elif display_opt == 2:
                display(products)
            elif display_opt == 3:
                display(customers)
            elif display_opt == 4:
                display(ordersPlaced)
            elif display_opt == 5:
                break
            
    elif option == 6:
        username, password = str(input("Enter username & password: ")).split()
        status = verify(username, password)
        if status:
            pass
        elif not status:
            continue        
        while True:
            print(" Get total sales based on:\n 1:ProductID\n 2:Category\n 3:PriceRange(L->H)\n 4:PriceRange(H->L)\n 5:Location\n 6:Exit to General Options\n")
            admin_opt = int(input("Please select an option: "))
            if admin_opt == 1:
                prodId = int(input("Please provide product ID: "))
                get_sales_productID(prodId)
            if admin_opt == 2:
                print('\n')
                for i in range(len(category['catName'])):
                    print(category['catName'][i] ,end=' | ' )
                print('\n')
                category_name = str(input("Please provide a category name from the above: "))
                get_sales_category(category_name)

            if admin_opt == 5:
                for i in range(len(category['catName'])):
                    print(customers['location'][i] ,end=' | ' )
                print('\n')
                location = str(input("Please provide location from the above: "))
                get_sales_location(location)
            if admin_opt == 3:
                items_dict = {}
                get_sales_price_range(low=True, high=False)
            if admin_opt == 4:
                items_dict = {}
                get_sales_price_range(low=False, high=True)
            if admin_opt == 6:
                break

    if option == 7:
        print('bye')
        break