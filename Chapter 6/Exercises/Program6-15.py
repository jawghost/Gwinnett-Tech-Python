def main():
    amother = 'y'

    coffee_file = open('coffee.txt', 'a')

    while another == 'y' or another == 'Y':
        print('Enter the following coffee data:')
        descr = input('Description: ')
        qty = int(input('Quantity (in pounds): '))

        coffee_file.write(descr + '\n')
        coffee_file.write(str(qty) + '\n')

        print('Do you want to add another record?')
        another = input('Y = yes, anything else = no: ')

    coffee_file.close()
    print('Data appended to coffee.txt.')

main()
