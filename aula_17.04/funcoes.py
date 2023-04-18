def mysoma(valor,percentual):
    return ((1+(percentual/100))*valor)


def divisao(a,b):
    return a//b,a%b


def divisao_v2(a,b):
    a += 2
    b += 1
    return a//b,a%b


def divisao_v3(lista):
    lista[0] += 2
    lista[1] += 1
    return lista[0]//lista[1], lista[0]%lista[1]


def mmc(a,b):
    mmc = 1
    while mmc % a != 0 or mmc % b != 0:
        mmc+=1
    return mmc


def mdc(a,b):
    mdc = max(a,b)

    while a % mdc != 0 or b % mdc != 0:
        mdc-= 1
    return mdc
