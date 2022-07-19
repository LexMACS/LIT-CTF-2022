#include <stdio.h>
#include <stdlib.h>
#include <time.h>

unsigned char grid[800][1200][3];

bool get(unsigned char uc[3],int pos) {
	bool current = (uc[pos / 8] >> (pos % 8)) & 1;
	return current;
}

int main() {
	bool arr[50 * 8];

	FILE* original_file = fopen("yougotrickrolledChallenge.bmp","r");
	for(int i = 0;i < 54 + 84;++i) {
		unsigned char b;
		fread(&b,1,1,original_file);
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
		arr[i] = get(grid[posX][posY],bit);
		bit = (bit + 1) % 24;
		if(arr[i]) {
			posX++;
		}else{
			posY++;
		}
		printf("%d",arr[i]);
	}
	printf("\n");

	fclose(original_file);
	return 0;
}
