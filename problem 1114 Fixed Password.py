while(True):
    try:
        a = int(input())
        if(a==2002):
            print("Acesso Permitido")
            break
        else:
            print("Senha Invalida")
    except EOFError:
        break