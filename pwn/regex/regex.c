#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <regex.h>

char *s;
regex_t *preg;
regmatch_t *pmatch;

void invalid(char *mes){
    printf("Invalid %s.\n", mes);
    _exit(1);
}

int insz(){
    int sz;
    scanf("%d", &sz);
    getchar();
    puts("");
        
    if(sz <= 0 || sz > 0x30000) invalid("size, out of bounds");
    return sz;
}

void instr(int sz){
    fgets(s, sz + 1, stdin);
    s[strcspn(s, "\n")] = '\0';
    puts("");
}

void divider(){
    puts("------------------------------------------------------\n");
}

int input_pattern(){
    puts("Input the size of your pattern:");

    int sz = insz();
    free(s);
    s = malloc(sz + 1);

    puts("Input your pattern:");
    
    instr(sz);

    preg = malloc(sizeof(regex_t));
    int er = regcomp(preg, s, 0);

    return er;
}

void match_string(){
    puts("Input the size of the string you'd like to match:");

    int sz = insz();
    free(s);
    s = malloc(sz + 1);

    puts("Input the string you'd like to match:");

    instr(sz);

    puts("Input the number of subexpressions matches you'd like to list:");

    int nmatch;
    scanf("%d", &nmatch);
    getchar();
    puts("");

    if(nmatch < 0 || nmatch > 0x1000) invalid("# subexpressions, out of bounds");

    nmatch += 1;
    free(pmatch);
    pmatch = malloc(nmatch * sizeof(regmatch_t));

    regexec(preg, s, nmatch, pmatch, 0);

    puts("Matching complete.\n");

    puts("Here is the first match interval found:");
    printf("[%d, %d]\n", pmatch[0].rm_so, pmatch[0].rm_eo - 1);
    puts("");

    puts("Here are the subexpressions found:");
    for(int i = 1; i < nmatch; i++){
        printf("%d: [%d, %d]\n", i, pmatch[i].rm_so, pmatch[i].rm_eo - 1);
    }
    puts("");
}

int main(){
    puts("Welcome to my regex pattern searching program!\n");

    puts("First you need to initialize the pattern.\n");

    for(int er = -1; er == -1 || er == REG_EPAREN || er == REG_EBRACK || er == REG_EBRACE || er == REG_EESCAPE || er == REG_BADBR || er == REG_BADPAT || er == REG_BADRPT;){
    	er = input_pattern();
	if(er != 0){
	    puts("Invalid expression, try again.\n");
	    free(preg);
	}
    }

    puts("Pattern initialized.\n");

    divider();

    puts("Now you can match strings to your pattern.\n");

    while(1){
        match_string();

        puts("Would you like to match another string? (y/N)");

        char c;
        scanf("%c", &c);
        getchar();
        puts("");

        if(c != 'y' && c != 'Y'){
            break;
        }
    }

    regfree(preg);

    divider();

    puts("I hope you liked our program!\n");

    puts("Before you go, could you leave a review?\n");

    puts("Input your review length:");

    int sz = insz();
    free(s);
    s = malloc(sz);

    puts("Input your reivew:");

    instr(sz);

    puts("Thanks!");

    _exit(0);

    return 0;
}
