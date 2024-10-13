#include <iostream>

using namespace std;

class ShortestTime
{
    public:
        int n,bt[10],at[10],tat[10],wt[10],rt[10],finish[10],twt,ttat,total;
        void readData()
        {
            cout<<"\nEnter Number of Processes: ";
            cin>>n;
            cout<<"Enter the Burst Time in order(separated by space): ";
            for(int i = 0;i < n;i++)
            cin>>bt[i];
            cout<<"Enter the Arrival Time in Order(separated by space): ";
            for(int i = 0; i < n;i++)
            cin>>at[i];
        }
        
        void Init()
        {
            total = 0;
            twt = 0;
            ttat = 0;
             for(int i = 0;i < n; i++)
             {
                 rt[i] = bt[i];
                 finish[i] = 0;
                 wt[i] = 0;
                 tat[i] = 0;
                 total += bt[i];
         
            }
        }

        void ComputeSRT()
        {
            readData();
            Init();
            int time,old,i;
            int next = 0;
            cout<<"\n     Shortest Remaining Time First Algorithm\n";
            cout<<"\n-------------GANTT CHART-----------------\n";
            for(time = 0;time < total; time++)
            {
                old = next;
                next = getNextProcess(time);
                if(old != next || time == 0)
                {
                    cout<<"("<<time<<")| == P"<<next + 1<<"==|";
                }
                rt[next] = rt[next] - 1;
                if(rt[next] == 0)
                {
                    finish[next] = 1;
                }

                for( i = 0; i < n;i++)
                if(i != next && finish[i] == 0 && at[i] <= time)
                   wt[i]++;
            }
            cout<<"("<<total<<")"<<endl;
            for(i = 0;i < n;i++)
            if(!finish[i])
            {
                cout<<"Scheduling Failed , Cannot Continue!!\n";
                return;
            }
            dispTime();

        }

        int getNextProcess(int time)
        {
            int i,low;
            for(i = 0;i < n;i++)
            if(finish[i] == 0)
            {
                low = i;
                break;
            }
            for(i = 0;i < n;i++)
            {
                if(finish[i] != 1)
                if(rt[i] < rt[low] && at[i] <= time)
                {
                    low = i;
                }
            
            }
            return low;
        }

        void dispTime()
        {
            for(int i = 0;i < n;i++)
            {
                twt += wt[i];
                tat[i] = wt[i] + bt[i];
                ttat += tat[i];
                cout<<endl;
                cout<<"Waiting Time for P"<<(i+1)<<" : "<<wt[i]<<",Turnaround Time : "<<tat[i]<<endl;
            }
            cout<<"\nAverage Waiting Time : "<<(double)twt/n;
            cout<<"\nAverage Turnaround Time : "<<(double)ttat/n<<endl;
            cout<<"\nScheduling Complete\n";
            
        }
};

int main()
{
    ShortestTime obj;
    obj.ComputeSRT();
}