"""Generate sales report showing total melons each salesperson sold."""




f = open('sales-report.txt')

# for line in f:
#     line = line.rstrip()
#     entries = line.split('|')
#     salesperson = entries[0]
#     melons = int(entries[2])

#     if salesperson in salespeople:
#         print(salespeople)
#         position = salespeople.index(salesperson)
#         melons_sold[position] += melons
        
#     else:
#         salespeople.append(salesperson)
#         melons_sold.append(melons)


# for i in range(len(salespeople)):
#     print(f'{salespeople[i]} sold {melons_sold[i]} melons')

sales_dic ={}
total = 0
for line in f:
    #gets rid of white space 
    line = line.rstrip()
    #converts it in array
    entries = line.split('|')
    #gets names
    salesperson = entries[0]
    #gets # of melons
    melons = int(entries[2])
    #checks if the name its in dic and if it is it adds to the value
    if salesperson in sales_dic:
        sales_dic[salesperson] += melons
    #if the dic does not have the key then it adds it
    else:
        sales_dic[salesperson] = melons
#print values
for key,value in sales_dic.items():
    print(f'{key} sold {value} melons')



        
