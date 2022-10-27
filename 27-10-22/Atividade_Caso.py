# Atividade Turno

print("em que turno você estuda?")
turno = str(input("digite M para matutino, V para vespertino ou N para noturno: "))
turno = turno.lower()
match turno:
    case "m":
        print("Bom dia")
    case "v":
        print("Boa tarde")
    case "n":
        print("Boa noite")
    case _:
        print("Valor invalido")
