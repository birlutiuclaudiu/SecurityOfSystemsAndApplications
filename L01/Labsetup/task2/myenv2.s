section .text
  global _start
    _start:
		BITS 32 ;utilizarea unui bus de date de 32 de biți de către procesor.
		jmp short two ;se sare cu execyutia la eticheta "two" modificandu-se
		  ;fluxul de execuție a programului; cuvantul short indica faptul ca 
		  ;eticheta este în interiorul aceluiași segment de cod, adică distanța 
		  ;până la etichetă este de cel mult 127 de octeți
    one:
		pop ebx     		 ;e adresa sirului '/usr/bin/env****AAAAa=11BBBBb=22CCCC'
		xor eax, eax 		 ;se initializeaza cu 0 fara a introduce octeiti de 0 in codul masina
		mov [ebx+12], eax    ;se sparge sirul de caractere usr/bin/env; **** sunt inlocuite cu octeti de 0
		mov [ebx+16], ebx    ;se ia valoare adresei sirului de inceput si salveaza in AAAAA
        mov [ebx+20], eax    ;NULL pentru argumente
		
		;for environment
		;definire variabila a=11
		mov [ebx+28], eax   ;terminator string a=11
		lea ecx, [EBX+24]  
		mov [EBX+40], ecx   ;se pune adresa sirului a=11 in EEEE
		;definire variabila b=22
        mov [EBX+36], eax   ;terminatorul de string b=22
		lea ecx, [EBX+32]  
		mov [EBX+44], ecx   ;se pune adresa sirului b=22 in FFFF
        mov [EBX+48], eax   ;se pune NULL pe ultima valoare env[2] =NULL

		lea ecx, [ebx+16]   ;se incarca registru ecx cu adresa sirului de argumente 
        lea edx, [EBX+40]   ;se incarca registru edx cu adresa sirului de variabile de mediu
		mov al,  0x0b       ;se pune codul instructiunii execve
		int 0x80            ;se face apelul functiei execve
     two:
		call one ;se face un salt la eticheta one, dar de data aceasta se foloseste 
		;instruvtiunea de apelare, ceea ce inseamna ca se va pastra o adresa de retur pe stiva 
		; la instructiunea urmatoare dupa ce se executa pasii de la eticheta 2, dar instructiunea
		; urmatoarea reprezinta de fapt declararea unei variabile, ceea ce arata faptul ca pe 
		; stiva vom avea in varf stringul de mai jos
		db '/usr/bin/env' ;declararea stringului, a carui adresa este pusa pe stiva 12
		db '****'       ;12: terminator string comanda
		db 'AAAA'       ;16: '/usr/bin/env' argument
		db 'BBBB'       ;20: NULL
		db "a=11"       ;24: env[1] -> nume=valoare pentru variabila b=22  
		db "****"       ;28: terminatorul de string pentru a=11
		db "b=22"       ;32: env[1] -> nume=valoare pentru variabila b=22  
		db '****'       ;36: terminator pentru stringul b=22
		db "EEEE"       ;40: place holder for env[0] a=11
		db "FFFF"       ;44: place holder for env[1] b=22
		db "NNNN"       ;48: env[2] NULL
		
		