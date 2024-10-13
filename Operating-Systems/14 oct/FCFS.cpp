#include<iostream>
using namespace std;


int main()
{
    int n, process[20], burst[20], waiting_time[20],turn_around[20];
    double avg_Wt,sum=0, avg_Tt , sum_t=0;
   
    cout<<"Enter the number of processes: ";
    cin>>n; 
    cout<<"\nEnter the burst(execution) time of the processes: \n";
    for(int i=0;i<n;i++){
        cout<<"Process "<<i+1<<" : ";
        cin>>burst[i];
    }
    
    for(int i=1;i<n;i++){
        waiting_time[0] = 0;
        waiting_time[i]= burst[i-1] + waiting_time[i-1];
        
    }
    cout<<"\nWaiting time: \n";
    for(int i=0;i<n;i++){
        cout<<"Process "<<i+1<<" : ";
        cout<<waiting_time[i]<<endl;
    }
    
    for(int i=0;i<n;i++){
        turn_around[i]= waiting_time[i]+burst[i];
    }
    cout<<"\nTurn around time: \n";
    for(int i=0;i<n;i++){
        cout<<"Process "<<i+1<<" : ";
        cout<<turn_around[i]<<endl;
    }
    
    for(int i=0;i<n;i++){
        int temp = waiting_time[i];
         sum = sum+temp;
         avg_Wt= sum/n;
    }
    cout<<"\nAverage Waiting Time: ";
    cout<<avg_Wt;
    
    for(int i=0;i<n;i++){
        int temp = turn_around[i];
         sum_t = sum_t+temp;
         avg_Tt= sum_t/n;
    }
    cout<<"\nAverage Turn Around Time: ";
    cout<<avg_Tt;
    

    return 0;
}