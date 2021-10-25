import JAClass as jo

print('------- Customer Details -------')
name = input('Enter name : ')
address = input('Enter address : ')
phone = input('Enter phone : ')
customer = jo.Customer(name, address, phone)
print()


print('--------- Car Details ----------')
make = input('Enter manufacturer : ')
model = input('Enter car model : ')
year = int(input('Enter year of manufacture : '))
car = jo.Car(make, model, year)
print()


print('------- Charges Details --------')
pcharge = float(input('Enter parts charges : '))
lcharge = float(input('Enter labour charges : '))
charges = jo.ServiceQuote(pcharge, lcharge)
print()


print('\nCustomer Information')
print("Customer's name is", name,'.', "Customer's address is", address,'.', "Customer's phone number is", phone,'.')


print('\nCar Information')
print(f'Manufacturer = {car.get_make()}\n'
      f'Model : {car.get_model()}\nYear : {car.get_year()}')

print('\nCharges Information')
print(f'Parts Charges : {charges.get_parts_charges()}\n'
      f'Labour Charges : {charges.get_labour_charges()}\n'
      f'Sales Tax : {charges.get_sales_tax()}\n'
      f'Total Charges : {charges.get_total_charges()}')
