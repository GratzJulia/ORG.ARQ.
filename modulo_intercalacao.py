import struct

registroCEP1 = struct.Struct("72s72s72s72s2s8s2s")
registroCEP2 = struct.Struct("72s72s72s72s2s8s2s")
colunaCEP=5

qtd_arq = 8
i = 0

while i < 14:
     # 14 é o num fixo de intercalações a serem feitas!
     pos_atual = "A" + str(i)
     prox = "A" + str(i+1)
     resultado = "A" + str(qtd_arq)
     qtd_arq = qtd_arq + 1
     
     ### Os 3 arquivos são abertos.
     with open(pos_atual, "rb") as primeiro:
          with open(prox, "rb") as segundo:
               saida = open(resultado, "wb")
              
               primeiro.seek(0,2)
               fim1 = primeiro.tell()
               primeiro.seek(0,0)
               segundo.seek(0,2)
               fim2 = segundo.tell()
               segundo.seek(0,0)
              
               #Leitura da 1ª linha de cada arq de entrada.
               linha1 = primeiro.read(registroCEP1.size)
               linha2 = segundo.read(registroCEP2.size)
               
               while primeiro.tell() < fim1 and segundo.tell() < fim2:
                  #Enquanto os 2 arq de entrada não acabarem...
                  registro1 = registroCEP1.unpack(linha1)
                  registro2 = registroCEP2.unpack(linha2)
               
                  if registro1[colunaCEP] <= registro2[colunaCEP]:
                      saida.write(linha1)
                      linha1 = primeiro.read(registroCEP1.size)       
                  else:
                      saida.write(linha2)
                      linha2 = segundo.read(registroCEP2.size)

               while primeiro.tell() < fim1:
                    saida.write(linha1)
                    linha1 = primeiro.read(registroCEP1.size)

               while segundo.tell() < fim2:
                    saida.write(linha2)
                    linha2 = segundo.read(registroCEP2.size)
               
               saida.close()
     i=i+2

