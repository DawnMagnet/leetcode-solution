# No.284 窥探迭代器
<p>请你设计一个迭代器，除了支持 <code>hasNext</code> 和 <code>next</code> 操作外，还支持 <code>peek</code> 操作。</p>

<p>实现 <code>PeekingIterator</code> 类：</p>

<div class="original__bRMd">
<div>
<ul>
	<li><code>PeekingIterator(int[] nums)</code> 使用指定整数数组 <code>nums</code> 初始化迭代器。</li>
	<li><code>int next()</code> 返回数组中的下一个元素，并将指针移动到下个元素处。</li>
	<li><code>bool hasNext()</code> 如果数组中存在下一个元素，返回 <code>true</code> ；否则，返回 <code>false</code> 。</li>
	<li><code>int peek()</code> 返回数组中的下一个元素，但 <strong>不</strong> 移动指针。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>
["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
[[[1, 2, 3]], [], [], [], [], []]
<strong>输出：</strong>
[null, 1, 2, 2, 3, false]

<strong>解释：</strong>
PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [<em><strong>1</strong></em>,2,3]
peekingIterator.next();    // 返回 1 ，指针移动到下一个元素 [1,<em><strong>2</strong></em>,3]
peekingIterator.peek();    // 返回 2 ，指针未发生移动 [1,<em><strong>2</strong></em>,3]
peekingIterator.next();    // 返回 2 ，指针移动到下一个元素 [1,2,<em><strong>3</strong></em>]
peekingIterator.next();    // 返回 3 ，指针移动到下一个元素 [1,2,3]
peekingIterator.hasNext(); // 返回 False
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li>对 <code>next</code> 和 <code>peek</code> 的调用均有效</li>
	<li><code>next</code>、<code>hasNext</code> 和 <code>peek </code>最多调用&nbsp; <code>1000</code> 次</li>
</ul>
</div>
</div>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你将如何拓展你的设计？使之变得通用化，从而适应所有的类型，而不只是整数型？</p>

# 思路分析

本题的难点主要在于，本来原题给我们提供的数据结构`Iterator`只提供了以下两个接口：
- `int next()`
- `bool hasNext()`

而我们要实现的数据结构要在其基础上再实现一个`int peek()`。

这里就会出现一个问题，也就是每次调用`next()`无疑都会使得迭代器向后移动一个位置，但是每次调用`peek()`却不会。

其实很好提出一个解决方法，就是在每次调用`next()`的时候拿一个数字存一下，作为下次调用`peek()`时候的返回值。但这样会出现问题。

观察一下示例1，可以发现，在调用`peek()`时，指针不发生移动，但是确确实实地，我们获取到了下一个变量的值。这题的难点就在于，我们期望能够在获取下一个元素的值的时候不移动指针。但`next()`一定会移动指针。

思路可以这样：先用一个变量一直存住下一个元素的值，如果遇到了`peek()`就返回这个预先存的值，如果遇到`next()`也返回这个预先存的值并且更新预先存的值为下一个。

# C++ 代码
```cpp
class PeekingIterator : public Iterator {
public:
    PeekingIterator(const vector<int>& nums) : Iterator(nums) {
        flag = Iterator::hasNext();
        if (flag) {
            nextElement = Iterator::next();
        }
    }
    
    int peek() {
        return nextElement;
    }
    
    int next() {
        int ret = nextElement;
        flag = Iterator::hasNext();
        if (flag) {
            nextElement = Iterator::next();
        }
        return ret;
    }
    
    bool hasNext() const {
        return flag;
    }
private:
    int nextElement;
    bool flag;
};
```
