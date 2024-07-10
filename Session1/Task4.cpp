#include<iostream>
#define UPPER_CASE_OFFSET 'a'-'A'
int main(){
    char vowels[]={'a','e','o','u','i'};
    char check_v;
    bool charIsV{0};
    std::cout << "enter char to check" << std::endl;
    std::cin>>check_v;
    for(char i:vowels){
        if((check_v==i)||(check_v+UPPER_CASE_OFFSET==i)){            
            charIsV=1;
            break;
        }
    }
    if(charIsV)
        std::cout << "Char is vowel" << std::endl;
    else
    {
        std::cout << "Char is  not vowel" << std::endl;
    }

    return 0;
}