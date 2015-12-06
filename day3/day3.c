#include <stdio.h>

const int dim = 1000;

typedef int housePlane[dim][dim];

int deliverPresent(housePlane *houses, int *x, int *y, char c){

     switch(c){
        case('^'):
            *y = *y + 1;
            (*houses)[*x][*y] = (*houses)[*x][*y] + 1;
        break;
        case('>'):
            *x = *x + 1;
            (*houses)[*x][*y] = (*houses)[*x][*y] + 1;
        break;
        case('<'):
            *x = *x - 1;
            (*houses)[*x][*y] = (*houses)[*x][*y] + 1;
        break;
        case('v'):
            *y = *y - 1;
            (*houses)[*x][*y] = (*houses)[*x][*y] + 1;
        break;
    }  

    return 1;
}

int main(void)
{
    FILE *fp;
    
    housePlane *houses;

    int houseGrid[dim][dim];
    int mid = dim / 2;

    houses = &houseGrid;

    int sx = mid, sy = mid;    
    int rx = mid, ry = mid;

    int *tmpSx = &sx;
    int *tmpSy = &sy;

    int *tmpRx = &rx;
    int *tmpRy = &ry;

    int c;
    int i,j;
    int turn = 0;

    int presentHouseCount = 0;

    fp = fopen("input.txt", "r"); // error check this!

    //initialize grid to zero
    for (i = 0; i < dim; i++){
        for (j = 0;j < dim; j++){
            (*houses)[i][j] = 0; 
        }
    }

    while((c = fgetc(fp)) != EOF) {
        if(turn == 0){
            deliverPresent(houses,tmpSx,tmpSy,c);
            turn = 1;
        } else {
            deliverPresent(houses,tmpRx,tmpRy,c);
            turn = 0;
        }
    }
    
    //Calculate the number of houses with presents    
    for (i = 0; i < dim; i++){
        for (j = 0;j < dim; j++){
            if((*houses)[i][j] > 0){
                presentHouseCount++;
            }
        }
    }

    printf(" houses = %i \n", presentHouseCount);
    fclose(fp);

    return 0;
}