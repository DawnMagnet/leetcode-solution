# No.434 字符串中的单词数
<p>统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。</p>

<p>请注意，你可以假定字符串里不包括任何不可打印的字符。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> "Hello, my name is John"
<strong>输出:</strong> 5
<strong>解释: </strong>这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。
</pre>

# 思路分析

这题考察的有点像状态机。因为需要维护一个前一个字符是不是字母的状态。如果前一个是空格，后一个是字母，就说明开始了一个新单词。

# Rust代码
```rust
# struct Solution;
impl Solution {
    pub fn count_segments(s: String) -> i32 {
        let mut state = 0;
        let mut res = 0;
        for ch in s.chars() {
            if ch == ' ' {
                state = 0;
            } else {
                if state == 0 {
                    res += 1;
                }
                state = 1;
            }
        }
        res
    }
}
```
