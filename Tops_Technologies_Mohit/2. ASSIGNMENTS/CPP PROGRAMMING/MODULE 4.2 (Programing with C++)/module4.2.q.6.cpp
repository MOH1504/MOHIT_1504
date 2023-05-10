#include <iostream>
using namespace std;
 
class Person {
    protected:
        string name;
        int age;
 
    public:
        Person(string n, int a) {
            name = n;
            age = a;
        }
        void read() {
            cout << "Enter name: ";
            cin >> name;
            cout << "Enter age: ";
            cin >> age;
        }
        void display() {
            cout << "Name: " << name << endl;
            cout << "Age: " << age << endl;
        }
};
 
class Student : public Person {
    protected:
        float percentage;
 
    public:
        Student(string n, int a, float p) : Person(n, a) {
            percentage = p;
        }
        void read() {
            Person::read();
            cout << "Enter percentage: ";
            cin >> percentage;
        }
        void display() {
            Person::display();
            cout << "Percentage: " << percentage << endl;
        }
};
 
class Teacher : public Person {
    protected:
        float salary;
 
    public:
        Teacher(string n, int a, float s) : Person(n, a) {
            salary = s;
        }
        void read() {
            Person::read();
            cout << "Enter salary: ";
            cin >> salary;
        }
        void display() {
            Person::display();
            cout << "Salary: " << salary << endl;
        }
};
 
int main() {
    Person p("John", 25);
    p.display();
    p.read();
    p.display();
 
    Student s("John", 25, 88.5);
    s.display();
    s.read();
    s.display();
 
    Teacher t("John", 25, 25000);
    t.display();
    t.read();
    t.display();
 
    return 0;
}