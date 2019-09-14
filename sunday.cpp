#include <string>
#include <iostream>
#include <vector>
#include <map>

using std::cout;
using std::endl;
using std::map;
using std::string;
using std::vector;

int sunday(const string& haystack, const string& needle)
{
  if (needle.length() == 0)
    return 0;

  int idx = 0;
  size_t len_needle = needle.length();
  map<char, int> lookup;
  for (int i = 0; i < needle.length(); ++i)
  {
    lookup[needle[i]] = needle.length() - i;
  }

  while (idx + len_needle <= haystack.length())
  {
    for (int i = 0; i < len_needle; ++i)
    {
      if (needle[i] != haystack[idx + i])
        break;
      if (i == len_needle - 1)
        return idx;
    }
    /*
    // 遍历方式比map数据结构时间更快 4ms in leetcode
    // 倒序找到从后往前的字符
    for (int i = len_needle - 1; i >= 0; --i)
    {
      // idx + len_src是母串在当前子串之后的首字符
      if (needle[i] == haystack[idx + len_needle])
      {
        idx += (len_needle - i);
        break;
      }
      if (i == 0)
      {
        idx += (len_needle + 1);
      }
    }
    */
    // 使用map数据结构 时间反而更久 8ms in leetcode
    if (lookup.count(haystack[idx + len_needle]) == 0)
    {
      idx += (len_needle + 1);
    }
    else
    {
      idx += lookup[haystack[idx + len_needle]];
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

  A.push_back("hello");
  B.push_back("ll");

  A.push_back("hello");
  B.push_back("ab");

  A.push_back("mississippi");
  B.push_back("issi");

  for (size_t i = 0; i < A.size(); ++i)
  {
    int result = sunday(A[i], B[i]);
    if (result != -1)
      cout << result << "\t" << A[i][result] << '\t' << A[i].substr(result, B[i].length()) << endl;
  }
}
