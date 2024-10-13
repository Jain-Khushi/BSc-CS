#include<pthread.h>
#include<stdio.h>
#include<stdlib.h>
#include<sys/types.h>
#include<unistd.h>
#include<sys/wait.h>

int sum;
int product;
void *runner1(void *param1);
void *runner2(void *param2);

int main(int argc,char *argv[]){
	pthread_t tid1;
	pthread_t tid2;
	pthread_attr_t attr1;
	pthread_attr_t attr2;

	if(argc !=2){
		fprintf(stderr,"usage: a.out <integer value>\n");
		return -1;
	}
	if(atoi(argv[1])<0){
			fprintf(stderr,"%d must be >=0\n",atoi(argv[1]));
			return -1;
			}
	
	pthread_attr_init(&attr1);
	pthread_attr_init(&attr2);
	pthread_create(&tid1,&attr1,runner1,argv[1]);
	pthread_create(&tid2,&attr2,runner2,argv[1]);
	pthread_join(tid1,NULL);
	pthread_join(tid2,NULL);

	printf("Sum = %d\n",sum);
	printf("Product = %d\n",product);
}
	void *runner1(void *param1){
	    int i,upper=atoi(param1);
 	    sum=0;

	    for(i=1;i<=upper;i++)
	        sum=sum+i*i;
	    pthread_exit(0);
	}
        
        void *runner2(void *param2){
		int j,upp=atoi(param2);
		product=1;

	        for(j=1;j<=upp;j++)
		    product=product*j;
                pthread_exit(0);
	}
