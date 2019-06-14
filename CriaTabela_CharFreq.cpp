#include <cstdio>
#include <iostream>
using namespace std;

int main() {
  FILE *f = fopen("arq.txt", "r");
  char caracteres[256];
  int freq_caracteres[256];

  for(int i=0; i<256; i++) {
    freq_caracteres[i] = 0;
    caracteres[i] = ' ';
  }

  // Contabiliza a frequencia dos caracteres:
  int aux = 0;
  while(!feof(f)) {
    aux = fgetc(f);
    freq_caracteres[aux] = freq_caracteres[aux] + 1;
    caracteres[aux] = (char)aux;
  }

  // Visualizacao do resultado da tabela:
  for(int i=0; i<256; i++) {
    if(freq_caracteres[i] > 0) {
      cout << "Código ASCII: " << i << " | Char: " << caracteres[i] << " | Frequência: " << freq_caracteres[i] << "\n";
    }
  }

  fclose(f);
  return 0;
}