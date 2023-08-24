print('''Quanto dinheiro você ganharia se lavasse 12 carros,
      cobrando R$ 12,50 por lavagem?''')

x= 12.50*12
valor="R${:,.2f}".format(x)

print("\n")
print("Você ganharia", valor,".")
