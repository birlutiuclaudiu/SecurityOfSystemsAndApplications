#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main()
{
    char* fn = "/tmp/XYZ"; //calea spre fiserul XYZ din directorul tmp unde se va scrie inputul utilizatorului
    char buffer[60];       //declararea unui buffer de 60 de bytes
    FILE* fp;             

    /* get user input */
    scanf("%50s", buffer);                              //se citeste intrarea de la stdin

    /**
     * aceasta verificare cu access verifica scrierea accidentala a fisierelor altora, 
     * programul verifica mai intai daca 
     * ID de utilizator real are permisiunea de acces la fisierul /tmp/XYZ
    */
    if (!access(fn, W_OK)) {
        //timp in care atacatorul poate schimba printr-un symlink destinatia fisierului /tmp/XYZ la /etc/passwd
        //VULNERABILITATE
        sleep(10);                                      //simularea unei masini lente
        fp = fopen(fn, "a+");                           //se dechide fisierul in modul append
        if (!fp) {
            perror("Open failed");
            exit(1);
        }
        fwrite("\n", sizeof(char), 1, fp);            //se pune new line la fiecare scriere
        fwrite(buffer, sizeof(char), strlen(buffer), fp);  //se scrie inputul in fisier (pe noua linie)
        fclose(fp);
    } else {
        printf("No permission \n");
    }

    return 0;
}
