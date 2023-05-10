#include<iostream>
#include <cmath>
using namespace std;

class EventOrganizer
{

    private:
        string eventName;
        string firstName;
        string lastName;
        int numberOfGuests;
        int numberOfMinutes;
        int numberOfServers;
        double cost1;
        double cost2;
        double deposit;
        double costForOneServer;
        double totalFoodCost;
        double averageCost;
        double totalCost;
        const double CostPerHour = 18.50;
        const double CostPerMinute = .40;
        const double CostOfDinner = 20.70;
    public:
        // Default Constructor
        EventOrganizer(); 
        // Parameterized Constructor
        EventOrganizer(string, string, string, int, int);
        // Function to get the event name
        void getEventName(); 
        // Function to get the first and last name
        void getName(); 
        // Function to get the number of guests and minutes
        void getGuestsMinutes(); 
        // Function to get the number of servers
        void getNumberOfServers(); 
        // Function to calculate the cost for one server
        void calculateCostForOneServer(); 
        // Function to calculate the total food cost
        void calculateTotalFoodCost(); 
        // Function to calculate the average cost per person
        void calculateAverageCost(); 
        // Function to calculate the total cost
        void calculateTotalCost(); 
        // Function to display the cost estimation
        void displayCostEstimation();
        //function to display the min depost cost
        void depositamount();
         
};
// Default Constructor
EventOrganizer::EventOrganizer()
{
    eventName = "";
    firstName = "";
    lastName = "";
    numberOfGuests = 0;
    numberOfMinutes = 0;
    numberOfServers = 0;
    cost1 = 0.0;
    cost2 = 0.0;
    costForOneServer = 0.0;
    totalFoodCost = 0.0;
    averageCost = 0.0;
    totalCost = 0.0;
    deposit=0.0;
}

// Parameterized Constructor
EventOrganizer::EventOrganizer(string _eventName, string _firstName, string _lastName, int _numberOfGuests, int _numberOfMinutes)
{
    eventName = _eventName;
    firstName = _firstName;
    lastName = _lastName;
    numberOfGuests = _numberOfGuests;
    numberOfMinutes = _numberOfMinutes;
    numberOfServers = 0;
    cost1 = 0.0;
    cost2 = 0.0;
    costForOneServer = 0.0;
    totalFoodCost = 0.0;
    averageCost = 0.0;
    totalCost = 0.0;
    deposit=0.0;
}
// Function to get the event name
void EventOrganizer::getEventName()
{
    cout << "\nPlease enter the name of the event: ";
    getline(cin, eventName);
}

// Function to get the first and last name
void EventOrganizer::getName()
{
    cout << "\nPlease enter your first name: ";
    getline(cin, firstName);
    cout << "\nPlease enter your last name: ";
    getline(cin, lastName);
}

// Function to get the number of guests and minutes
void EventOrganizer::getGuestsMinutes()
{
    cout << "\nPlease enter the number of guests: ";
    cin >> numberOfGuests;
    cout << "\nPlease enter the number of minutes: ";
    cin >> numberOfMinutes;
}

// Function to get the number of servers
void EventOrganizer::getNumberOfServers()
{
    numberOfServers = ceil(numberOfGuests/20.0);
}

// Function to calculate the cost for one server
void EventOrganizer::calculateCostForOneServer()
{
    cost1 = (numberOfMinutes / 60) * CostPerHour;
    cost2 = (numberOfMinutes % 60) * CostPerMinute;
    costForOneServer = cost1 + cost2;
}

// Function to calculate the total food cost
void EventOrganizer::calculateTotalFoodCost()
{
    totalFoodCost = numberOfGuests * CostOfDinner;
}

// Function to calculate the average cost per person
void EventOrganizer::calculateAverageCost()
{
    averageCost = totalFoodCost / numberOfGuests;
}

// Function to calculate the total cost
void EventOrganizer::calculateTotalCost()
{
    totalCost = totalFoodCost + (costForOneServer * numberOfServers);
}
// Function to display the cost estimation
void EventOrganizer::displayCostEstimation()
{
    cout << "\n\nEvent Cost Estimation\n\n" << endl;
    cout << "\n\nEvent Name:\n\n " << eventName << endl;
    cout << "\n\nCustomer Name: " << firstName << " " << lastName << endl;
    cout << "\n\nNumber of guests: " << numberOfGuests << endl;
    cout << "\n\nNumber of minutes:  " << numberOfMinutes << endl;
    cout << "\n\nNumber of servers: " << numberOfServers << endl;
    cout << "\n\nCost for one server: " << costForOneServer << endl;
    cout << "\n\nTotal food cost: " << totalFoodCost << endl;
    cout << "\nAverage cost per person: " << averageCost << endl;
    cout << "\nTotal cost: " << totalCost << endl;
}
    void EventOrganizer::depositamount()
    {
    	deposit = totalCost*.25;
    	cout<<"you need to deposit 25% amount to reserve a event:"<<deposit;
	}
   

int main()
{
	
	
	cout<<"************Event Management System************\n\n";

	 // Create an object
    EventOrganizer obj; 
    // Get the event name
    obj.getEventName(); 
    // Get the name
    obj.getName(); 
    // Get the number of guests and minutes
    obj.getGuestsMinutes(); 
    // Get the number of servers
    obj.getNumberOfServers(); 
    // Calculate the cost for one server
    obj.calculateCostForOneServer(); 
    // Calculate the total food cost
    obj.calculateTotalFoodCost(); 
    // Calculate the average cost per person
    obj.calculateAverageCost(); 
    // Calculate the total cost
    obj.calculateTotalCost(); 
    // Display the cost estimation
    obj.displayCostEstimation(); 
    obj.depositamount();
			           
	
	return 0;
}
