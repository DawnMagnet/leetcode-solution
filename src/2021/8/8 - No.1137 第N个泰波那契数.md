# No.1137 第N个泰波那契数
<p>泰波那契序列&nbsp;T<sub>n</sub>&nbsp;定义如下：&nbsp;</p>

<p>T<sub>0</sub> = 0, T<sub>1</sub> = 1, T<sub>2</sub> = 1, 且在 n &gt;= 0&nbsp;的条件下 T<sub>n+3</sub> = T<sub>n</sub> + T<sub>n+1</sub> + T<sub>n+2</sub></p>

<p>给你整数&nbsp;<code>n</code>，请返回第 n 个泰波那契数&nbsp;T<sub>n </sub>的值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 4
<strong>输出：</strong>4
<strong>解释：</strong>
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 25
<strong>输出：</strong>1389537
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 37</code></li>
	<li>答案保证是一个 32 位整数，即&nbsp;<code>answer &lt;= 2^31 - 1</code>。</li>
</ul>

# 思路分析
通过观察，发现题目要求的是一个数列的和。而且这个数列可以通过前面的3项来计算得到后面的一项。因此我们可以用最简单的暴力算法来做。
也就是我们新建一个数组，里面有固定的三项`[0,1,1]`。这是题目中给我们的条件，然后我们根据给入的n去计算到我们需要的地方，就可以获得第 N 个泰波那契数了
# Rust代码
```rust
# struct Solution;
impl Solution {
    pub fn tribonacci(n: i32) -> i32 {
        let n = n as usize;
        let mut v = vec![0, 1, 1];
        let mut cur_len = 3;
        while cur_len <= n {
            v.push(v[cur_len - 1] + v[cur_len - 2] + v[cur_len - 3]);
            cur_len += 1;
        }
        v[n]
    }
}
```
# 运行效果
```rust,editable
# fn main() {
# pub fn tribonacci(n: i32) -> i32 {
#    let n = n as usize;
#    let mut v = vec![0, 1, 1];
#    let mut cur_len = 3;
#    while cur_len <= n {
#        v.push(v[cur_len - 1] + v[cur_len - 2] + v[cur_len - 3]);
#        cur_len += 1;
#    }
#    v[n]
# }
println!("{:?}", tribonacci(2));
# }
```