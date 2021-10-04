# No.482 密钥格式化
<p>有一个密钥字符串 S ，只包含字母，数字以及 '-'（破折号）。其中， N 个 '-' 将字符串分成了 N+1 组。</p>

<p>给你一个数字 K，请你重新格式化字符串，使每个分组恰好包含 K 个字符。特别地，第一个分组包含的字符个数必须小于等于 K，但至少要包含 1 个字符。两个分组之间需要用 '-'（破折号）隔开，并且将所有的小写字母转换为大写字母。</p>

<p>给定非空字符串 S 和数字 K，按照上面描述的规则进行格式化。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>S = "5F3Z-2e-9-w", K = 4
<strong>输出：</strong>"5F3Z-2E9W"
<strong>解释：</strong>字符串 S 被分成了两个部分，每部分 4 个字符；
&nbsp;    注意，两个额外的破折号需要删掉。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>S = "2-5g-3-J", K = 2
<strong>输出：</strong>"2-5G-3J"
<strong>解释：</strong>字符串 S 被分成了 3 个部分，按照前面的规则描述，第一部分的字符可以少于给定的数量，其余部分皆为 2 个字符。
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ol>
	<li>S 的长度可能很长，请按需分配大小。K 为正整数。</li>
	<li>S 只包含字母数字（a-z，A-Z，0-9）以及破折号'-'</li>
	<li>S 非空</li>
</ol>

<p>&nbsp;</p>

# 思路分析

待补充

# Rust代码
```rust
# struct Solution;
impl Solution {
    pub fn license_key_formatting(s: String, k: i32) -> String {
        let k = k as usize;
        let n = s.len();
        let count = s.chars().fold(0, |acc, x| acc + (x == '-') as usize);
        let valid = n - count;
        let parts = valid / k + (valid % k > 0) as usize;
        let mut remains = if valid % k == 0 {k} else {valid % k};
        let mut res = "".to_string();
        for ch in s.chars() {
            if ch == '-' {
                continue;
            }
            if remains == 0 {
                res.push('-');
                remains = k;
            }
            res.push(ch.to_ascii_uppercase());
            remains -= 1;
        }
        res
    }
}
```
