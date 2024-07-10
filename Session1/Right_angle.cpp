#include<iostream>
main()
{
    int x,y,z,max,max_ind;
    bool IsRightAngle{0};
    std::cin>>x>>y>>z;
    max=x; //start with x as max
    max_ind=1;//set ind to x
    //search for max num
    if(y>max){
        max_ind=2;
        max=y;
    }        
    if(z>max){
        max_ind=3;
        max=z;
    }
    //check right angle "pythagoras"
    switch(max_ind){
        case 1://x is max
        if((x*x)==((y*y)+(z*z)))
        {
            IsRightAngle=1;
        }
    //    std::cout << "formula " <<(z*z)<<"r s"<<((y*y)+(x*x))<< std::endl;
        break;
        case 2://y is max
        if((y*y)==((x*x)+(z*z)))
        {
            IsRightAngle=1;
        }
     //   std::cout << "formula " <<(y*y)<<" rs "<<((z*z)+(x*x))<< std::endl;
        break;
        case 3://z is max
        if((z*z)==((y*y)+(x*x)))
        {
            IsRightAngle=1;
        }
     //   std::cout << "formula " <<(z*z)<<"r s"<<((y*y)+(x*x))<< std::endl;
        break;

    }
        
//std::cout << "Max number is: " <<max<< std::endl;
std::cout << "The given side lengths form a right angled triangle: "<<std::boolalpha <<IsRightAngle<<std::noboolalpha<< std::endl;

}