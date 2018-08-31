#include <string>
#include <iostream>
#include <vector>

using std::cout;
using std::endl;
using std::string;
using std::vector;

int sunday(const string& tar, const string& src)
{
  int idx = 0;
  size_t len_src = src.length();
  while (idx + len_src <= tar.length())
  {
    for (size_t i = 0; i < len_src; ++i)
    {
      if (src[i] != tar[idx + i])
        break;
      if (i == len_src - 1)
        return idx;
    }
    for (size_t i = 0; i < len_src; ++i)
    {
      if (src[i] == tar[idx + len_src])
      {
        idx += len_src - i;
        break;
      }
      if (i == len_src - 1)
      {
        idx += len_src + 1;
      }
    }
  }
  return -1;
}

// Sunday字符串匹配算法
int main()
{
  vector<string> A;
  vector<string> B;
  A.push_back("BBC ABCDAB ABCDABCDABDE");
  B.push_back("ABCDABD");

  A.push_back("substring searching algorithm");
  B.push_back("search");

  A.push_back("HERE IS A SIMPLE EXAMPLE");
  B.push_back("EXAMPLE");

  for (size_t i = 0; i < A.size(); ++i)
  {
    int result = sunday(A[i], B[i]);
    if (result != -1)
      cout << result << ": " << A[i][result] << endl;
  }
}
