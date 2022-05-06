# Exercício 05-12: Cálculo do juros de uma poupança com depósito 
# Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
# Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.

depósito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros (Ex.: 3 para 3%): "))
investimento = float(input("Depósito mensal: "))
mês = 1 # mês é um contador, pois o valor a acrescentar é constante *
saldo = depósito #acumula valores da taxa a cada repetição, valores variam.
while mês <= 24:
    saldo = saldo + (saldo * (taxa / 100)) + investimento
    print(f"Saldo do mês {mês} é de R${saldo:6.2f}.")
    mês = mês + 1 #*
print(f"O ganho obtido com os juros foi de R${saldo - depósito:6.2f}.")