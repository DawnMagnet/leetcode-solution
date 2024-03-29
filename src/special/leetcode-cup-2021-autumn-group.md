# 2021 秋季力扣杯 - 战队赛复盘

## 写在前面

![](./leetcode-cup-2021秋战队赛.png)
![](./leetcode-cup-2021秋战队赛-1.png)
今年发挥还算挺不错的。以后再接再励！  
我 30 分钟写完了 2、4 两道题，队友一小时多写完了 1、3 两道题，然后就是啥都不会的几个小时。。。

争取以后不会出现这种情况。

## [第一题 开幕式焰火](https://leetcode-cn.com/problems/sZ59z6/)

### 1.1 题目

<div class="css-330z23" style="padding: 0px; margin: 13px 0px;"><p>「力扣挑战赛」开幕式开始了，空中绽放了一颗二叉树形的巨型焰火。<br>
给定一棵二叉树 <code>root</code> 代表焰火，节点值表示巨型焰火这一位置的颜色种类。请帮小扣计算巨型焰火有多少种不同的颜色。</p>
<p><strong>示例 1：</strong></p>
<blockquote>
<p>输入：<code>root = [1,3,2,1,null,2]</code></p>
<p>输出：<code>3</code></p>
<p>解释：焰火中有 3 个不同的颜色，值分别为 1、2、3</p>
</blockquote>
<p><strong>示例 2：</strong></p>
<blockquote>
<p>输入：<code>root = [3,3,3]</code></p>
<p>输出：<code>1</code></p>
<p>解释：焰火中仅出现 1 个颜色，值为 3</p>
</blockquote>
<p><strong>提示：</strong></p>
<ul>
<li><code>1 &lt;= 节点个数 &lt;= 1000</code></li>
<li><code>1 &lt;= Node.val &lt;= 1000</code></li>
</ul>
</div>

### 1.2 思路分析

数组 dp 存一下状态就行了，没有出现过就加一次。

