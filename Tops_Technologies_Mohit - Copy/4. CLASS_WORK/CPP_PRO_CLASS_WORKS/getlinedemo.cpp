#include<iostream>
using namespace std;

class Accept
{
	public:
		string name;
		
		void getName()
		{
			cout<<"\nEnter Name : ";
			getline(cin,name);
		}
		void showName()
		{
			cout<<"\nName is : "<<name;
		}
};

int main()
{   
    Accept obj;
    obj.getName();
    obj.showName();
	return 0;
}