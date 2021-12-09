#Number 2
from os import CLD_DUMPED


cupCake = open("CupcakeInvoices.csv")

#Number 3
# for cupCakes in cupCake:
#     print(cupCakes)

#number4

# choco = ""
# straw =""
# vanilla = ""

# for cup in cupCake:
#     cup = cup.rstrip('\n').split(',')
#     for value in cup:
#         if value == "Chocolate":
#             print(value)
            
#         elif value == "Strawberry":
#             print(value)
            
#         elif value == "Vanilla":
#             print(value)
            
#     print(choco,straw,vanilla)


#Number 5

# for invoiceTotal in cupCake:
#    arr = (invoiceTotal.split(','))

#    print(float(arr[3])* (float(arr[4])))
   
   
#Number 6
total=0
for invoiceTotal in cupCake:
    arr = (invoiceTotal.split(','))
    total += (float(arr[3])* (float(arr[4])))
    print(total)
    
#Number 7
cupCake.close()


