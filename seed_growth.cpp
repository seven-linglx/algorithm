//
// Created by linglx on 18-8-11.
//

#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <Eigen/Core>

void seedGrowth(Eigen::MatrixXi const& a, Eigen::MatrixXi& m, long column, long row)
{
  std::queue<std::pair<int, int>> seeds;
  std::vector<std::vector<std::pair<int, int>>> obstacles;
  std::vector<std::pair<int, int>> obstacle;
  for (int i = 0; i < row; ++i)
  {
    for (int j = 0; j < column; ++j)
    {
      if (a(i, j) == 0)
        continue;

      if (!m(i, j))
      {
        seeds.push(std::pair<int, int>(i, j));
        m(i, j) = 1;
      }
      while (!seeds.empty())
      {
        const std::pair<int, int>& c = seeds.front();
        obstacle.push_back(c);
        // up
        if ((c.first - 1 >= 0) && a(c.first - 1, c.second) && !m(c.first - 1, c.second))
        {
          seeds.push(std::pair<int, int>(c.first - 1, c.second));
          m(c.first - 1, c.second) = 1;
        }
        // down
        if ((c.first + 1 < row) && a(c.first + 1, c.second) && !m(c.first + 1, c.second))
        {
          seeds.push(std::pair<int, int>(c.first + 1, c.second));
          m(c.first + 1, c.second) = 1;
        }
        // left
        if ((c.second - 1 >= 0) && a(c.first, c.second - 1) && !m(c.first, c.second - 1))
        {
          seeds.push(std::pair<int, int>(c.first, c.second - 1));
          m(c.first, c.second - 1) = 1;
        }
        // right
        if ((c.second + 1 < column) && a(c.first, c.second + 1) && !m(c.first, c.second + 1))
        {
          seeds.push(std::pair<int, int>(c.first, c.second + 1));
          m(c.first, c.second + 1) = 1;
        }
        seeds.pop();
      }
      if (!obstacle.empty())
      {
        obstacles.push_back(obstacle);
        obstacle.clear();
      }
    }
  }
  for (int i = 0; i < obstacles.size(); ++i)
    std::cout << "Obstacle " << i << " : " << obstacles[i].size() << std::endl;
}

int main(int argc, char* argv[])
{
  Eigen::MatrixXi a(3, 6);
  // clang-format off
  a << 1, 0, 1, 0, 1, 1,
       0, 0, 1, 1, 0, 1,
       0, 1, 1, 0, 0, 0;
  // clang-format on
  Eigen::MatrixXi m(3, 6);
  m = Eigen::Matrix<int, 3, 6>::Zero();

  seedGrowth(a, m, a.cols(), a.rows());
}
