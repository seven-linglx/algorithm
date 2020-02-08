#!/usr/bin/env python


class Solution:
    def atoi_op(self, cleaned_str):
        result = 0
        correlation = 1
        for cur in cleaned_str[::-1]:
            result += int(cur) * correlation
            correlation = 10 * correlation
        return result

    def check(self, result):
        if result < -2147483648:
            return -2147483648
        elif result > 2147483648 - 1:
            return 2147483648 - 1
        else:
            return result

    def my_atoi(self, input_str):
        required = [str(i) for i in range(10)]
        suffix_dict = {"-": -1, "+": 1}
        suffix = 1
        clened_str = ""
        for i, i_ch in enumerate(input_str):
            if i_ch == " ":
                continue
            if i_ch in required or i_ch in suffix_dict:
                if i_ch in suffix_dict:
                    suffix = suffix_dict[i_ch]
                else:
                    clened_str += i_ch
                for j_ch in input_str[i + 1 :]:
                    if j_ch in required:
                        clened_str += j_ch
                    else:
                        break
                # return self.atoi_op(clened_str)
                return self.check((int(clened_str) if clened_str else 0) * suffix)
            else:
                break
        return 0


def test_atoi_op():
    solu = Solution()
    assert solu.my_atoi(" jk234") == 0
    assert solu.my_atoi("-023") == -23
    assert solu.my_atoi("4193 with words") == 4193
    assert solu.my_atoi("words and 987") == 0
    assert solu.my_atoi("-91283472332") == -2147483648
    assert solu.my_atoi("91283472332a") == 2147483647
    assert solu.my_atoi("+") == 0
    assert solu.my_atoi("+-2") == 0
    assert solu.my_atoi("+-+2") == 0
