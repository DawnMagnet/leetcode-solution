# No.166 分数到小数
<p>给定两个整数，分别表示分数的分子&nbsp;<code>numerator</code> 和分母 <code>denominator</code>，以 <strong>字符串形式返回小数</strong> 。</p>

<p>如果小数部分为循环小数，则将循环的部分括在括号内。</p>

<p class="MachineTrans-lang-zh-CN">如果存在多个答案，只需返回 <strong>任意一个</strong> 。</p>

<p class="MachineTrans-lang-zh-CN">对于所有给定的输入，<strong>保证</strong> 答案字符串的长度小于 <code>10<sup>4</sup></code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>numerator = 1, denominator = 2
<strong>输出：</strong>"0.5"
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>numerator = 2, denominator = 1
<strong>输出：</strong>"2"
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>numerator = 2, denominator = 3
<strong>输出：</strong>"0.(6)"
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>numerator = 4, denominator = 333
<strong>输出：</strong>"0.(012)"
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>numerator = 1, denominator = 5
<strong>输出：</strong>"0.2"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;=&nbsp;numerator, denominator &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>denominator != 0</code></li>
</ul>

# 思路分析

待补充

# Rust代码
```rust
# struct Solution;
use std::collections::HashMap;
pub fn gcd(a: i64, b: i64) -> i64 {
    return if a % b == 0 {
        b
    } else {
        gcd(b, a % b)
    }
}
impl Solution {
    pub fn fraction_to_decimal(numerator: i32, denominator: i32) -> String {
        let mut ret = String::new();
        if (numerator as i64 * denominator as i64) < 0 {
            ret.push('-');
        }
        let denominator = (denominator as i64).abs();
        let numerator = (numerator as i64).abs();
        let g = gcd(numerator, denominator);
        let mut denominator = denominator / g;
        let mut numerator = numerator / g;
        let pre = numerator / denominator;
        numerator %= denominator;
        let mut map: HashMap<i64, i32> = HashMap::new();
        ret.push_str(&pre.to_string());
        if numerator == 0 {
            return ret;
        }
        ret.push('.');
        let mut ws = ret.len() as i32;
        loop {
            if numerator == 0 {
                break;
            }
            if map.contains_key(&numerator) {
                ret.insert(*map.get(&numerator).unwrap() as usize, '(');
                ret.push(')');
                break;
            }
            map.insert(numerator, ws);
            numerator *= 10;
            ret.push((('0' as u8) + (numerator / denominator) as u8) as char);
            numerator %= denominator;
            ws += 1;
        }
        ret
    }
}
```
