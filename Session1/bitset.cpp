#include <iostream>
#include <bitset>

    void BinaryToDec(){
        std::bitset<8> myBits; // Create an 8-bit bitset (initialized to all zeros)
        std::cout << "Enter number in binary " << std::endl;
        std::cin>>myBits;
        // Convert bitset to unsigned long
        unsigned long value = myBits.to_ulong();
        std::cout << "Value: " << value << std::endl; // Output: 6
    }

    void DecToBinary(){
        
        std::bitset<8> myBits; // Create an 8-bit bitset (initialized to all zeros)
        std::bitset<8> b4{"ABBA", length_t(4), /*0:*/'A', /*1:*/'B'}; // == 0B0000'0110
        long Dvalue;
        std::cout << "Enter number in decimal" << std::endl;
        std::cin>>Dvalue;
        myBits=Dvalue;
        std::cout << "Binary represenation for "<<Dvalue<<" is "<<myBits << std::endl;


    }

int main() {

    while(1)
    {
        char ConverType;
        std::cout << "Select type of conversion: 1-Decimal to Binary.    2-Binary to Decimal " << std::endl;
        std::cin>>ConverType;
        if(ConverType=='1'){
            DecToBinary();
        }
        else if(ConverType=='2'){
            BinaryToDec();    
        }
        else
        {
            std::cout << "Invalid Selection" << std::endl;
        }
    }
    return 0;
}