### 1.3 代码

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool dp[1005];
    int count = 0;
    void deal(TreeNode * root) {
        if (!root) return ;
        if (!dp[root->val]) {
            count++;
            dp[root->val] = true;
        }
        deal(root->left);
        deal(root->right);
    }
    int numColor(TreeNode* root) {
        deal(root);
        return count;
    }
};
```

## [第二题 自行车炫技赛场](https://leetcode-cn.com/problems/kplEvH/)

### 2.1 题目

<div class="css-330z23" style="padding: 0px; margin: 13px 0px;"><p>「力扣挑战赛」中 <code>N*M</code> 大小的自行车炫技赛场的场地由一片连绵起伏的上下坡组成，场地的高度值记录于二维数组 <code>terrain</code> 中，场地的减速值记录于二维数组 <code>obstacle</code> 中。</p>
<ul>
<li>若选手骑着自行车从高度为 <code>h1</code> 且减速值为 <code>o1</code> 的位置到高度为 <code>h2</code> 且减速值为 <code>o2</code> 的相邻位置（上下左右四个方向），速度变化值为 <code>h1-h2-o2</code>（负值减速，正值增速）。</li>
</ul>
<p>选手初始位于坐标 <code>position</code> 处且初始速度为 1，请问选手可以刚好到其他哪些位置时速度依旧为 1。请以二维数组形式返回这些位置。若有多个位置则按行坐标升序排列，若有多个位置行坐标相同则按列坐标升序排列。</p>
<p><strong>注意：</strong> 骑行过程中速度不能为零或负值</p>
<p><strong>示例 1：</strong></p>
<blockquote>
<p>输入：<code>position = [0,0], terrain = [[0,0],[0,0]], obstacle = [[0,0],[0,0]]</code></p>
<p>输出：<code>[[0,1],[1,0],[1,1]]</code></p>
<p>解释：<br>
由于当前场地属于平地，根据上面的规则，选手从<code>[0,0]</code>的位置出发都能刚好在其他处的位置速度为 1。</p>
</blockquote>
<p><strong>示例 2：</strong></p>
<blockquote>
<p>输入：<code>position = [1,1], terrain = [[5,0],[0,6]], obstacle = [[0,6],[7,0]]</code></p>
<p>输出：<code>[[0,1]]</code></p>
<p>解释：<br>
选手从 <code>[1,1]</code> 处的位置出发，到 <code>[0,1]</code> 处的位置时恰好速度为 1。</p>
</blockquote>
<p><strong>提示：</strong></p>
<ul>
<li><code>n == terrain.length == obstacle.length</code></li>
<li><code>m == terrain[i].length == obstacle[i].length</code></li>
<li><code>1 &lt;= n &lt;= 100</code></li>
<li><code>1 &lt;= m &lt;= 100</code></li>
<li><code>0 &lt;= terrain[i][j], obstacle[i][j] &lt;= 100</code></li>
<li><code>position.length == 2</code></li>
<li><code>0 &lt;= position[0] &lt; n</code></li>
<li><code>0 &lt;= position[1] &lt; m</code></li>
</ul>
</div>

### 2.2 思路分析

这道题是一个比较基础的 dfs 思路。
可能会要使用记忆化的技术去重。
仔细读题后发现，自行车到达一个地方，并非一定会有相同的速度，也就是说，不同的路径到达一个地方，速度可能并不相同。
在这种情况下，我们必须得记录一下，如果两次到达同一个地方，具有相同的速度，我们就可以考虑不再继续。如果不去判断这一点，就会导致循环的出现，也就是示例 1 中出现的情况，如果我们不判断重复，一定会导致死循环。

所以总结一下，思路就是 dfs 加上记忆化去重（剪枝）。只有两次到达同一个地方并且具有相同的速度，才会是剪枝条件。

我的代码中主要分成了两块，一块是主函数，一块是 dfs，dfs 函数接受三个参数，也就是当前的 x，y 坐标和 speed 速度。
当`passed[x][y][speed]`为`true`时候，就说明之前以相同的速度遍历过相同的地方，而且无需再遍历一次。`res[x][y]`为`true`的时候说明该坐标是答案的一个候选坐标。接下来就是非常常规的往四个方向进行遍历。速度小于 0 就截断之类的基操。

主函数中主要是处理了一下输入输出的逻辑，存了一些全局变量，对输出的答案格式做了一个简单的操作，包括将 res 变成答案所需的形式。

### 2.3 C++代码

```cpp
using VI = vector<int>;
using VVI = vector<VI>;
const VI direc = {0, 1, 0, -1, 0};
class Solution {
public:
    VVI t, o;
    bool res[100][100] = {};
    bool passed[100][100][105] = {};
    int n, m;
    void dfs(int x, int y, int speed) {
        if (speed == 1) res[x][y] = true;
        if (speed < 1) return;
        if (passed[x][y][speed]) {
            return;
        }
        passed[x][y][speed] = true;
        for (int i = 0; i < 4; ++i) {
            int xt = x + direc[i];
            int yt = y + direc[i + 1];
            if (xt >= 0 && yt >= 0 && xt < n && yt < m)
                dfs(xt, yt, speed + t[x][y] - t[xt][yt] - o[xt][yt]);
        }
    }
    VVI bicycleYard(VI& p, VVI& terrain, VVI& obstacle) {
        t = terrain;
        o = obstacle;
        n = t.size();
        m = t[0].size();
        int x = p[0], y = p[1];
        dfs(x, y, 1);
        VVI res_v;
        res[x][y] = false;
        for (int i = 0; i < 100; ++i)
            for (int j = 0; j < 100; ++j)
                if (res[i][j])
                    res_v.push_back({i, j});
        return res_v;
    }
};
```

## [第三题 志愿者调配](https://leetcode-cn.com/problems/05ZEDJ/)

### 3.1 题目

<div class="css-330z23" style="padding: 0px; margin: 13px 0px;"><p>「力扣挑战赛」有 <code>n</code> 个比赛场馆（场馆编号从 <code>0</code> 开始），场馆之间的通道分布情况记录于二维数组 <code>edges</code> 中，<code>edges[i]= [x, y]</code> 表示第 <code>i</code> 条通道连接场馆 <code>x</code> 和场馆 <code>y</code>(即两个场馆相邻)。初始每个场馆中都有一定人数的志愿者（不同场馆人数可能不同），后续 <code>m</code> 天每天均会根据赛事热度进行志愿者人数调配。调配方案分为如下三种：</p>
<ol>
<li>将编号为 <code>idx</code> 的场馆内的志愿者人数减半；</li>
<li>将编号为 <code>idx</code> 的场馆相邻的场馆的志愿者人数都加上编号为 <code>idx</code> 的场馆的志愿者人数；</li>
<li>将编号为 <code>idx</code> 的场馆相邻的场馆的志愿者人数都减去编号为 <code>idx</code> 的场馆的志愿者人数。</li>
</ol>
<p>所有的调配信息记录于数组 <code>plans</code> 中，<code>plans[i] = [num,idx]</code> 表示第 <code>i</code> 天对编号 <code>idx</code> 的场馆执行了第 <code>num</code> 种调配方案。<br>
在比赛结束后对调配方案进行复盘时，不慎将第 <code>0</code> 个场馆的<strong>最终</strong>志愿者人数丢失，只保留了<strong>初始</strong>所有场馆的志愿者总人数 <code>totalNum</code> ，以及记录了第 <code>1 ~ n-1</code> 个场馆的<strong>最终</strong>志愿者人数的一维数组 <code>finalCnt</code>。请你根据现有的信息求出初始每个场馆的志愿者人数，并按场馆编号顺序返回志愿者人数列表。</p>
<p><strong>注意：</strong></p>
<ul>
<li>测试数据保证当某场馆进行第一种调配时，该场馆的志愿者人数一定为偶数；</li>
<li>测试数据保证当某场馆进行第三种调配时，该场馆的相邻场馆志愿者人数不为负数；</li>
<li>测试数据保证比赛开始时每个场馆的志愿者人数都不超过 <code>10^9</code>；</li>
<li>测试数据保证给定的场馆间的道路分布情况中不会出现自环、重边的情况。</li>
</ul>
<p><strong>示例 1：</strong></p>
<blockquote>
<p><img src="./leetcode-cup-1.png" alt="image.png" onerror="this.src='data:image/svg+xml,%3Csvg height=\'150\' viewBox=\'0 0 150 150\' width=\'150\' xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cpath d=\'m2465 2286.42347-18.95363-18.92555-50.0112 43.79935-24.62708-24.5906-33.41155 24.5906-22.99654-17.22567v-73.0716c0-2.20914 1.79086-4 4-4h142c2.20914 0 4 1.79086 4 4zm-122-25.59081c5.52285 0 10-4.47052 10-9.98518 0-5.51467-4.47715-9.98519-10-9.98519s-10 4.47052-10 9.98519c0 5.51466 4.47715 9.98518 10 9.98518zm122 40.89296v61.27438c0 2.20914-1.79086 4-4 4h-142c-2.20914 0-4-1.79086-4-4v-53.62625l22.99654 17.22567 33.41155-24.5906 24.62708 24.5906 50.0112-43.79935z\' fill=\'%23eee\' fill-rule=\'evenodd\' transform=\'translate(-2315 -2217)\'/%3E%3C/svg%3E'; "><br>
输入：<br>
<code>finalCnt = [1,16], totalNum = 21, edges = [[0,1],[1,2]], plans = [[2,1],[1,0],[3,0]]</code></p>
<p>输出：<code>[5,7,9]</code></p>
<p>解释：<br>
<img src="./leetcode-cup-2.png" alt="image.png" height="200" onerror="this.src='data:image/svg+xml,%3Csvg height=\'150\' viewBox=\'0 0 150 150\' width=\'150\' xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cpath d=\'m2465 2286.42347-18.95363-18.92555-50.0112 43.79935-24.62708-24.5906-33.41155 24.5906-22.99654-17.22567v-73.0716c0-2.20914 1.79086-4 4-4h142c2.20914 0 4 1.79086 4 4zm-122-25.59081c5.52285 0 10-4.47052 10-9.98518 0-5.51467-4.47715-9.98519-10-9.98519s-10 4.47052-10 9.98519c0 5.51466 4.47715 9.98518 10 9.98518zm122 40.89296v61.27438c0 2.20914-1.79086 4-4 4h-142c-2.20914 0-4-1.79086-4-4v-53.62625l22.99654 17.22567 33.41155-24.5906 24.62708 24.5906 50.0112-43.79935z\' fill=\'%23eee\' fill-rule=\'evenodd\' transform=\'translate(-2315 -2217)\'/%3E%3C/svg%3E'; "></p>
</blockquote>
<p><strong>示例 2 ：</strong></p>
<blockquote>
<p>输入：<br>
<code>finalCnt = [4,13,4,3,8], totalNum = 54, edges = [[0,3],[1,3],[4,3],[2,3],[2,5]], plans = [[1,1],[3,3],[2,5],[1,0]]</code></p>
<p>输出：<code>[10,16,9,4,7,8]</code></p>
</blockquote>
<p><strong>提示：</strong></p>
<ul>
<li><code>2 &lt;= n &lt;= 5*10^4</code></li>
<li><code>1 &lt;= edges.length &lt;= min((n * (n - 1)) / 2, 5*10^4)</code></li>
<li><code>0 &lt;= edges[i][0], edges[i][1] &lt; n</code></li>
<li><code>1 &lt;= plans.length &lt;= 10</code></li>
<li><code>1 &lt;= plans[i][0] &lt;=3</code></li>
<li><code>0 &lt;= plans[i][1] &lt; n</code></li>
<li><code>finalCnt.length = n-1</code></li>
<li><code>0 &lt;= finalCnt[i] &lt; 10^9</code></li>
<li><code>0 &lt;= totalNum &lt; 5*10^13</code></li>
</ul>
</div>

### 3.2 思路分析

我们只有一个值不知道，就是当前（最后时刻）第 0 号位的人数。
通过观察题目不难得出，三个操作都是线性操作，而且我们准确地知道每一步的操作，也就是说，只要知道知道了最后一个时刻的第 0 号位的人数，我们就可以严丝合缝地将结果递推到第一步。并且，在此时，第一步的总和应当严格等于`totalNum`。

既然如此，我们不妨设一个变量 x，作为最后时刻第 0 号位的人数。逆推来完成最终的推理，推理到第一步之后，每一个场馆的人数都应该是一个关于变量 x 的一次函数，我们将其求和之后仍然是一个一次函数，这个一次函数最终等于 `totalNum` ，代入就可以求得 x，代入每个场馆的表达式中即可获得每个场馆在第一步时的人数。

在具体代码中，设置两个数组 `x_param` 和 `c_param` ，分别代表指定场馆一次函数中的 x 系数项和常数项。最终递推回第一步，求得 `x_param_sum` 与 `c_param_sum` 。求解 x 的方程为:

$\sum^{n}_{i=1}{x_{param}[i]} * x + \sum^{n}_{i=1}{c_{param}[i]} = totalNum$  
简单变换后得到:

$x = \frac{(totalNum - \sum^{n}_{i=1}{c_{param}[i]})}{\sum^{n}_{i=1}{x_{param}[i]}}$

最后代入到表达式中即可完成计算。

### 3.3 C++代码

```cpp
using VI = vector<int>;
using VVI = vector<VI>;
using ll = long long;
class Solution {
public:
    VI volunteerDeployment(VI& finalCnt, ll totalNum, VVI& edges, VVI& plans) {
        VI m[50005];
        int n = finalCnt.size() + 1;
        // x系数和常数
        int x_param[50005] = {}, c_param[50005] = {};
        for (auto & edge : edges) {
            m[edge[0]].push_back(edge[1]);
            m[edge[1]].push_back(edge[0]);
        }
        x_param[0] = 1;
        for (int i = 0; i < n - 1; ++i)
            c_param[i + 1] = finalCnt[i];
        while (plans.size()) {
            int kind = plans.back()[0];
            int place = plans.back()[1];
            plans.pop_back();
            if (kind == 1) {
                x_param[place] *= 2;
                c_param[place] *= 2;
            } else if (kind == 2) {
                for (auto & nxt : m[place]) {
                    x_param[nxt] -= x_param[place];
                    c_param[nxt] -= c_param[place];
                }
            } else {
                for (auto & nxt : m[place]) {
                    x_param[nxt] += x_param[place];
                    c_param[nxt] += c_param[place];
                }
            }
        }
        ll x_param_sum = 0, c_param_sum = 0;
        for (int i = 0; i < n; ++i) {
            x_param_sum += x_param[i];
            c_param_sum += c_param[i];
        }
        // 方程: x_param_sum * x + c_param_sum = totalNum
        int x = (totalNum - c_param_sum) / x_param_sum;
        vector<int> res(n);
        for (int i = 0; i < n; ++i)
            res[i] = x_param[i] * x + c_param[i];
        return res;
    }
};
```

## [第四题 入场安检](https://leetcode-cn.com/problems/oPs9Bm/)

### 4.1 题目

<div class="css-330z23" style="padding: 0px; margin: 13px 0px;"><p>「力扣挑战赛」 的入场仪式马上就要开始了，由于安保工作的需要，设置了可容纳人数总和为 <code>M</code> 的 <code>N</code> 个安检室，<code>capacities[i]</code> 记录第 <code>i</code> 个安检室可容纳人数。安检室拥有两种类型：</p>
<ul>
<li>先进先出：在安检室中的所有观众中，最早进入安检室的观众最先离开</li>
<li>后进先出：在安检室中的所有观众中，最晚进入安检室的观众最先离开</li>
</ul>
<p align="center"><img src="https://pic.leetcode-cn.com/1628843202-cdFPSt-c24754f1a5ff56989340ba5004dc5eda.gif" alt="c24754f1a5ff56989340ba5004dc5eda.gif"></p>
<p>恰好 <code>M+1</code> 位入场的观众（编号从 0 开始）需要排队<strong>依次</strong>入场安检， 入场安检的规则如下：</p>
<ul>
<li>观众需要先进入编号 <code>0</code> 的安检室</li>
<li>当观众将进入编号 <code>i</code> 的安检室时（<code>0 &lt;= i &lt; N</code>)，
<ul>
<li>若安检室未到达可容纳人数上限，该观众可直接进入；</li>
<li>若安检室已到达可容纳人数上限，在该观众进入安检室之前需根据当前安检室类型选择一位观众离开后才能进入；</li>
</ul>
</li>
<li>当观众离开编号 <code>i</code> 的安检室时 （<code>0 &lt;= i &lt; N-1</code>)，将进入编号 <code>i+1</code> 的安检室接受安检。</li>
</ul>
<p>若可以任意设定每个安检室的类型，请问有多少种设定安检室类型的方案可以使得编号 <code>k</code> 的观众第一个通过最后一个安检室入场。</p>
<p><strong>注意：</strong></p>
<ul>
<li>观众不可主动离开安检室，只有当安检室容纳人数达到上限，且又有新观众需要进入时，才可根据安检室的类型选择一位观众离开；</li>
<li>由于方案数可能过大，请将答案对 <code>1000000007</code> 取模后返回。</li>
</ul>
<p><strong>示例 1：</strong></p>
<blockquote>
<p>输入：<code>capacities = [2,2,3], k = 2</code></p>
<p>输出：<code>2</code><br>
解释：<br>
存在两种设定的 <code>2</code> 种方案：</p>
<ul>
<li>方案 1：将编号为 <code>0</code> 、<code>1</code> 的实验室设置为 <strong>后进先出</strong> 的类型，编号为 <code>2</code> 的实验室设置为 <strong>先进先出</strong> 的类型；</li>
<li>方案 2：将编号为 <code>0</code> 、<code>1</code> 的实验室设置为 <strong>先进先出</strong> 的类型，编号为 <code>2</code> 的实验室设置为 <strong>后进先出</strong> 的类型。</li>
</ul>
<p>以下是方案 1 的示意图：<br>
<img src="https://pic.leetcode-cn.com/1628841618-bFKsnt-c60e38199a225ad62f13b954872edf9b.gif" alt="c60e38199a225ad62f13b954872edf9b.gif"></p>
</blockquote>
<p><strong>示例 2：</strong></p>
<blockquote>
<p>输入：<code>capacities = [3,3], k = 3</code></p>
<p>输出：<code>0</code></p>
</blockquote>
<p><strong>示例 3：</strong></p>
<blockquote>
<p>输入：<code>capacities = [4,3,2,2], k = 6</code></p>
<p>输出：<code>2</code></p>
</blockquote>
<p><strong>提示:</strong></p>
<ul>
<li><code>1 &lt;= capacities.length &lt;= 200</code></li>
<li><code>1 &lt;= capacities[i] &lt;= 200</code></li>
<li><code>0 &lt;= k &lt;= sum(capacities)</code></li>
</ul>
</div>

### 4.2 思路分析

本题注意观察题目即可发现，先进先出对应的数据结构为队列，后进先出对应的数据结构为栈。
而注意看第二个gif，我们发现，当一个容器（实验室，我们在此统称为容器）为队列时，第一个进入的第一个出队列，也就是说，一个队列对于改变流程中的第一个人没任何影响。对比着来看栈，我们发现，一个长度为2的栈必须先填充1个元素，这一个元素就相当于固定在此处，没法移动，也就是说，对于流程中的第一个人，一个长度为`c`的栈能够拦截`c-1`个人。

那么就很简单了。因为我们想要让第`k`个人达到对首，我们必须使用栈来拦截前`k`个人。

所以我们把这道题翻译成一个我们喜闻乐见的形式：
```markdown
有`N`个硬币，每个的金额都在`cap`数组中给出（需要一个减1操作）。我们从前往后选，求最终金额为`k`的方案数。
```
是不是一下就简单了呢！

最终的做法就是一个非常简单的dp。因为一个硬币只能用一次，所以要控制dp的方向。

### 4.3 C++代码
```cpp
const int md = 1000000007;
class Solution {
public:
    int securityCheck(vector<int>& cap, int k) {
        for (auto & c : cap) c--;
        int sum = accumulate(cap.begin(), cap.end(), 0);
        if (sum < k) return 0;
        int dp[40005] = {1};
        for (auto & c : cap) {
            for (int i = k - c; i >= 0; --i) {
                (dp[i + c] += dp[i]) %= md;
            }
        }
        return dp[k];
    }
};
```