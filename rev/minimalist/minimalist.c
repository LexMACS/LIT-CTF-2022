#include <stdio.h>

long long xor[47] = {52, 96, 122, 30, 57, 75, 121, 37, 88, 20, 43, 72, 117, 86, 51, 99, 104, 125, 16, 20, 2, 63, 99, 127, 100, 123, 13, 5, 112, 58, 125, 96, 12, 47, 41, 76, 8, 65, 119, 31, 27, 97, 83, 53, 120, 53, 63};

long long ans[47] = {-121, -45, -52, -75, -123, -32, -64, -95, -16, -125, -28, -24, -28, -102, -1, -8, -28, -35, -114, -38, -52, -97, -24, -24, -85, -9, -73, -91, -23, -15, -20, -4, -118, -113, -25, -35, -124, -54, -6, -107, -121, -22, -59, -91, -23, -71, -1};

int main(){
    printf("Enter the flag: \n");
    for(int i = 0; i < 47; i++){
        int x = getchar();
        if(i == 0) __asm__ __volatile__("push %%rax;" : : "a" (x));
        __asm__ __volatile__("push %%rax;" : : "a" (ans[i]));
        __asm__ __volatile__("push %%rax;" : : "a" (xor[i]));
        __asm__ __volatile__("push %%rax;" : : "a" (x));
    }
    long long ret = 0;
    for(int i = 0; i < 47; i++){
        __asm__ __volatile__(
"pop %%r13;" // swap
"pop %%r11;" // xor
"pop %%r14;" // ans
"pop %%r10;" // char
"push %%r13;"
// debug
//"mov %%r10, %%rbx;"
// XOR(r10, r11)
"not %%r10;"
"push %%r11;"
"pop %%r12;"
"or %%r10, %%r12;"
"not %%r12;" // AND(r10, NOT(r11))
"not %%r10;"
"not %%r11;"
"push %%r11;"
"pop %%r13;"
"or %%r10, %%r13;"
"not %%r13;" // AND(r11, NOT(r10))
"or %%r13, %%r12;"
// AND(r12, r14)
"push %%r12;"
"push %%r14;"
"push %%r12;"
"push %%r14;"
"pop %%r10;"
"pop %%r11;"
"not %%r10;"
"not %%r11;"
"push %%r11;"
"pop %%r12;"
"or %%r10, %%r12;"
"not %%r12;"
// OR(rax, r12)
"or %%r12, %%rax;"
// NOR(r12, r14)
"pop %%r10;"
"pop %%r12;"
"or %%r10, %%r12;"
"not %%r12;"
// OR(rax, r12)
"or %%r12, %%rax;"
        : "=a" (ret)
        : "a" (ret)
        : "r10", "r11", "r12", "r13", "r14");
    }
    __asm__ __volatile__(
// NOR(r10, ~0x7d)
"pop %%r10;"
"push %%r10;"
"push $0xffffffffffffff82;"
"pop %%r11;"
"or %%r11, %%r10;"
"not %%r10;"
// OR(r10, rax)
"or %%r10, %%rax;"
// AND(r10, ~0x7d)
"pop %%r10;"
"push $0xffffffffffffff82;"
"pop %%r11;"
"not %%r10;"
"not %%r11;"
"push %%r11;"
"pop %%r12;"
"or %%r10, %%r12;"
"not %%r12;"
// OR(r12, rax)
"or %%r12, %%rax;"
: "=a" (ret)
: "a" (ret)
: "r10"
    );
    if(ret){
        printf("Wrong flag!\n");
    }else{
        printf("The flag is correct.\n");
    }
}
