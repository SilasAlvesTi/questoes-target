import json

def ler_arquivo():
    with open('dados.json', 'r') as dados:
        dados = json.load(dados)
    return dados

def menor_faturamento(faturamentos):
    menor = faturamentos[0]['valor']
    for faturamento in faturamentos:
        if faturamento['valor'] < menor:
            menor = faturamento['valor']
    return menor

def maior_faturamento(faturamentos):
    maior = faturamentos[0]['valor']
    for faturamento in faturamentos:
        if faturamento['valor'] > maior:
            maior = faturamento['valor']
    return maior

def media_de_faturamentos(faturamentos):
    soma = 0
    soma_dias_com_faturamento = 0
    for faturamento in faturamentos:
        if faturamento['valor'] == 0:
            continue
        soma += faturamento['valor']
        soma_dias_com_faturamento += 1
    return soma/soma_dias_com_faturamento

def dias_faturamento_e_superior_a_media(faturamentos, media):
    dias = 0
    for faturamento in faturamentos:
        if faturamento['valor'] > media:
            dias += 1
    return dias


if __name__ == '__main__':
    dados = ler_arquivo()
    print(f'{menor_faturamento(dados)} foi o menor faturamento diario')
    print(f'{maior_faturamento(dados)} foi o maior faturamento diario')
    media = media_de_faturamentos(dados)
    print(f'{dias_faturamento_e_superior_a_media(dados, media)} é o numero de dias em que o faturamento diario superou a media mensal')