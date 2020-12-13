# set丧失唯一性

## 问题

对一组数按照从大到小的顺序排序，且排序后的数须具有唯一性，请给出下列代码的输出结果？为什么？

```c++
#include <vector>
#include <set>
#include <iostream>

using namespace std;

int main()
{
    vector<int> nums = {8, 9, 10, 23, 23, 19, 20, 10};
    set<int, greater_equal<int>> uniq_nums(nums.begin(), nums.end());

    for (int num : uniq_nums) {
        cout << num << " ";
    }
   
    return 0;
}
```

## 答案

代码输出：

```c++
23 23 20 19 10 10 9 8
```

set具有唯一性，为什么代码输出结果中包含了重复的23和10？

在[cppreference](https://en.cppreference.com/w/cpp/container/set)中有下列的一句话：

<p>
std::set is an associative container that contains a sorted set of unique objects of type Key. Sorting is done using the key comparison function <a href="https://en.cppreference.com/w/cpp/named_req/Compare">Compare</a>.
</p>

其中，[Compare](https://en.cppreference.com/w/cpp/named_req/Compare)函数必须满足严格弱排序：

* for all a, comp(a,a)==false
* if comp(a,b)==true then comp(b,a)==false
* if comp(a,b)==true and comp(b,c)==true then comp(a,c)==true
* equiv(a, b), an expression equivalent to !comp(a, b) && !comp(b, a)

以一个更简单的例子说明：

```c++
#include <set>
using namespace std;

int main()
{
    int a = 10;
    int b = 10;
    set<int, greater<int>> uniq_nums;

    uniq_nums.insert(a);
    uniq_nums.insert(b);
   
    return 0;
}
```

**1. 若Compare函数为<a href="https://en.cppreference.com/w/cpp/utility/functional/greater">greater</a>**

```c++
// Defined in header <functional>
template< class T >
struct greater;

// Possible implementation
constexpr bool operator()(const T &lhs, const T &rhs) const 
{
    return lhs > rhs;
}
```

a. 向`uniq_nums`中`insert`变量a，此时集合为空，不用判定与其他元素的相等性；
b. 向`uniq_nums`中`insert`变量b，此时集合中存在变量a的值10，需要与之判定相等性：

   * 如上提到的判定相等性，即判定`!comp(a, b) && !comp(b, a)`
   * !greater(a, b)，返回true
   * !greater(b, a)，返回true
   * !greater(a, b) && !greater(b, a)，返回true

因此，新插入的b与集合中的值存在相等性，不能将b插入到集合中。**从而保证了集中值得唯一性。**


**2. 若Compare函数为<a href="https://en.cppreference.com/w/cpp/utility/functional/greater_equal">greater_equal</a>**

```c++
// Defined in header <functional>
template< class T >
struct greater_equal;

// Possible implementation
constexpr bool operator()(const T &lhs, const T &rhs) const 
{
    return lhs >= rhs;
}
```

与上述`Compare`函数为`greater`类似，在插入b时判定与集合中元素的相等性：

   * !greater_equal(a, b)，返回false
   * !greater_equal(b, a)，返回false
   * !greater_equal(a, b) && !greater_equal(b, a)，返回false

因此，判定为新插入的b与集合中的元素a不相等，可以将b的值插入到集合中。**从而导致set集合中值重复，丧失唯一性。**


## 规范

在C++中，涉及`Compare`比较的函数，保证用于比较的函数，必须**满足严格弱排序**。
