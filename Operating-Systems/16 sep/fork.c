#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
int main()
{
	int a,b,c;
	a=fork();
	b=fork();
	c=fork();

	if(a<0){
		printf("Error!!!Fork failed.\n");
		exit(0);
	}
	else if(a==0){
		printf("\nThis is child process of fork a.");
		printf("\nChild id of fork a %d",getpid());
		printf("\nParent id of fork a %d",getppid());
	}
	else{
		printf("\nThis is parent process of fork a.");
		printf("\nParent id of fork a %d",getpid());
	}
	if(b==0){
		printf("\nThis is child process of fork b.");
		printf("\nChild id of fork b %d",getpid());
		printf("\nParent id of fork b %d",getppid());
	}
	else{
		printf("\nThis is parent process of fork b.\n");
		printf("\nParent id of fork b %d",getpid());
	}
	if(c==0){
		printf("\nThis is child process of fork c.");
		printf("\nChild id of fork c %d",getpid());
		printf("\nParent id of fork c %d",getppid());
	}
	else{
		printf("\nThis is parent process of fork c.");
		printf("\nParent id of fork c %d\n",getpid());
	}
	return(0);
}

	   	
