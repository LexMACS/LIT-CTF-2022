#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define n 32

int size[n];
char *note[n];

int menu(){
    puts("Your options are:");
    puts("1) create");
    puts("2) delete");
    puts("3) edit");
    puts("4) display");
    puts("5) exit\n");
    
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

    if(idx < 0 || idx >= n) invalid("index, out of bounds");

    return idx;
}

void create(){
    puts("You get to create a note.\n");

    puts("Which index would you like to creat a note at?");
    int idx = inidx();

    if(note[idx]) invalid("index, already exists");

    puts("What size would you like your note to be?");
    
    scanf("%d", &size[idx]);
    getchar();
    puts("");

    if(size[idx] <= 0 || size[idx] > 0x1000) invalid("size, out of bounds");

    note[idx] = malloc(size[idx] + 1);

    puts("Note created.\n");
}

void delete(){
    puts("You get to delete a note.\n");

    puts("Which index would you like to delete a note from?");
    int idx = inidx();

    if(!note[idx]) invalid("index, does not exist");

    free(note[idx]);
    note[idx] = 0;

    puts("Note deleted.\n");
}

void edit(){
    puts("You get to edit a note.\n");

    puts("Which index would you like to edit a note at?");
    int idx = inidx();

    if(!note[idx]) invalid("index, doest not exist");
    
    puts("What message would you like the note to contain?");
    note[idx][read(0x0, note[idx], size[idx] + 1) - 1] = '\0';
    puts("");

    puts("Note edited.\n");
}
    
void display(){
    puts("You get to display a not.\n");

    puts("Which index would you like to display a note from?");
    int idx = inidx();

    if(!note[idx]) invalid("index, does not exist");

    printf("This not contains the message: %s\n\n", note[idx]);

    puts("Note displayed.\n");
}

int main(){
    puts("Welcome to my heapnote challenge.\n");

    for(int x = 0; x != 5;){
        x = menu();
        switch(x){
            case 1:
                create();
                break;
            case 2:
                delete();
                break;
            case 3:
                edit();
                break;
            case 4:
                display();
                break;
            case 5:
                puts("Bye.");
                break;
            default:
                invalid("option, does not exist");
                break;
        }
    }
    
    return 0;
}
