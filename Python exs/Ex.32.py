#Leap year?

num = int(input("O ano é bissexto? \n"))

if num % 4 == 0:
    str_num = str(num)
    if str_num[-2:] == "00":
        if num % 400 == 0:
            print("{} é bissexto.".format(num))
        else:
            print("{} não é bissexto.".format(num))
    else:
        print("{} é bissexto.".format(num))
else:
    print("{} não é bissexto.".format(num))