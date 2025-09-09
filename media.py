def calcular_media(notas):
    return sum(notas) / len(notas)

def classificar_media(media):
    if media >= 7.0:
        return "Aprovado(a) ✅"
    elif media >= 5.0:
        return "recuperação ⚠️"
    else:
        return "reprovado (a)❌"
    
def executar_calculo():
    nota1 = float (input("digite a nota 1: "))
    nota2 = float (input("digite a nota 2: "))
    nota3 = float (input("digite a nota 3: "))
    nota4 = float (input("digite a nota 4: "))

    media = calcular_media([nota1, nota2, nota3, nota4])

    print(f"\nMédia: {media:.2f}")

    print(classificar_media(media))


executar_calculo()