#include <stdio.h>
#include <string.h>
#include <locale.h>

typedef struct _Endereco Endereco;

struct _Endereco {
	char logradouro[72];
	char bairro[72];
	char cidade[72];
	char uf[72];
	char sigla[2];
	char cep[8];
	char lixo[2];
};

int main(int argc, char** argv) {
    FILE *f;
	Endereco e;
	int cont = 0;
	long posicao, primeiro, ultimo, meio;

	if(argc != 2) {
		fprintf(stderr, "USO: %s [CEP]", argv[0]);
		return 1;
    }
    
    f = fopen("cep_ordenado.dat","r");
    
	fseek(f,0,SEEK_END);
	posicao = ftell(f);
	rewind(f);
	primeiro = 0;
    ultimo = (posicao/sizeof(Endereco))-1;
    
    while(primeiro <= ultimo) {
        cont++;
        meio = (primeiro+ultimo)/2;
        
        //Apontar a cabeça de leitura para o meio do arquivo e ler a qtd de bytes de uma linha:
        fseek(f, meio*sizeof(Endereco), SEEK_SET);
        fread(&e,sizeof(Endereco),1,f);
        
        //(atrncmp) é uma função que compara strings byte a byte:
        if(strncmp(argv[1],e.cep,8) == 0) {		
			printf("%.72s\n%.72s\n%.72s\n%.72s\n%.2s\n%.8s\n",e.logradouro,e.bairro,e.cidade,e.uf,e.sigla,e.cep);
			break;	
        }else if(strncmp(argv[1],e.cep,8) < 0) {
            meio = meio-1;
        }else {
            meio = meio+1;
        }
    }
    printf("\n Numero de enderecos lidos: %d\n", cont);
    
    fclose(f);
    return 0;
}

