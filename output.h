#include <vector>
#include <iostream>
#include <string>
#include <sstream>

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
