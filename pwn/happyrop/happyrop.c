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
    puts("?");
    int x = safeint();
    int y = safeint();
}

int main(){
    setbuf(stdout, NULL);

    puts("*Program starting* (I will expand to multiple concurrent users later)\n");

    divider();

    pthread_t tid;
    pthread_create(&tid, NULL, intarray, NULL);
    pthread_join(tid, NULL);

    int x = safeint();

    return 0;
}
