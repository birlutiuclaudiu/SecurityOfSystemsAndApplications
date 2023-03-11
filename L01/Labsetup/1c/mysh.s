section .text
  global _start
    _start:
      xor eax, eax    ; initializarea la 0
      mov ax, "la"    ; se pune restul din stringu "ls -la", adica stringul "la"
                      ; cei doi octeti sunt pusi pe ultimii doi octeti (cei mai din stanga-little endian) ai 
                      ; registrului eax; astfel registrul eax = x00x00xx61x6c, unde 61-a, 6c-l
                      ; octelul al doilea va reprezenta sfarsitul sirului /0
      push eax        ; incarcarea pe stiva a restului din sir la
      push "ls -"     ; incarcarea inceputului de argument "ls -la"; se vor pune primii 4 octeti pe stiva din 
                      ; sir 
      mov ecx, esp    ; stocarea in ecx a inceputlui de string "ls -la"

      ;incarcarea pe stiva a argumentului -c
      xor eax, eax
      mov ax, "-c"   ; se pun cei doi octeti ai sirului -c pe ultimii doi octeti ai registrului eax
                     ; eax = x00x00x63x2d, unde x63 =c, x2d=-; aldoilea octet al registrului reprezinta 
                     ; terminatorul de string (/0)
      push eax       ; incarcarea pe stiva a stringului
      mov edx, esp   ; stocarea in ecx a inceputlui de string "-c"
      
      ; Store the argument string on stack
      xor  eax, eax 
      push eax          ; Use 0 to terminate the string
      push "//sh"
      push "/bin"
      mov  ebx, esp     ; Get the string address
      ; Construct the argument array argv[]
      push eax          ; argv[3] = 0
      push ecx          ; argv[2] points "ls -la"
      push edx          ; argv[1] points "-c"
      push ebx          ; argv[0] points "/bin//sh"
      mov  ecx, esp     ; Get the address of argv[]
   
      ; For environment variable 
      xor  edx, edx     ; No env variables 

      ; Invoke execve()
      xor  eax, eax     ; eax = 0x00000000
      mov   al, 0x0b    ; eax = 0x0000000b
      int 0x80
