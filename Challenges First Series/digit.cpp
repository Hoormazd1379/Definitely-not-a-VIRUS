#include <iostream>
#include <string>

int reversDigits(int num) 
{ 
    int rev_num = 0; 
    while (num > 0) 
    { 
        rev_num = rev_num*10 + num%10; 
        num = num/10; 
    } 
    return rev_num; 
} 

int main()
{
    int a, b = 0, c;
    std::cin>>a;
    if (a==0)
    {
        std::cout<<0;
    }
    else if (a==1)
    {
        std::cout<<1;
    }
    else
    {
        for (int i = 9; i > 1; i--)
        {
            c = a %i;
            while (c==0)
            {
                b = (b*10)+i;
                a = a/i;
                c = a%i;
            }
        }
        
        if (a>1)
        {
            std::cout<<-1;
        }
        else
        {
              //  int reversedNumber = 0, r;
              //  while(b != 0)
              //  {
              //      r = b%10;
              //      reversedNumber = reversedNumber*10 + r;
              //      b /= 10;
              //  }
              
              std::cout << reversDigits(b);
        }
    }
  
}


