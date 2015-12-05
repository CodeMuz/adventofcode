#include <stdio.h>

int main(void)
{
    FILE *fp;
    int c;
    int currentFloor = 0;    
    int pos = 0;
    int basementPos = 0;
    int enteredBasement = 0;

    fp = fopen("input.txt", "r"); // error check this!

    while((c = fgetc(fp)) != EOF) {
    	pos++;
        if (c == '(') {
        	currentFloor++;
        }
        if (c == ')') {
        	currentFloor--;
        }
        if((currentFloor == -1) && (enteredBasement == 0)){
        	basementPos = pos;
        	enteredBasement = 1;
        }
    }

    printf("last floor = %i \n",currentFloor);
    printf("first basement position = %i \n",basementPos);
    fclose(fp);

    return 0;
}