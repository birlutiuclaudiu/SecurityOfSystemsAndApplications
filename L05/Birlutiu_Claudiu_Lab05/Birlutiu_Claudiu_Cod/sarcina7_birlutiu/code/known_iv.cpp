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
int main(int argc, char const *argv[]){
    // key, iv1, iv2
    array<Byte, KEY_SIZE> key;
    array<Byte, BLOCK_SIZE> iv;
    //////////////////////CREATE IV////////////////////////////////////////
    Bytes iv_bytes= {0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff, 0x00, 0x99, 0x88, 
                                0x77, 0x66, 0x55, 0x44, 0x33, 0x22, 0x11};
    for (unsigned int i = 0; i < BLOCK_SIZE; i++) {
        iv[i] = static_cast<Byte>(iv_bytes[i]);
    }
    // plaintext define array of bytes
    std::string inputString = "This is a top secret.";
    Bytes ptext1(inputString.begin(), inputString.end());
    ptext1.emplace_back(0x0B); ptext1.emplace_back(0x0B); ptext1.emplace_back(0x0B); ptext1.emplace_back(0x0B); ptext1.emplace_back(0x0B); ptext1.emplace_back(0x0B); 
    ptext1.emplace_back(0x0B); ptext1.emplace_back(0x0B); ptext1.emplace_back(0x0B); ptext1.emplace_back(0x0B); ptext1.emplace_back(0x0B);
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
            std::cout << word << std::endl;
            for(unsigned int i=0; i< KEY_SIZE; i++ ){
                key[i] = word[i];
            }
            Bytes ctext1 = aes_encrypt(key.data(), iv.data(), ptext1);
            
            // print essential information
            std::cout << "Ciphertex: " << hexlify(ctext1) << endl
                    << "Plain text: " << hexlify(ptext1) << endl
                    << "The IV used    : " << hexlify(iv) << endl
                    << "The Key used    : " << hexlify(key) << endl;
        }
    } 
    return 0;
}
