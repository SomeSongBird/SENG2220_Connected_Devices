
#include <stdio.h>
#include <string.h>

//simple funciton to read the memory location of a string as well as what each character is in that string
int main(void){
    char string [] = "this is a string";
    for(int i = 0;i<strlen(string);i++){
        if(i==0){printf("Address  |  Contents\n");}
        printf("%p : %x\n", &string[i],string[i]);
    }
    return 0;
}