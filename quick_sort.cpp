#include <iostream>
#include <vector>
#include "output.h"

template <typename T>
void QuickSort(std::vector<T>& data, int s, int e)
{
  if (s >= e)
    return;

  T center = data[s];
  int i = s;
  int j = e;
  while (1)
  {
    while (data[j] >= center && i < j)
    {
      j--;
    }
    while (data[i] <= center && i < j)
    {
      i++;
    }
    if (i < j)
    {
      T temp = data[j];
      data[j] = data[i];
      data[i] = temp;
    }
    else
    {
      data[s] = data[i];
      data[i] = center;
      break;
    }
  }
  QuickSort<int>(data, s, i - 1);
  QuickSort<int>(data, j + 1, e);
}

int main(int argc, char* argv[])
{
  std::vector<int> data{ 3, 1, 2, 5, 4, 3, 9, 8, 10, 8 };
  QuickSort<int>(data, 0, data.size() - 1);
  std::cout << data << std::endl;
  return 0;
}
