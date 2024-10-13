#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
int main(){
	int id;
	id=fork();
	if(id<0){
		printf("Error!!!Fork Failed.\n");
		exit(0);
	}
	else{
		printf("\nFork was successful.\n");
		if(id==0){
			printf("This is the child process.\n");
			exit(0);
		}
		else{
			printf("This is the parent process.\n");
			exit(0);
		}
	}
	return(0);
}
