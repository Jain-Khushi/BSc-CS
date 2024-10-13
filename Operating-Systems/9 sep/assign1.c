#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
int main(){
	int id;
	id=fork();
	if(id<0){
		printf("Error!!!Fork Failed.\n");
		exit(0);
	}
	else
	{
		printf("\nFork Successful.\n");
		printf("The id value is:%d\n",id);
		exit(0);
	}
	return(0);
}
