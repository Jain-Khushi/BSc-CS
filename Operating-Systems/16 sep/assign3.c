#include<stdlib.h>
#include<stdio.h>
#include<unistd.h>
#include<sys/wait.h>

int main()
{
	int id;
	id=fork();
	if(id<0){
		printf("Error!!!Fork failed.!\n");
		exit(0);
	}
	else{
		printf("\nFork was successful.\n");
		if(id==0){
			printf("This is the child process.\n");
			execlp("/bin/ls","ls",NULL);
			exit(0);
		}
		else{
		        wait(NULL);
			printf("This is the parent process.\n");
			exit(0);
		}
	}
	return 0;
}

