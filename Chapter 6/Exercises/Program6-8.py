# This program prompts the user for sales amounts
# and writes those amounts to the sales.txt file.

def main():
    #Get the number of days.
    num_days = int(input("Fpr how many days do ' + \
    'you have sales? '))
    #open a new file named sales.txt.
    sales_file = open('sales.txt", 'w')

    # Get the amount of sales for each day and write
    #it to the file.
    for count in range(1, num_days + 1):
        # Get the sales for a day.
        sales = float(input('Enter the sales for day #' + \
                            str(count) + ': '))

        #Write the sales amount to the file.
        sales_file.write(Str(sales) + '\n')

        #Close the file.
        sales_file.close()
        print('Data written to sales.txt.')

# call the main function
main()
