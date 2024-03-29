#include <iostream>
#include <string>

//a function that reverses an integer number
//long reversDigits(long num) 
//{ 
//    long rev_num = 0; 
//    while (num > 0) 
//    { 
//        rev_num = rev_num*10 + num%10; 
//        num = num/10; 
//    } 
//    return rev_num; 
//} 

long appendDigit(long base, long append) {
   std::string sBase = std::to_string(base);
   std::string sAppend = std::to_string(append);
   std::string result = sBase + sAppend;
   return std::stol(result);

}

int main()
{

    int a, c;
    long b = 0;
	//a is the input number
	//b is the output number
	//c is the remainder counter
	
	//getting the input
    std::cin>>a;
	
	//checking for special cases
    if (a==0)
    {
        std::cout<<0;
    }
    else if (a==1)
    {
        std::cout<<1;
    }
	
	//program starts to count down from 9 to 2 and checks if the number is devisible by those digits. 
	//if yes, it will devide it as much as possible before moving on to the next digit.
    else
    {
        for (int i = 9; i > 1; i--)
        {
            c = a %i;
            while (c==0)
            {
				//b will be the biggest number, which the product of it's digits are equal to the input number.
				//therefore, it should be reversed
                //b = (b*10)+i;
                b = appendDigit(i, b);
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
			
			// reverse integer 
			//now we use the function
			
               //long reversedNumber = 0, r;
                //while(b != 0)
                //{
                //    r = b%10;
               //     reversedNumber = reversedNumber*10 + r;
              //     b /= 10;
              // }
              
              std::cout << b/10;
        }
    }
  
}


