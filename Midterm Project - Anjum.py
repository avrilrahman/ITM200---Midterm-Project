# Import the packages/libraries
import csv
import matplotlib.pyplot as plt

# Step 1: Reading the CSV file
with open('Data.csv', mode='r') as fCSV:
    cv = csv.reader(fCSV)

# Step 2: The total sale from 2012-2021
with open('Data.csv') as excel:
    read = csv.reader(excel)
    next(read)

    total_sales = {}
    for i in read:
        year = int(i[0])
        if year < 2012 or year > 2021:
            continue
        sales_data = []
        for x in i[1:]:
            if x != '':
                sales_data.append(int(x))
        total_sales[year] = sum(sales_data)

with open('stats.txt', mode='w') as file:
    file.write('The Total Sales from 2012-2021 are:\n')

    for year, sales in total_sales.items():
        file.write(str(year) + ': ' + str(sales) + '\n')

# Step 3: The bar plot of total sales for each year (2012 to 2021)
import matplotlib.pyplot as plt

years = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
sales = [1665063, 1728140, 1851645, 1867498, 1948375, 2029668, 1987373, 1921449, 1661560, 1638340]

plt.figure(1)

plt.bar(years, sales)

plt.title('The Total Car Sales Per Year')
plt.xlabel('Year')
plt.ylabel('Total Sales')

plt.show()

# Step 4: The sales estimation
sales_2021 = [110903, 114510, 153722, 154105, 152141, 162549]
sales_2022 = [36922, 39082, 55611, 57110, 56991, 66514]

total_sales_2021 = sum(sales_2021)
total_sales_2022 = sum(sales_2022)

sale_growth_rate = (total_sales_2022 - total_sales_2021) / total_sales_2022

with open('stats.txt', mode='a') as file:
    file.write('The Sales Growth Rate is: ' + str(round(sale_growth_rate, 2)))

num_sales2022 = []

for month in range(7, 13):
    month_year_21 = sales_2021[month - 7]

    num_sale = month_year_21 * (1 + sale_growth_rate)

    num_sales2022.append(num_sale)

with open('stats.txt', 'a') as file:
    file.write('\nThe Estimated Sales For The Last Six Months of 2022:\n')
    file.write('July 2022: ' + str(round(-num_sales2022[0])) + '\n')
    file.write('Aug 2022: ' + str(round(-num_sales2022[1])) + '\n')
    file.write('Sept 2022: ' + str(round(-num_sales2022[2])) + '\n')
    file.write('Oct 2022: ' + str(round(-num_sales2022[3])) + '\n')
    file.write('Nov 2022: ' + str(round(-num_sales2022[4])) + '\n')
    file.write('Dec 2022: ' + str(round(-num_sales2022[5])) + '\n')

# Step 5: The horizontal bar plot
sales_months = ['July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
num_sales2022 = [-num_sales2022[0], -num_sales2022[1], -num_sales2022[2], -num_sales2022[3], -num_sales2022[4],
                 -num_sales2022[5]]

plt.figure(2)
plt.barh(sales_months, num_sales2022)

plt.title('The Estimated Sales For The Last Six Months of 2022')
plt.ylabel('Sales')
plt.xlabel('Months')

plt.show()
