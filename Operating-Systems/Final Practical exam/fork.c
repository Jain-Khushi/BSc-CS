//Name : KHUSHI JAIN  
//Roll no. : 204024


#include<stdlib.h>
#include<stdio.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/wait.h>

int main(){
	int id;
	id=fork();
	if(id<0){
		printf("ERROR! FORK FAILED!");
		exit(0);
	}
	else{
		printf("\nThe fork was successfull\n");

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
	return (0);
}

