min_salary = 30000.0
min_years = 2

salary = float(input('Enter your annual salary:'))

years_on_job = int(input('Enter the number of' + ' years employed:'))


if salary >= min_salary:
    if years_on_job >= min_years:
        print('You qualify for the loan.')
    else:
        print('You must have emploted', \
              'for at least', min_years, \
              'years to qualify.')
else:
    print('You must earn at least $', \
          format(min_salary, ',.2f'), \
          ' per year to qualify.', sep='')
