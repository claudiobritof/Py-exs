#Employee Salary

salario = float(input("Digite seu salário: \nR$"))
aumento = salario * 15/100
print("O salário do funcionário, que é de R${:.2f}, vai subir para R${:.2f} com o aumento de 15%.".format(salario, salario + aumento))