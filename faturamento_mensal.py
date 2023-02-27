
if __name__ == '__main__':
    faturamentos = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53,
    }

    total = sum(faturamentos.values())
    print(total)
    for estado in faturamentos:
        print(f'O estado {estado} teve {(faturamentos[estado]/total) * 100}% de participação')