//Name : KHUSHI JAIN  
//Roll no. : 204024

// Function to allocate memory to blocks as per Best fit algorithm.
#include<bits/stdc++.h>
using namespace std; 
void Best_Fit(int Block_Size[], int m, int Process_Size[], int n)
{
 int Arr[n]; // Stores block id of the block allocated to a process
 memset(Arr, -1, sizeof(Arr));
 for (int i=0; i<n; i++)
 {
 int index = -1;
 for (int j=0; j<m; j++)
 {
 if (Block_Size[j] >= Process_Size[i])
 {
 if (index == -1)
 index = j;
 else if (Block_Size[index] > Block_Size[j])
 index = j;
 }
 }
 if (index != -1)
 {
 Arr[i] = index;
 Block_Size[index] -= Process_Size[i];
 }
 }

 cout << "\nProcess No.\tProcess Size\tBlock No.\n";
 for (int i = 0; i < n; i++)
 { 
 cout << " " << i+1 << "\t\t" << Process_Size[i] << "\t\t";
 if (Arr[i] != -1)
 cout << Arr[i] + 1;
 else
 cout << "Not Allocated";
 cout << endl;
 }
}
int main()
{
     int Block_Size[5],Process_Size[5];
    cout<<"Enter sizes of 5 memory holes(Separated by space) : ";
    for(int i=0;i<5;i++)
    cin>>Block_Size[i];
    cout<<"Enter sizes of 5 processes(Separated by space) : ";
    for(int i=0;i<5;i++)
    cin>>Process_Size[i];
    
    cout<<"\n    Best Fit Allocation Strategy\n";

 int m = sizeof(Block_Size)/sizeof(Block_Size[0]);
 int n = sizeof(Process_Size)/sizeof(Process_Size[0]);

 Best_Fit(Block_Size, m, Process_Size, n);

 return 0;
}