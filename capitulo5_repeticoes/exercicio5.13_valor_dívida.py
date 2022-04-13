# Exercício 05-13: Cálculo do pagamento de uma dívida com pagamentos mensais
# Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.

dívida = float(input("Dívida: "))
taxa = float(input("Juros (Ex.: 3 para 3%): "))
pagamento = float(input("Pagamento mensal:"))
mês = 1
if (dívida * (taxa/100) > pagamento):
    print("Sua dívida não será paga nunca, pois os juros são superiores ao pagamento mensal.")
else:
    saldo = dívida
    juros_pago = 0
    while saldo > pagamento:
        juros = saldo * taxa / 100
        saldo = saldo + juros - pagamento
        juros_pago = juros_pago + juros
        print(f"Saldo da dívida no mês {mês} é de R${saldo:6.2f}.")
        mês = mês + 1
    print(f"Para pagar uma dívida de R${dívida:8.2f}, a {taxa:5.2f} % de juros,")
    print(f"você precisará de {mês - 1} meses, pagando um total de R${juros_pago:8.2f} de juros.")
    print(f"No último mês, você teria um saldo residual de R${saldo:8.2f} a pagar.")
