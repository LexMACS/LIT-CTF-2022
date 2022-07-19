#include <stdio.h>
#include <stdlib.h>
#include <time.h>

unsigned char grid[800][1200][3];

void alter(unsigned char uc[3],int pos,bool bit) {
	bool current = (uc[pos / 8] >> (pos % 8)) & 1;
	uc[pos / 8] ^= (current ^ bit) << (pos % 8);
	return;
}

int main() {
	unsigned char flag[50];
	FILE* flag_file = fopen("flag.txt","r");
	bool arr[50 * 8];
	if(flag_file == (FILE *)0x0) {
		puts("Error: The flag file does not exist");
		exit(0);
	}
	if(fread(flag,50,1,flag_file) < 1) {
		puts("Error: The flag is too short");
		exit(0);
	}
	for(int i = 0;i < 50;++i) {
		for(int j = 0;j < 8;++j) {
			arr[i * 8 + j] = (flag[i] >> (7 - j)) & 1;
			// printf("%d",arr[i * 8 + j]);
		}
	}

	FILE* original_file = fopen("yougotrickrolled.bmp","r");
	FILE* output_file = fopen("yougotrickrolledChallenge.bmp","w");
	for(int i = 0;i < 54 + 84;++i) {
		unsigned char b;
		fread(&b,1,1,original_file);
		fputc(b,output_file);
	}
	// printf("%d",working);

	for(int i = 0;i < 800;++i) {
		for(int j = 0;j < 1200;++j) {
			for(int k = 0;k < 3;++k) {
				fread(&grid[i][j][k],1,1,original_file);
			}
		}
	}

	int posX = 0;
	int posY = 0;
	int bit = 0;

	for(int i = 0;i < 50 * 8;++i) {
		alter(grid[posX][posY],bit,arr[i]);
		bit = (bit + 1) % 24;
		if(arr[i]) {
			posX++;
		}else{
			posY++;
		}
	}

	for(int i = 0;i < 800;++i) {
		for(int j = 0;j < 1200;++j) {
			for(int k = 0;k < 3;++k) {
				fputc(grid[i][j][k],output_file);
			}
		}
	}
	
	fclose(flag_file);
	fclose(original_file);
	fclose(output_file);
	return 0;
}
