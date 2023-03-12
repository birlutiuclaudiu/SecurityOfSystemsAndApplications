section .text
  global _start
    _start:
      ; Store the argument string on stack
      xor  eax, eax 
      push eax          ; Use 0 to terminate the string
      push "/env"
      push "/bin"
      push "/usr"
      mov  ebx, esp     ; Get the string address

      ;se pun pe stiva variabilele de mediu
      ;incarcare variabila cccc=1234
      mov eax, "4***"  ;se inititlizeaza registrul eax cu octeti diferiti de 0
      shl eax, 24      ; se elimina cele 3 stelute cu octeti de 0 pein shiftarea la stanga cu 
      shr eax, 24      ; 3 octeti iar apoi cu shiftare la dreapta cu 3 octeti (little endian reprezentarea)
      push eax         ; se incarca pe stiva valoare continuarea stringului 4/0/0/0
      push "=123"      ; se incarca pe stiva o parte din stringul pentru variabila cccc
      push "cccc"      ; se incarca pe stiva numele varibilei de mediu
      mov esi, esp     ; se salveaza intr-un registru adresa de pe stiva a stringului cu variabila cccc
     
      xor eax, eax  ;reintitilizare eax 
      ;incarcare variabila bbb=5678
      push eax        ;se adauga terminator de string /0
      push "5678"     ;se incarca valoarea varibilei
      push "bbb="     ;se incepe stringul care defineste variabila bbb=5678
      mov ecx, esp    ;se salveaza in ecx valoarea variabile de mediu 
     ;incarcare variabila aaa=1234
      push eax        ;se pune terminatorul de string
      push "1234"     ;se incarca valoarea varibilei
      push "aaa="     ;se incepe stringul care defineste variabila aaa=1234
      mov edx, esp    ;se salveaza in edx valoarea variabile de mediu 
      
      ;
      xor eax, eax
      ; Construct the argument array argv[]
      push eax          ; argv[1] = 0
      push ebx          ; argv[0] points "/bin//sh"
      push eax          ;env[3] =0 NULL
      push esi          ;env[2] points to cccc=1234 
      push ecx          ;env[1] points to bbb=5678
      push edx          ;env[0] points to aaa=1234
      mov  ecx, esp     ; Get the address of argv[]
      ; For environment variable 
      mov edx, esp
   

      ; Invoke execve()
      xor  eax, eax     ; eax = 0x00000000
      mov   al, 0x0b    ; eax = 0x0000000b
      int 0x80
