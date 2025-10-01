from pyscript import display, document

def form_order(e):
    item1= document.getElementById('check1')
    item2= document.getElementById('check2')
    item3= document.getElementById('check3')
    item4= document.getElementById('check4')
    item5= document.getElementById('check5')
    item6= document.getElementById('check6')
    item7= document.getElementById('check7')
    item8= document.getElementById('check8')

    total= (float(item1.value)*item1.checked +
            float(item2.value)*item2.checked +
            float(item3.value)*item3.checked +
            float(item4.value)*item4.checked +
            float(item5.value)*item5.checked +
            float(item6.value)*item6.checked +
            float(item7.value)*item7.checked +
            float(item8.value)*item8.checked)
    
    name= document.getElementById('customer').value
    address= document.getElementById('address').value
    number= document.getElementById('contact').value
    summary=f'''
    Order for: {name}
    Address: {address}
    Contact No.: {number}
    '''

    if not name or not address or not number:
        display("Please complete customer information.", target="diva4", append=False)
        return
    
    display("", target="diva4", append=False)
    display(summary, target= 'diva4')
    display(f'The total amount of your order is {total} pesos. :)', target='diva4')


first_name = 'Clarisse'  # String
last_name = 'Casal'  # String
age = 15  # integer
weight = 81.5  # float 
is_a_new_student = False  # boolean 
sections = ['Emerald', 'Ruby', 'Sapphire', 'Topaz']  # List


restaurant_name = 'Sajarap'  # String
owner_name = 'Clarisse Casal'  # String
year_established = 2025  # integer
popular_item_price = 300.75  # float
has_delivery = True  # Boolean
product_names = ['Soda Pop', 'Saja Shrimp Crackers', 'Saja Kimchi', 'Saja Sausage', 'Saja Ramyeon', 'Saja Tteokbokki', 'Saja Gimbap', 'Saja Bulgogi']  # List
business_hours = {'Weekdays': '8 a.m. to 11 p.m.', 'Weekends': 'Closed'}  # Dictionary
menu_prices = { 
    'Soda Pop': 300.75,
    'Saja Shrimp': 150.00,
    'Saja Kimchi': 200.50,
    'Saja Sausage': 250.00,
    'Saja Ramyeon': 350.00,
    'Saja Tteokbokki': 350.00,
    'Saja Gimbap': 250.00,
    'Saja Bulgogi': 250.00
}  # Dictionary
common_allergens = ['wheat, sesame, eggs, milk']  # List
tax_rate = 0.15  # float

# header
display(restaurant_name, target="restaurant_name")
display(f"Owned by {owner_name} • Est. {year_established}", target="restaurant_details")

if document.getElementById("menu_title"):
    display("MENU", target="menu_title")

# table rows
display("Soda Pop", target="row1col1")
display(menu_prices["Soda Pop"], target="row1col2")

display("Saja Shrimp", target="row2col1")
display(menu_prices["Saja Shrimp"], target="row2col2")

display("Saja Kimchi", target="row3col1")
display(menu_prices["Saja Kimchi"], target="row3col2")

display("Saja Sausage", target="row4col1")
display(menu_prices["Saja Sausage"], target="row4col2")

display("Saja Ramyeon", target="row5col1")
display(menu_prices["Saja Ramyeon"], target="row5col2")

display("Saja Tteokbokki", target="row6col1")
display(menu_prices["Saja Tteokbokki"], target="row6col2")

display("Saja Gimbap", target="row7col1")
display(menu_prices["Saja Gimbap"], target="row7col2")

display("Saja Bulgogi", target="row8col1")
display(menu_prices["Saja Bulgogi"], target="row8col2")

# business hours
display(f"Weekdays: {business_hours['Weekdays']} • Weekends: {business_hours['Weekends']}", target="business_hours")
