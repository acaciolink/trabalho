def voto(nasc):
    from datetime import date
    data = date.today().year
    idade = data - nasc
    if 65 > idade >= 18:
        return 'VOTO OBRIGATÓRIO!'
    elif idade < 16:
        return 'NÃO VOTA!'
    else:
        return 'VOTO OPICIONAL!'

ano_nascimento = int(input("Ano de nascimento: "))
print(voto(ano_nascimento))