#include <iostream>
#include <math.h>
#include <sstream>
#include <vector>

int gCount = 0;
bool isValid(const std::vector<int>& positions, int row, int col)
{
  for (int i = 0; i < row; ++i)
  {
    const int& d = positions[i];
    if (d == col)
      return false;
    if (std::abs(d - col) == std::abs(i - row))
      return false;
  }
  return true;
}

void findPosition(std::vector<int>& positions, int row, int N)
{
  for (int i = 0; i < N; ++i)
  {
    if (isValid(positions, row, i))
    {
      positions[row] = i;
      if (row == (N - 1))
      {
        gCount++;
        positions[row] = 0;
        return;
      }
      findPosition(positions, row + 1, N);
    }
  }
}

// 使用递归求解八皇后问题
int main()
{
  int N = 8;
  std::vector<int> positions(N, 0);
  findPosition(positions, 0, N);
  std::cout << gCount << std::endl;
  return 0;
}
