//
// Created by linglx on 18-3-22.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool max_comp(pair<int, int>& one, pair<int, int>& two) {
    return (one.second - one.first) < (two.second - two.first);
}

bool comp(pair<int, int>& one,
          pair<int, int>& two) {
    return (one.second - one.first) < (two.second - two.first);
}

std::pair<int, int> f(std::string &str) {
    std::vector<std::pair<int, int>> pair_vec;
    auto *a = const_cast<char *>(str.data());
    auto len = static_cast<int>(str.length());
    // cout << *a << endl;

    int s_right = -1;
    int e_right = -1;

    int s = 0;
    int e = len - 1;
    for (int i = 0; i < len - 1; ++i) {
        s = i;
        if (!isalpha(*(a + s))) continue;

        e = len - 1;
        while (e > s) {
            if (!isalpha(*(a + e))) e--;

            if (*(a + s) == *(a + e)) {
                if (s_right == -1 && e_right == -1) {
                    s_right = s;
                    e_right = e;
                }
                s++;
                e--;
            } else {
                s_right = -1;
                e_right = -1;
                e--;
                s = i;
            }

            if (s == e || (s - e) == 1) {
                if (s_right != -1 && e_right != -1) {
                    std::pair<int, int> p(s_right, e_right);
                    pair_vec.push_back(p);
                }
                break;
            }
        }
    }
    auto it =
//    std::max(pair_vec, max_comp); // not work
    std::max_element(pair_vec.begin(), pair_vec.end(), comp);
//    cout << it->first << '\t' << it->second << endl;
    return *it;

    /*
    int max = 0;
    int idx = -1;
    for (int i = 0; i < pair_vec.size(); ++i) {
        if (max < (pair_vec[i].second - pair_vec[i].first)) {
            idx = i;
            max = (pair_vec[i].second - pair_vec[i].first);
        }
        // cout << pair_vec[i].first << '\t' << pair_vec[i].second << endl;
    }
    pair<int, int> empty(-1, -1);
    if (idx == -1)
        return empty;
    else
        return pair_vec[idx];
    */
}

int main() {
    string a = "bbab23abe3ceabae2fg";
    pair<int, int> p = f(a);
    for (int i = p.first; i <= p.second; ++i)
        cout << a[i];
    cout << endl;
    return 0;
}
