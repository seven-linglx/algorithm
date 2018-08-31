#include <iostream>
#include <math.h>
#include <sstream>
#include <vector>

int gCount = 0;

template <typename T>
inline std::ostream& operator<<(std::ostream& o, std::vector<T> const& v)
{
  std::stringstream s;
  for (size_t i = 0; i < v.size(); i++)
  {
    if (i != v.size() - 1)
      s << v[i] << ", ";
    else
      s << v[i];
  }
  return o << "vector: " << s.str();
}

bool isEnd(const std::vector<int>& steps, int level, int N)
{
  int count = 0;
  for (int i = 0; i <= level; ++i)
  {
    count += steps[i];
  }
  return (count == N);
}

void stair(std::vector<int>& steps, int level, int N)
{
  if (level >= N)
  {
    return;
  }
  for (int i = 1; i < 3; ++i)
  {
    steps[level] = i;
    if (isEnd(steps, level, N))
    {
      gCount++;
      std::cout << steps << std::endl;
      steps[level] = 0;
      return;
    }
    stair(steps, level + 1, N);
  }
}

// 使用递归求解爬楼梯问题
int main(int argc, char** argv)
{
  int N = std::atoi(argv[argc - 1]);
  std::vector<int> step(N, 0);
  stair(step, 0, N);
  std::cout << gCount << std::endl;
  return 0;
}
