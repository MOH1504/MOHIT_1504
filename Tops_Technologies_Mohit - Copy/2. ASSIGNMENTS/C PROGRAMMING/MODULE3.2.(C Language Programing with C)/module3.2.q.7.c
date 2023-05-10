#include <stdio.h> 
 
int main() 
{ 
  int n[10]; 
  int i, oCtr, eCtr, ctr; 
  
  for( i=0; i<10; i++ ) 
  { 
    printf( "Enter number : " ); 
    scanf( "%d", &n[i] ); 
 
    if( n[i]%2 == 0 ) 
      eCtr += n[i]; 
    else 
      oCtr += n[i]; 
 
    ctr += n[i]; 
  } 
 
  printf( "Analysis: \n" ); 
  printf( "Sum of all odd numbers is : %d\n", oCtr ); 
  printf( "Sum of all even numbers is : %d\n", eCtr ); 
  printf( "Sum of all 10 numbers is : %d\n", ctr ); 
 
  return 0; 
} 


    