#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include "output.h"

using namespace std;

int add(int x, int y)
{
  return (x + y);
}

int multiply(int x, int y)
{
  return (x * y);
}

void testLambda()
{
  vector<int> s(5, 1);
  vector<int> a(2, 2);
  vector<int> b(5);
  transform(s.begin(), s.end(), a.begin(), b.begin(), [](int const& x, int const& y) -> int { return add(x, y); });
  cout << b << endl;
}

void testLambda2()
{
  vector<int> s{ 0, 1, 2, 3, 4 };
  vector<int> a(2);
  a[0] = (1);
  a[1] = (2);
  vector<int> b(5);
  for (size_t i = 0; i < a.size(); ++i)
  {
    transform(s.begin(), s.end(), b.begin(), [a, i](int const& x) -> int { return add(x, a[i]); });
    cout << b << endl;
  }
}

void testLambda3()
{
  vector<int> s{ -2, -1, 0, 1, 2 };
  vector<int> a(2);
  a[0] = (-1);
  a[1] = (2);
  vector<int> const& a_const = a;
  vector<int> b(5);
  int i = 0;
  long idx =
      max_element(s.begin(), s.end(),
                  ([&a_const, i](int x, int b) -> bool { return multiply(x, a_const[i]) < multiply(b, a_const[i]); })) -
      s.begin();
  cout << idx << '\t' << s[idx] << endl;
}

void testLambda4()
{
  int a, b, c;
  a = b = c = 10;
  cout << a << b << c << endl;
  const int vec[3] = { 0 };
  auto func = [&a](int v) { cout << v + a << endl; };
  for (auto i : vec)
  {
    func(i);
    ++a;
  }
}

// 练习lambda语法，并使用其处理vector
int main()
{
  // testAuto();
  testLambda3();
  return 0;
}
