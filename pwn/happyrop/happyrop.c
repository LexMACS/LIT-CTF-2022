#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <string.h>
#include <seccomp.h>
#define ll long long

void divider(){
    puts("------------------------------------------------------\n");
}

void invalid(char *mes){
    printf("Invalid %s.\n", mes);
    _exit(1);
}

ll safeint(){
    char s[0x10];
    s[read(0x0, s, 0x10) - 0x1] = '\x00';
    puts("");
    return atoll(s);
}

void aradd(ll a[]){
    puts("Input the index you'd like to add to:");
    
    int idx = safeint();

    if(idx < 0 || idx >= 0x1000) invalid("index, it ain't that secure but you can't write anywhere");

    puts("Input the value you'd like to add:");

    int val = safeint();

    a[idx] += val;

    puts("Value added.\n");
}

void security(){
        scmp_filter_ctx ctx = seccomp_init(SCMP_ACT_ALLOW);

	seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(execve), 0);
	seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(execveat), 0);
	seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(mmap), 0);
	seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(remap_file_pages), 0);
	seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(socket), 0);
	seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(open), 0);
	seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(openat), 0);
	seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(connect), 0);
	seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(sendfile), 0);
	seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(socketpair), 0);
	seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(read), 0);
	seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(getdents), 0);
	seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(getdents64), 0);
	seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(write), 0);
	seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(pwrite64), 0);

	seccomp_load(ctx);
	seccomp_release(ctx);
}

void *happyrop(void *args){
    puts("Let's try again.");
    puts("I'll let you add on up to 6 values this time\n");

    ll a[0x10];
    for(int i = 0; i < 6; i++){
    	puts("Would you like to add another value? (y/N)");

	char c[0x400];
	c[read(0, c, 0x400) - 0x1] = '\0';
	puts("");

	if(!strcmp(c, "y") || !strcmp(c, "Y")) aradd(a);
	else break;
    }

    puts("Ok, that's it.\n");

    puts("Oh yeah, this would currently be too easy, so before I go I'm going to secure and close out the program.");
    puts("Bye now.");

    security();

    close(0x0);
    close(0x1);
    close(0x2);
}

int main(){
    puts("You like rop?\n");

    puts("You only get to add onto 1 index of my array (maybe you should write oob :o).\n");

    ll a[0x10];
    aradd(a);

    puts("Actually, this is dumb, let's try something else instead.\n");

    divider();

    pthread_t tid;
    pthread_create(&tid, NULL, happyrop, NULL);
    pthread_join(tid, NULL);

    return 0;
}
