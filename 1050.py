input_ddd = input()

ddds_cadastrados = {"61": "Brasilia", "71": "Salvador", "11": "Sao Paulo", "21": "Rio de Janeiro",
                    "32": "Juiz de Fora", "19": "Campinas", "27": "Vitoria", "31": "Belo Horizonte"}

if input_ddd in ddds_cadastrados.keys():
    print(ddds_cadastrados.get(input_ddd))
else:
    print("DDD nao cadastrado")