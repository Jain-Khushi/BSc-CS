#include<iostream>
#include <algorithm>
#include<fstream>
using namespace std;
    
//Heapify function
void heapify(int arr[],int n,int i,int &count)
{

    
    int largest=i; 

    int l=i*2+1;                  //left child
    int r=(i*2)+2;               //right child

   if(l<n&&(count+=1)&&(arr[l]>arr[largest]))   // If left child is larger than root
    {
        largest=l;
       
    }

    if(r<n&&(count+=1)&&(arr[r]>arr[largest]))   // If right child is larger than largest so far
    {
        largest=r;
                  
    }

    if(largest != i )   // If largest is not root
    {

        swap(arr[i],arr[largest]);    
        
       heapify(arr,n,largest,count);   // Recursively heapify the affected sub-tree
    }

    
    
}

//heap sort func
int Heap_Sort(int arr[],int n,int &comp)
{
        // For building heap
    for(int i=n/2-1;i>=0;i--)              
    {
      heapify(arr,n,i,comp);
        
    }
  
    
    // for deletion from heap
    for(int i=n-1;i>=0;i--)
    {
        swap(arr[i],arr[0]);        
        heapify(arr,i,0,comp); 
        
    }
    
    return comp;             
}


// For generating Random array
    
void generate_random_array(int arr[], int size)
{
        for (int i = 0; i < size; i++)
        {
            arr[i] = (rand() % 100);
        }
}

 // Average Case
    
void heap_avg(int num_cases = 100, int min_size = 30, int max_size = 1000)
{
        int interval = (max_size - min_size) / num_cases;
        int comp = 0;
        for (int size = min_size, i = 0; i < num_cases; i++, size += interval)
        {
            int *Arr = new int[size];
            generate_random_array(Arr, size);
    
            fstream fout1;
            
            Heap_Sort(Arr,size,comp);
    
            fout1.open("HeapAverage.csv", ios::out | ios::app);
    
            fout1 << size << "," << comp << endl;
            comp = 0;
        }
}

//Best Case
void heap_best(int num_cases = 20, int min_size = 30, int max_size = 1000)
{
        int interval = (max_size - min_size) / num_cases;
        int comp = 0;
        for (int size = min_size, i = 0; i < num_cases; i++, size += interval)
        {
            int *Arr = new int[size];
            generate_random_array(Arr, size);
            sort(Arr, Arr + size, greater<int>());
            fstream fout1;
            
            Heap_Sort(Arr,size,comp);
    
            fout1.open("HeapBest.csv", ios::out | ios::app);
    
            fout1 << size << "," << comp << endl;
            comp = 0;
        }
}

//Worst Case
void heap_Worst(int num_cases = 20, int min_size = 30, int max_size = 1000)
{
        int interval = (max_size - min_size) / num_cases;
        int comp = 0;
        for (int size = min_size, i = 0; i < num_cases; i++, size += interval)
        {
            int *Arr = new int[size];
            generate_random_array(Arr, size);
            sort(Arr, Arr + size);
            fstream fout1;
            
            Heap_Sort(Arr,size,comp);
    
            fout1.open("HeapWorst.csv", ios::out | ios::app);
    
            fout1 << size << "," << comp << endl;
            comp = 0;
        }
}

int main()
{
   

    heap_avg();
    heap_best();
    heap_Worst();

    
     return 0;
}
