#Salary changes

sal = float(input("Digite o salário: \n"))
if sal > 1250:
    aum = (sal + (sal * 10/100))
    print("Com o aumento de 10%, o salário foi de R${:.2f} para R${:.2f}.".format(sal, aum))
else:
    aum = (sal + (sal * 15/100))
    print("Com o aumento de 15%, o salário foi de R${:.2f} para R${:.2f}.".format(sal, aum))