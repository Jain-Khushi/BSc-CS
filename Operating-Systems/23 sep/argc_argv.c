#include<stdio.h>
#include<sys/types.h>

int main(int argc,char *argv[]){
	int i;
	printf("argc value : %d\n ",argc);
	for(i=1;i<argc;i++){
		printf("\nargv values : %s",argv[i]);
	}
	printf("\n");
	return 0;
}
