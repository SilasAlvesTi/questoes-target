
if __name__ == '__main__':
    numero_a_ser_testado = 89
    anterior = 0
    proximo = 1
    soma = 1

    for i in range(0, 100):
        if(soma > numero_a_ser_testado):
            print("Numero informado nao pertence a sequencia de Fibonacci")
            break
        elif(soma == numero_a_ser_testado):
            print("Numero informado pertence a sequencia de Fibonacci")
            break

        soma = proximo + anterior
        anterior = proximo
        proximo = soma