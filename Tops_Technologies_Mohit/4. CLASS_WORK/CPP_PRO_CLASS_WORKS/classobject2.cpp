#include <iostream>
using namespace std;

class PersonalDetails
{
	public:	
		string fname,lname,email;
		
		void acceptDetails()
		{
			cout<<"Enter your First Name : ";
			cin>>fname;
			cout<<"Enter your Last Name : ";
			cin>>lname;
			cout<<"Enter your Email : ";
			cin>>email;
		}
		
		void displayDetails()
		{
			cout<<"\nFirst Name : "<<fname;
			cout<<"\nLast Name : "<<lname;
			cout<<"\nEmail : "<<email;
		}
		
};

int main()
{
	PersonalDetails p;
	p.acceptDetails();
	p.displayDetails();	
	return 0;
}












