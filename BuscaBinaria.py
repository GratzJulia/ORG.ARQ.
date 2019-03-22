import struct
import sys

if len(sys.argv) != 2:
    print("USO %s [CEP]" %sys.argv[0])
    quit()

registroCEP = struct.Struct("72s72s72s72s2s8s2s")
colunaCEP = 5

print("Tamanho da estrutura = tamanho de 1 linha: %d" %registroCEP.size)

with open("cep_ordenado.dat", "rb") as f:
    f.seek(0,2)
    tamanhoArquivo = f.tell()
    f.seek(0,0)
    fim = tamanhoArquivo/registroCEP.size
    print("Quantidade de linhas: %d" %fim)
    inicio = 0
    loop = 0
    
    while inicio <= fim:
        loop = loop+1
        meio = int((inicio+fim)/2)
        f.seek(meio*registroCEP.size, 0)
        linha = f.read(registroCEP.size)
        registro = registroCEP.unpack(linha)
        
        if registro[colunaCEP].decode() == sys.argv[1]:
            print("Seu endereço foi encontrado!")
            for i in range(0, 6):
                print(registro[i])
            break
        if registro[colunaCEP].decode() < sys.argv[1]:
            inicio = meio + 1

        if registro[colunaCEP].decode() > sys.argv[1]:
            fim = meio - 1

print("A busca binária foi feita %d vezes." %loop)
