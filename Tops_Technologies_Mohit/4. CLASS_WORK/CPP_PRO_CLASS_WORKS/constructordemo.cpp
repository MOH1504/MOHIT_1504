#include<iostream>
using namespace std;

class Sample
{
	public:
			
			Sample()
			{
				cout<<"\n\nDefault Constructor Called.";
			}
			
			Sample(string fname,string lname,string email)
			{
				cout<<"\n\nParameterized Constructor Called.";
				cout<<"\nFname : "<<fname;
				cout<<"\nLname : "<<lname;
				cout<<"\nEmail : "<<email;
			}
	
};


int main()
{
	Sample s1("rakesh","kharva","rakesh@gmail.com");
	Sample s2("rakesh","kharva","rakesh@gmail.com");
	Sample s3("rakesh","kharva","rakesh@gmail.com");
	Sample s6;
	Sample s4("rakesh","kharva","rakesh@gmail.com");
	Sample s5("rakesh","kharva","rakesh@gmail.com");
	
	return 0;
}