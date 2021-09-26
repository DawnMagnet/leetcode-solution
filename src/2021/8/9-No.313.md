# No.313 超级丑数
<p><strong>超级丑数</strong> 是一个正整数，并满足其所有质因数都出现在质数数组 <code>primes</code> 中。</p>

<p>给你一个整数 <code>n</code> 和一个整数数组 <code>primes</code> ，返回第 <code>n</code> 个 <strong>超级丑数</strong> 。</p>

<p>题目数据保证第 <code>n</code> 个 <strong>超级丑数</strong> 在 <strong>32-bit</strong> 带符号整数范围内。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 12, primes = [2,7,13,19]
<strong>输出：</strong>32 
<strong>解释：</strong>给定长度为 4 的质数数组 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 1, primes = [2,3,5]
<strong>输出：</strong>1
<strong>解释：</strong>1 不含质因数，因此它的所有质因数都在质数数组 primes = [2,3,5] 中。
</pre>
&nbsp;

<div class="top-view__1vxA">
<div class="original__bRMd">
<div>
<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= primes.length &lt;= 100</code></li>
	<li><code>2 &lt;= primes[i] &lt;= 1000</code></li>
	<li>题目数据<strong> 保证</strong> <code>primes[i]</code> 是一个质数</li>
	<li><code>primes</code> 中的所有值都 <strong>互不相同</strong> ，且按 <strong>递增顺序</strong> 排列</li>
</ul>
</div>
</div>
</div>

# 思路分析
题目的意思还是比较好理解的，我们需要列出来一个列表（的前n项），这个列表里包括了所有的超级丑数，而我们关心的就是只有第n个超级丑数。
列这个表有许多种思路。比较常见的是优先队列的思路。

优先对列是一个特殊的数据结构，它能保证在其中的所有数字都是有序的。
既然如此，我们可以维护一个优先队列，原始值为`[1]`，并对它进行n次如下操作:
```text
    1.在第n次的时候，从优先队列中取出一个最小的数字t
    2.t即为第n个超级丑数
    3.将t * primes[0], t * primes[1], .....等数字放入优先队列中。
    4.这样就能保证所有超级丑数都曾经被加入过该优先队列，而且因为我们是按照从小到大的顺序取的，所以第二条成立
```
按照这个思路，我们可以在$O(n * primes.length * log_2(n * primes.length))$的复杂度内计算出第n个超级丑数。

# Rust代码
```rust
use std::collections::*;
# struct Solution;
impl Solution {
    pub fn nth_super_ugly_number(mut n: i32, primes: Vec<i32>) -> i32 {
        let mut set = BTreeSet::new();
        set.insert(1);
        while set.len() > 0 {
            let first = *set.iter().next().unwrap();
            set.remove(&first);
            for &prime in &primes {
                if (first as i64) * (prime as i64) < (i32::MAX as i64) {
                    set.insert(first * prime);
                }
            }
            n -= 1;
            if n == 0 {
                return first;
            }
        }
        0
    }
}
```
# 进阶方法
## 思路
不难看出，超级丑数数列中的所有项都可以表示为 primes中的一个数和另一个在其之前出现的超级丑数的乘积。  
看懂了上面的那个方法之后，也可以看出，我们再每一步将一个超级丑数取出来，乘了一个primes中的数字，再放回到超级丑数的序列中作为候选。  
但这样会出现许多冗余和不必要的计算。  
比如超级丑数的数列过长，而我们需要的可能只是前几项。  
这促使我们找到一个新的方法来计算   
因此，我们设立一个新的数组pointer，其中的每一项和primes中的每一项都对应，且初值均为0。在这种情况下，我们也需要将丑数记录在一个名为dp的数列里  
在每一次循环中做如下的工作
```text
1.计算出当前最小候选超级丑数的值
2.具体的流程为求 dp[pointer[i]] * primes[i] 的最小值(i的取值范围就是primes的长度m)
3.该数即为下一个超级丑数 dp_nxt
4.对于所有项 dp[pointer[i]] * primes[i] == dp_nxt 的i，均使 pointer[i] 增加1
```
再理一遍思路，所有超级丑数都是由之前出现过的一个超级丑数乘上primes中的一个数可以获得的。而现在pointer指示的就是之前出现过的超级丑数的位置。  
可能出现重复的情况，比如2\*9和6\*3都会获得18，也就是说为什么对于所有符合最小值的项均需在pointer加1。  
按照这种遍历方式，可以从小到大完全遍历所有可能出现的超级丑数，并且省去了很多无效计算。  
按照这个思路，我们可以在O(n * primes.length)的时间内完成所有的计算。
```rust
use std::collections::*;
# struct Solution;
impl Solution {
    pub fn nth_super_ugly_number(n: i32, primes: Vec<i32>) -> i32 {
        let mut dp = vec![1];
        let n = n as usize;
        let m = primes.len();
        let mut pointer = vec![0; m];
        while dp.len() < n {
            let mut min_pos = 0;
            for i in 1..m {
                if dp[pointer[i]] * primes[i] < dp[pointer[min_pos]] * primes[min_pos] {
                    min_pos = i;
                }
            }
            let tmp = dp[pointer[min_pos]] * primes[min_pos];
            dp.push(tmp);
            for i in 0..m {
                if dp[pointer[i]] * primes[i] == tmp {
                    pointer[i] += 1;
                }
            }
        }
        println!("{:?}", dp);
        dp[n - 1]
    }
}
```