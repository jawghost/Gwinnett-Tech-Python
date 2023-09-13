min_salary = 30000.0
min_years = 2

salary = float(input('Enter your annual salary: '))

years_on_job = int(input('Enter the number of' + ' years employed:'))

if salary >= min_salary and years_on_job >=min_years:
    print('You qualify for the loan.')
else:
    print('You do not qualify for this loan.')
