#include<iostream>
using namespace std;

class Student{
	public:
	string name ;
	void getName()
	{
		cout<<"\n Enter Name : ";
		cin>>name;
	}
};

class Extra{
    public:
	int em;
	Extra()
	{
	    em = 54;	
	}	
};

class Result:public Student,public Extra{
	public:
    int s1,s2,s3,tot;
    float per;
    
    Result()
    {
    	s1 = 78;
    	s2 = 88;
    	s3 = 74;
    	tot= s1+s2+s3+em;
    	per= (float)tot/4;
	}
	
	void display()
	{
		cout<<"\nName : "<<name;
		cout<<"\nTotal : "<<tot;
		cout<<"\nPercentage : "<<per;
	}
};

int main()
{
	Result rs;
	rs.getName();
	rs.display();
	return 0;
}