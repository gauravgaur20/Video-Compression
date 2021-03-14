#include "stdc.h"
using namespace std;

int main()
{
  int pic[1920][1224];

  // system("python3 matrix_save.py");

  FILE *fp;
  fp = fopen("matrix.txt","r");

  for(int i=0;i<1920;i++)
  {
    for(int j=0;j<1224;j++)
    {
      int pixel;
      fscanf(fp,"%d\n",&pixel);
      pic[i][j] = pixel;
    }
  }

  printf("%d %d",pic[0][0],pic[0][1]);

  return 0;
}
