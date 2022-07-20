#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#define ll long long

#define n 16

int size[n];
char *container[n];
int mistake;

int menu(){
    puts("Your options are:");
    puts("1) catch cockroach");
    puts("2) exterminate cockroach");
    puts("3) look at cockroach");
    puts("4) dance with cockroach???");
    puts("5) evacuate house\n");
    
    puts("What would you like to do?");

    int x;
    scanf("%d", &x);
    getchar();
    puts("");

    return x;
}

void invalid(char *mes){
    printf("Invalid %s.\n", mes);
    _exit(1);
}

int inidx(){
    int idx;
    scanf("%d", &idx);
    getchar();
    puts("");
    
    if(idx < 0 || idx >= n) invalid("container, does not exist");
    return idx;
}

void catch(){
    puts("You are going to catch a cockroach.\n");

    puts("Which container would you like to store it in?");
    int idx = inidx();

    if(container[idx]) invalid("container, already storing cockroach");

    puts("How large is the cockroach you are catching?");
    scanf("%d", &size[idx]);
    getchar();
    puts("");

    if(size[idx] <= 0x500 || size[idx] > 0x10000) invalid("size, none like that exist");

    container[idx] = malloc(size[idx] + 1);

    puts("Cockroach caught.\n");
}

void exterminate(){
    puts("You are going to exterminate a cockroach.\n");

    puts("Which container would you like to exterminate the cockroach in?");
    int idx = inidx();

    if(!container[idx]) invalid("container, no cockroach stored");

    free(container[idx]);

    puts("Did you remember to close the container lid? (y/N)");
    char c = getchar();
    getchar();
    puts("");

    if(c == 'y' || c == 'Y'){
	container[idx] = 0;

    	puts("Nice job, cockroach exterminated.\n");
    }else{
    	if(mistake) invalid("decison, 'fool me once shame on you, fool me twice shame on me'");

	puts("Rip, cockroach escaped.\n");

	mistake = 1;
    }
}
    
void look(){
    puts("You are going to look at a cockroach.\n");

    puts("Which container do you want to look at?");
    int idx = inidx();

    if(!container[idx]) invalid("container, no cockroach stored");

    puts("Here is what you saw:");
    puts(container[idx]);

    puts("Cockroach has been seen.\n");
}

void dance(){
    puts("You are going to dance with a cockroach???\n");

    puts("Do you really want to do this? (0/1)");

    ll x;
    scanf("%lld", &x);
    puts("");
    
    if(!x){
    	puts("Yeah, that would be weird.\n");
	return;
    }

    puts("Um... ok.\n");

    puts("Which container holds the cockroach you would like to dance with?");

    int idx = inidx();

    if(!container[idx]) invalid("container, no cockroach stored");
    
    puts("You can now clothe the cockroach (you know, for the dance floor):");

    container[idx][read(0x0, container[idx], size[idx] + 1) - 1] = '\0';
    puts("");

    if(strchr(container[idx], 'n')) invalid("clothing, bad design");

    puts("Here's what she looks like:");
    printf(container[idx]);
    puts("");

    _exit(0);
}


int main(){
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);

    puts("Welcome to the house of cockarocha.\n");

    for(int x = -1; x != 5;){
        x = menu();
        switch(x){
            case 1:
                catch();
                break;
            case 2:
                exterminate();
                break;
            case 3:
                look();
                break;
            case 4:
                dance();
                break;
            case 5:
                puts("The cockarochas will miss you :(.");
                break;
            default:
                invalid("option, does not exist");
                break;
        }
    }

    _exit(0);
    
    return 0;
}
