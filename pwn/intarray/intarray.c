#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#define ll long long

void invalid(char *mes){
    printf("Invalid %s.\n", mes);
    _exit(1);
}

void safeint(int *x){
    scanf("%10d", x);
    getchar();
}

void safell(ll *x){
   scanf("%20lld", x);
   getchar();
}

int inyn(){
    char c = getchar();
    getchar();
    puts("");

    return c == 'y' || c == 'Y';
}

void *intarray(void *args){
    ll a[0x100];

    puts("Welcome to my int array storage program!\n");

    puts("How many ints would you like to store?");
    
    int n;
    safeint(&n);
    puts("");
    if(n <= 0 || n > 0x100) invalid("size, out of bounds");

    printf("Input %d ints.\n", n);
    for(int i = 0; i < n; i++){
        printf("%d: ", i);
        safell(&a[i]);
    }
    puts("");

    puts("Would you like to check for an error?");

    if(inyn()){
        puts("Input an index:");

        int x;
        safeint(&x);
        puts("");
        if(x < 0 || x >= n) invalid("index, out of bounds");

        printf("Index %d has value %lld.\n", x, a[x]);
        puts("");
    }

    puts("You can now make at most two edits.\n");

    for(int i = 0; i < 2; i++){
        puts("Would you like to make another edit?");

        if(inyn()){
            puts("Input an index:");

            int x;
            safeint(&x);
            puts("");
            if(x < 0) invalid("index, out of bounds");
    
            puts("Input the new value:");
            safell(&a[x]);
            puts("");

            printf("Index %d now has value %lld.\n", x, a[x]);
            puts("");
        }else{
            break;
	}
    }

    puts("The array will now be safely stored on a blockchain distributed across a convex hull network using ai-enhanced chacha cipher encryption technology with bloom filters for fast lookup...\n");

    puts("or something like that.");

    _exit(0);
}

int main(){
    setbuf(stdout, NULL);

    puts("*Program starting* (I will expand to multiple concurrent users later)\n");

    pthread_t tid;
    pthread_create(&tid, NULL, intarray, NULL);
    pthread_exit(NULL);

    return 0;
}
