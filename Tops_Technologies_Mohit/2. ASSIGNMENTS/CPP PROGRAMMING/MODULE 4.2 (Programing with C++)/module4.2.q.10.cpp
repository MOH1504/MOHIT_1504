#include <iostream> 
using namespace std; 

class String 
{ 
private: 
	char *s; 
	int size; 
public: 
	String(const char *str = NULL); // constructor 
	~String() { delete [] s; }// destructor 
	String(const String&); // copy constructor 
	void print() { cout << s << endl; } // Function to print string 
	void operator +=(String&); // concatenates two strings 
}; 

String::String(const char *str) 
{ 
	size = strlen(str); 
	s = new char[size+1]; 
	strcpy(s, str); 
} 

// Copy constructor 
String::String(const String& old_str) 
{ 
	size = old_str.size; 
	s = new char[size+1]; 
	strcpy(s, old_str.s); 
} 

// Concatenates two strings 
void String::operator +=(String& str) 
{ 
	// allocate memory for the concatenated string 
	size += str.size; 
	char *ns = new char[size+1]; 

	// copy the first string 
	strcpy(ns, s); 

	// concatenate the second string 
	strcat(ns, str.s); 

	// assign the concatenated string to the original string 
	delete [] s; 
	s = ns; 
} 

// Main function 
int main() 
{ 
	String str1("Geeks"); 
	String str2("ForGeeks"); 

	// Concatenates two strings 
	str1 += str2; 

	str1.print(); 
	return 0; 
}