#include<sys/wait.h>
#include<stdlib.h>
#include<stdio.h>
#include<unistd.h>

int main(){

	int id;
	id=fork(); /*Fork a child process*/

	if(id<0){  /*Error occured*/
		printf("Error!!!Fork Failed.\n");
		exit(0);
	}

	else{
		printf("\nFork was successful.\n");
		if(id==0){  /*child process*/
			printf("This is the child process.\n");
			exit(0);
		}

		else{   /*parent process*/
			printf("This is the parent process.\n");
			wait(NULL);
			printf("Child Complete\n");
			exit(0);
		}
	}
	return(0);
}
