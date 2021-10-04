
#/// Part 2///

#/// Problem 2///
cup_cakes = open('Cupcakeinvoices.csv')

#/// Problem 3///


# for data in cup_cakes:
#     print(data)


#/// Problem 4///

# cupcakes_sold = []

# for data in cup_cakes:
#     cupcakes_sold.append(data.split(',')[2])

# print(cupcakes_sold)

# total_chocolate = 0
# total_vanilla = 0
# total_strawberry = 0

# for totals in cupcakes_sold:
    
#     totals = totals.split(',')
#     for flavor in totals:
#         if flavor == 'Chocolate':
#             total_chocolate += 1
#         elif flavor == "Vanilla":
#             total_vanilla += 1
#         elif flavor == "Strawberry":
#             total_strawberry += 1

# print("total Chocolate", total_chocolate, "Total Strawberry", total_strawberry, "Total Vanilla", total_vanilla)



#///problem 5 & 6///

total = []

for num in cup_cakes:
    num = num.rstrip('\n').split(',')
    quantity = int(num[3])*float(num[4])
    total.append(quantity)


def sum(list):
    sum = 0
    
    for i in list:
        sum = sum + i
    return(round(sum))

print(sum(total))

cup_cakes.close()

import matplotlib.pyplot as plt

plt.bar(['chocolate', 'Vanilla', 'Strawberry'], [total_chocolate, total_vanilla, total_strawberry])

plt.show()

# Im not sure why I have to comment the previous codes from problem 2 - 4 for the 5 - 6 code to work. But everything should work just fine