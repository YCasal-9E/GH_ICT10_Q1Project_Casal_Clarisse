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
restaurant_name = 'Sajarap'  # String
owner_name = 'Clarisse Casal'  # String
year_established = 2025  # integer
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
def safe_display(content, target):
    if document.getElementById(target):
        display(content, target=target)

# restaurant header
safe_display(restaurant_name, "restaurant_name")
safe_display(f"Owned by {owner_name} • Est. {year_established}", "restaurant_details")

# menu title
safe_display("MENU", "menu_title")

# table rows
safe_display("Soda Pop", "row1col1")
safe_display(menu_prices["Soda Pop"], "row1col2")

safe_display("Saja Shrimp", "row2col1")
safe_display(menu_prices["Saja Shrimp"], "row2col2")

safe_display("Saja Kimchi", "row3col1")
safe_display(menu_prices["Saja Kimchi"], "row3col2")

safe_display("Saja Sausage", "row4col1")
safe_display(menu_prices["Saja Sausage"], "row4col2")

safe_display("Saja Ramyeon", "row5col1")
safe_display(menu_prices["Saja Ramyeon"], "row5col2")

safe_display("Saja Tteokbokki", "row6col1")
safe_display(menu_prices["Saja Tteokbokki"], "row6col2")

safe_display("Saja Gimbap", "row7col1")
safe_display(menu_prices["Saja Gimbap"], "row7col2")

safe_display("Saja Bulgogi", "row8col1")
safe_display(menu_prices["Saja Bulgogi"], "row8col2")

# business hours
safe_display(
    f"Weekdays: {business_hours['Weekdays']} • Weekends: {business_hours['Weekends']}",
    "business_hours"
)
