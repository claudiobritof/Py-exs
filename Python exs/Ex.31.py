#Trip distance

dist = int(input("Total distance? \n"))
if dist <= 200:
    price = (dist * 0.50)
    print("Ticket price: R${:.2f}.".format(price))
else:
    price = (dist * 0.45)
    print("Ticket price: R$ {:.2f}.".format(price))