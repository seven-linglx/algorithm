#include <iostream>
#include <cmath>
#include <vector>
#include <Eigen/Core>

#define F (INFINITY)

template <typename T>
inline std::ostream& operator<<(std::ostream& o, const std::vector<T>& d)
{
  for (size_t i = 0; i < d.size(); i++)
  {
    if (i != d.size() - 1)
      o << d[i] << ",";
    else
      o << d[i];
  }
  return o;
}

void dijkstar(const Eigen::MatrixXf& data, int m, std::vector<float>& dis)
{
  float min = F;
  float idx = 0;
  std::vector<int> flag(dis.size(), 0);
  flag[0] = 1;
  for (int i = 1; i < m; ++i)
  {
    min = F;
    idx = i;
    for (int j = 1; j < m; ++j)
    {
      if (dis[j] < min && flag[j] == 0)
      {
        min = data(i, j);
        idx = j;
      }
    }
    flag[idx] = 1;

    for (int k = 1; k < m; ++k)
    {
      if (data(idx, k) < F)
      {
        if (dis[k] > dis[idx] + data(idx, k))
        {
          dis[k] = dis[idx] + data(idx, k);
        }
      }
    }
  }
}

// 实现定点最短路径算法Dijkstar
int main()
{
  // clang-format off
  Eigen::MatrixXf data(5, 5);
  data << 0, 3, 2, F, F,
          3, 0, 2, 4, 5,
          2, 2, 0, 1, 7,
          F, 4, 1, 0, 3,
          F, F, 7, 1, 0;
  // clang-format on
  std::vector<float> dis{ 0, 3, 2, F, F };
  dijkstar(data, 5, dis);
  std::cout << dis << std::endl;
  return 0;
}
