print("Em que ano você nasceu?")
nascimento = input()
nascimento = int(nascimento)
print("Para qual ano você quer saber sua idade?")
ano = input()
ano = int(ano)
idadeEm2025 = ano - nascimento
print("No ano", ano ,"você terá", idadeEm2025 , "anos!" )
