produto_quantidade = input()
produto = int(produto_quantidade.split(" ")[0])
quantidade = int(produto_quantidade.split(" ")[1])

if produto == 1:
    valor_unitario = 4
elif produto == 2:
    valor_unitario = 4.5
elif produto == 3:
    valor_unitario = 5
elif produto == 4:
    valor_unitario = 2
elif produto == 5:
    valor_unitario = 1.50

valor_total = valor_unitario * quantidade

print("Total: R$", "%.2f" % valor_total)
