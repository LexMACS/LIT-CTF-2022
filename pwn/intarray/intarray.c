#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <string.h>
#define ll long long

void invalid(char *mes){
    printf("Invalid %s.\n", mes);
    _exit(1);
}

void divider(){
    puts("------------------------------------------------------\n");
}

ll safeint(){
    char s[0x10];
    s[read(0x0, s, 0x10) - 0x1] = '\x00';
    puts("");
    return atoll(s);
}

void *intarray(void *args){
    int n, idx;
    ll val;
    ll a[0x100];

    puts("Welcome to my int array storage program!\n");

    puts("How many ints would you like to store?");
    
    n = safeint();
    if(n <= 0 || n > 0x100) invalid("size, out of bounds");

    memset(a, 0, n * sizeof(int));

    divider();

    puts("You can edit one value (this is only beta version).\n");

    puts("Input an index:");

    idx = safeint();
    if(idx < 0 || (unsigned char)idx >= n) invalid("index, out of bounds");
    
    puts("Input the change:");

    val = safeint();
    a[idx] += val;

    puts("Edit complete.");

    divider();

    puts("You can clear up to two indices if you made a mistake (this is only beta version).\n");

    for(int i = 0; i < 2; i++){
        puts("Would you like to fix another mistake? (y/N)");

        char c = getchar();
        getchar();
        puts("");

        if(c == 'y' || c == 'Y'){
            puts("Input an index:");

            idx = safeint();
            if(idx < 0 || (unsigned char)idx >= n) invalid("index, out of bounds");

            a[idx] = 0;

	    puts("Clear complete.\n");
        }else{
	    break;
	}
    }

    divider();

    puts("The array will now be safely stored on a blockchain distributed across a convex hull network using ai-enhanced chacha cipher encryption technology with bloom filters for fast lookup...\n");

    puts("or something like that.");    

    _exit(0);
}

int main(){
    setbuf(stdout, NULL);

    puts("*Program starting* (I will expand to multiple concurrent users later)\n");

    divider();

    pthread_t tid;
    pthread_create(&tid, NULL, intarray, NULL);
    pthread_exit(NULL);

    return 0;
}
