#include<iostream>
using namespace std;

int main()
{
    int bt[20], p[20], wt[20], tat[20], i, j, n, total = 0, pos, temp;
    float avg_wt, avg_tat;
    cout<<endl;
    cout<<"   Enter Number of Process: ";
    cin>>n;

    cout<<endl; 

    cout<<"   Enter Burst Time:-"<<endl;
    for(i = 0; i < n; i++)
    {
        cout<<"   Process " << i + 1 <<": ";
        cin>>bt[i];
        cout<<endl;
        p[i] = i + 1;
    }

    //sorting of burst times
    for(i = 0; i < n; i++)
    {
        pos = i;
        for(j = i + 1; j < n; j++)
        {
            if(bt[j] < bt[pos])
            pos = j;
        }

        temp = bt[i];
        bt[i] = bt[pos];
        bt[pos] = temp;

        temp = p[i];
        p[i] = p[pos];
        p[pos] = temp;
    }

    wt[0] = 0;


    for(i = 1; i < n; i++)
    {
        wt[i] = 0;
        for(j = 0; j < i; j++)
        wt[i] += bt[j];

        total += wt[i];
    }

    avg_wt = (float)total/n;
    total = 0;
    cout<<"\n     Shortest Job First(non-preemptive)\n\n";

    cout << "   Processes  "<< " Burst Time  " << " Waiting Time  " << " Turnaround Time"<<endl;
    for(i = 0; i < n; i++)
    {
        tat[i] = bt[i] + wt[i];
        total += tat[i];

        cout << "   p" << p[i] << "\t\t" << bt[i] <<"\t\t"<< wt[i] <<"\t\t " << tat[i] <<endl;
    }

    cout<<endl;

    avg_tat = (float)total/n;
    cout<<"Average Waiting Time = "<<avg_wt<<endl;
    cout<<"Average Turnaround Time = "<<avg_tat<<endl;
}