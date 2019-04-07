import struct
import modulo_intercalacao

registroCEP = struct.Struct("72s72s72s72s2s8s2s")
colunaCEP   = 5
qtd_arq     = 8
i           = 0

with open("cep_ordenado.dat", "rb") as entrada:
    entrada.seek(0,2)
    tamanhoArquivo = entrada.tell()
    entrada.seek(0,0)
    fim = tamanhoArquivo/registroCEP.size
    saida = open("80_aleatorio.txt", "wb")

    for i in range(0,80):
        entrada.seek(8735*i * 300, 0)
        linha = entrada.read(registroCEP.size)
        registro =registroCEP.unpack(linha)
        saida.write(linha)
    saida.close()

    with open("80_aleatorio.txt", "rb") as entrada2:
        while i < qtd_arq:
            
            nome_arquivo = "A" + str(i)
            proximo = "A" + str((i+1))
            saida2 = open(nome_arquivo, "wb")

            for j in range(0, 10):
                linha2 = entrada2.read(registroCEP.size)
                saida2.write(linha2)

            while proximo:
                aux = "A" + str(qtd_arq)
                modulo_intercalacao.intercalar(nome_arquivo, proximo, aux)
                qtd_arq = qtd_arq + 1

            i = i+1
            saida2.close()
