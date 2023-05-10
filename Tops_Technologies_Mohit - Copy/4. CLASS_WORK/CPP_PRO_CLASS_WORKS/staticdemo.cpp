#include<iostream>
using namespace std;

class StaticDemo{
    public:
	static int objCount;	
	
	StaticDemo()
	{
		cout<<"\nDefault Constructor Called.";
		objCount++;
	}
};
 
int StaticDemo::objCount=0;

int main()
{
	StaticDemo sd1,sd2,sd3;
	cout<<"\nobjectCount :"<<sd3.objCount; 
	return 0;
}