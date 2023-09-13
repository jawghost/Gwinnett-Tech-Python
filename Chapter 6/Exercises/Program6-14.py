# This program displays the records that are
# in the employees.txt file.

def main():
    emp_file = open('employees.txt', 'r')

    name = emp_file.readline()

    while name != '':
        id_num = emp_file.readline()

        dept = emp_file.readline()

        name = name.rstrip('\n')
        id_num = id_num.rstrip('\n')
        dept = dept.rstrip('\n')

        print('Name:', name)
        print('ID:', id_num)
        print('Dept:', dept)
        print()

        name = emp_file.readline()

    emp_file.close()

main()
