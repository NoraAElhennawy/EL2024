#include<iostream>
main()
{
    int x,y,z,max;
    std::cin>>x>>y>>z;
    max=x;
    if(y>max)
        max=y;
    if(z>max)
        max=z;
std::cout << "Max number is: " <<max<< std::endl;
}