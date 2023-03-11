section .text
  global _start
    _start:
		BITS 32 ;utilizarea unui bus de date de 32 de biți de către procesor.
		jmp short two ;se sare cu execyutia la eticheta "two" modificandu-se
		  ;fluxul de execuție a programului; cuvantul short indica faptul ca 
		  ;eticheta este în interiorul aceluiași segment de cod, adică distanța 
		  ;până la etichetă este de cel mult 127 de octeți
    one:
		pop ebx     		;e adresa sirului '/usr/bin/env****AAAAa=11BBBBb=22CCCC'
		xor eax, eax 		;se initializeaza cu 0 fara a introduce octeiti de 0 in codul masina
		mov [ebx+12], eax   ;se sparge sirul de caractere usr/bin/env; **** sunt inlocuite cu octeti de 0
		mov [ebx+16], ebx   ;octetii AAAA vor fi inlocuiti cu adresa sirului de inceput
		mov [ebx+24], eax   ;octetii BBBB vor fi inlocuiti cu 0000
        mov [ebx+28], eax   ;octetii CCCC vor fi inlocuiti cu 0000
		lea ecx, [ebx+16]   ;se incarca registru ecx cu adresa sirului 
		lea edx, [ebx+20]   ;se incarca registru edx cu adresa sirului
		mov al,  0x0b       ;se pune codul instructiunii execve
		int 0x80            ;se face apelul functiei execve
     two:
		call one ;se face un salt la eticheta one, dar de data aceasta se foloseste 
		;instruvtiunea de apelare, ceea ce inseamna ca se va pastra o adresa de retur pe stiva 
		; la instructiunea urmatoare dupa ce se executa pasii de la eticheta 2, dar instructiunea
		; urmatoarea reprezinta de fapt declararea unei variabile, ceea ce arata faptul ca pe 
		; stiva vom avea in varf stringul de mai jos
		db '/usr/bin/env****AAAAa=12BBBBCCCC' ;declararea stringului, a carui adresa este pusa pe stiva 