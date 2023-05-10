#include <iostream>  
using namespace std; 
 
class Address {  

    public:  
   string addressLine, city, state; 
      
    Address(string a, string c, string s)    
    {    
        addressLine = a;    
        city = c;    
        state = s;    
    }    
};  

class Employee    
    {    
        private:  
        Address*address;    
        public:  
        int id;    
        string name;    
        Employee(int i, string n, Address* a)    
       {    
           id = i;    
           name = n;    
           address = a;    
       }    
     void display()    
       {    
           cout<<id <<" "<<name<< " "<<     
             address->addressLine<< " "<< address->city<< " "<<address->state<<endl;    
       }    
   };  
 
int main(void) {  
    Address a1("C-146, Sec-15","Noida","UP");    
    Employee e1(101,"Nakul",&a1);    
    e1.display();   
   return 0;  
}  