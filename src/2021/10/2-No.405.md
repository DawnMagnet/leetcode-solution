# No.405 数字转换为十六进制数
<p>给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用&nbsp;<a href="https://baike.baidu.com/item/%E8%A1%A5%E7%A0%81/6854613?fr=aladdin">补码运算</a>&nbsp;方法。</p>

<p><strong>注意:</strong></p>

<ol>
	<li>十六进制中所有字母(<code>a-f</code>)都必须是小写。</li>
	<li>十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符<code>'0'</code>来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。&nbsp;</li>
	<li>给定的数确保在32位有符号整数范围内。</li>
	<li><strong>不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。</strong></li>
</ol>

<p><strong>示例 1：</strong></p>

<pre>输入:
26

输出:
"1a"
</pre>

<p><strong>示例 2：</strong></p>

<pre>输入:
-1

输出:
"ffffffff"
</pre>

# 思路分析

本质上就是一个二进制转十六进制的操作。最好使用二进制运算来做，能够更高效地利用计算机二进制的架构。

一位十六进制对应到四位二进制。

# Rust代码
```rust
# struct Solution;
impl Solution {
    pub fn to_hex(num: i32) -> String {
        let turned: Vec<char> = "0123456789abcdef".chars().collect();
        let mut num = num as u32;
        if num == 0 {
            return "0".to_string();
        }
        let mut res = vec![];
        while num != 0 {
            let mut tmp = 0;
            for i in 0..4 {
                tmp += (num & 1) * (1 << i);
                num >>= 1;
            }
            res.push(turned[tmp as usize]);
        }
        res.reverse();
        res.iter().collect()
    }
}
```

# C++代码
```cpp
static const char * turned = "0123456789abcdef";
class Solution {
public:
    string toHex(unsigned int num) {
        string res;
        do {
            int tmp = 0;
            for (int i = 0; i < 4; ++i) {
                tmp += (num & 1) * (1 << i);
                num >>= 1;
            }
            res.push_back(turned[tmp]);
        } while (num != 0);
        reverse(res.begin(), res.end());
        return res;
    }
};
```