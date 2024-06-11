# A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result. It is defined using the 'def' keyword.

bill = 175.00

tax_rate = 15

total_tax = (bill * tax_rate) / 100.00

print('Total tax is', total_tax)

def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100.00 , 2) # the round function

print('Total tax is', calculate_tax(145.00, 20))

print('Total tax is', calculate_tax(164.33, 22))
