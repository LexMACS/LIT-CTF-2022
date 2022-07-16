#include <stdio.h>

int a[] = {43,94,18,90,89,31,1,100,46,14,76,10,121,107,89,115,46,58,95,109,4,112,73,39};
int a2[]= {0xf,0x49,-53,-74,12,22,51,-158,0x64,28,-133,44,-130,-43,38,0x5f,0x69,-77,0x5f,32,-88,71,97,-130};

int main(){
    int (*f)() = main;
    char input[25];
    scanf("%24s", input);
    for(int i = 0; i < 24; i++){
        unsigned char *inst = (unsigned char*)(main + a[i]);
        a[i] = *inst;
        a[i] += a2[i];
        if(a[i] != input[i]){
            printf("wrong\n");
            return 0;
        }
    }
    printf("correct\n");
}
