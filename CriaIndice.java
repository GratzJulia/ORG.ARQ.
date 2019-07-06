package Utils;

import java.io.*;
import java.util.ArrayList;

public class CriaIndice {

    public static void main(String[] args) throws Exception {
        
        String registro, nis;
        String dados[];
        long pos_ArqPrincipal;
        RandomAccessFile arqPrincipal = new RandomAccessFile("bolsa.csv", "r");
        RandomAccessFile index = new RandomAccessFile("indice.csv", "rw");
        index.setLength(0);
        arqPrincipal.readLine();    //pular a linha0 pq ela é o cabeçalho!
    
        while (arqPrincipal.getFilePointer() < arqPrincipal.length()) {
            pos_ArqPrincipal = arqPrincipal.getFilePointer();
            registro = arqPrincipal.readLine();

            dados = registro.split("\t");
            nis = dados[7]; //7 é o num da coluna onde estão os valores de NIS
            String idPrincipal = String.format("%09d", pos_ArqPrincipal);
            index.writeBytes(nis + " " + idPrincipal + "\n");
        }
        System.out.println("O arquivo indice.csv possui os números de NIT (não ordenados) e as suas posições de referência para o arquivo bolsa.csv.");

        arqPrincipal.close();
        index.close();
    } //fim da Main
} //fim da classe