#include <array>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <openssl/rand.h>

#include "evp-encrypt.hpp"
#include "utils.hpp"

using namespace std;

/**
 * Aceasta functie verifica daca cifrul dat e continut in cel rezultat
*/
bool contains_cipher_dat(Bytes cipher_dat, Bytes rezultat){
    if(cipher_dat.size() > rezultat.size()) return false;
    for(size_t i=0; i<cipher_dat.size(); i++){
        if(cipher_dat[i] != rezultat[i])
            return false;
    }
    return true;
}

int main(int argc, char const *argv[]){
    // key, iv1, iv2
    array<Byte, KEY_SIZE> key;
    array<Byte, BLOCK_SIZE> iv;
    //////////////////////CREARE IV////////////////////////////////////////
    Bytes iv_bytes= {0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff, 0x00, 0x99, 0x88, 
                                0x77, 0x66, 0x55, 0x44, 0x33, 0x22, 0x11};
    for (unsigned int i = 0; i < BLOCK_SIZE; i++) {
        iv[i] = static_cast<Byte>(iv_bytes[i]);
    }
    Bytes cipher_dat = {0x76,0x4a,0xa2,0x6b,0x55,0xa4,0xda,0x65,0x4d,0xf6,0xb1,0x9e,0x4b, 0xce,0x00,
      0xf4, 0xed, 0x05, 0xe0, 0x93, 0x46, 0xfb, 0x0e,0x76, 0x25, 0x83, 0xcb, 0x7d, 0xa2, 0xac,0x93, 0xa2};
   
    // plaintext define array of bytes
    std::string inputString = "This is a top secret.";
    Bytes ptext1(inputString.begin(), inputString.end());
    //facem padding cu 11 valori de 0x0B pentru a fi multiplu de 16
    for(int i=0; i<11; i++){
        ptext1.emplace_back(0x0B);
    }
 
    //read words from the file
    std::ifstream inputFile("words.txt");
    std::string line;
    // Read each line of the input file
    while (std::getline(inputFile, line)) {
        // Iterate over each word in the line
        std::istringstream iss(line);
        std::string word;
        while (iss >> word) {
            // Add "#" characters to the word until it has a length of 16 characters
            while (word.length() < 16) {
                word += "#";
            }
            ///CREARE CHEIE////////////
            for(unsigned int i=0; i< KEY_SIZE; i++ ){
                key[i] = word[i];
            }
            //OBTIERE CIFRU REZULTAT
            Bytes ctext1 = aes_encrypt(key.data(), iv.data(), ptext1);
            //DACA S_A GASIT CHEIA O AFISAM
            if(contains_cipher_dat(cipher_dat, ctext1)){
                // print essential information
                std::cout << "Ciphertex rezultat: " << hexlify(ctext1) << endl 
                        << "Ciphertex dat: " << hexlify(cipher_dat) << endl 
                        << "Word key: " << word <<endl
                        << "Plain text: " << hexlify(ptext1) << endl
                        << "The IV used    : " << hexlify(iv) << endl
                        << "The Key used    : " << hexlify(key) << endl;
            }
        }
    } 
    return 0;
}
