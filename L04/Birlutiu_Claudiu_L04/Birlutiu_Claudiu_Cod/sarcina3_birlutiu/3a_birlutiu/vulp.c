#define _POSIX_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

int main()
{
    char* fn = "/tmp/XYZ"; //calea spre fiserul XYZ din directorul tmp unde se va scrie inputul utilizatorului
    char buffer[60];       //declararea unui buffer de 60 de bytes
    FILE* fp;             

    /* get user input */
    scanf("%50s", buffer);      //se citeste intrarea de la stdin
    //AICI am schimbat partea de vulnerabilitate cu anularea privilegiului de root pentru deschiderea fisierului
    uid_t real_uid = getuid();  //obtine id user real
    uid_t eff_uid = geteuid();  //obtine id user efectiv
    setuid(real_uid);           //se va dezactiva privilegiul de root!
    fp = fopen(fn, "a+");       //se dechide fisierul in modul append
    if (fp) {
        fwrite("\n", sizeof(char), 1, fp);                  //se pune new line la fiecare scriere
        fwrite(buffer, sizeof(char), strlen(buffer), fp);  //se scrie inputul in fisier (pe noua linie)
        fclose(fp);
    } else {
        printf("No permission User_real:%d ; User_efectiv: %d \n", real_uid, eff_uid);
    }
    setuid(eff_uid); //se reface privilegiul de root

    return 0;
}
