# list查找元素

## 访问元素方法

仅列出常用访问元素的方法，其他方法请参考[cppreference](https://en.cppreference.com/w/cpp/container/list)。

* front和back
* 迭代器

**1.front和back访问前后元素**

list成员函数声明:

```c++
reference front();
reference back();
```

* front()：返回list双向链表表头元素的引用；
* back()：返回list双向链表表位元素的引用；

代码示例：

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    list<int> nums = {8, 13, 18};

    cout << nums.back() << " ";
    cout << nums.front() << endl;

    return 0;
}
```

代码输出：

```c++
18 8
```

**2.迭代器方式访问元素**

list成员函数声明：

```c++
iterator begin() noexcept;
iterator end() noexcept;

reverse_iterator rbegin() noexcept;
reverse_iterator rend() noexcept;
```

各迭代器指代位置如下图（来自[cppreference](https://en.cppreference.com/w/cpp/container/list/rbegin)）：

![](../../../images/stl/range-rbegin-rend.svg)

* list**不支持**随机访问容器的迭代器，但由于list为**双向链表**，迭代器支持向前/向后累加，即--或++运算
* 访问迭代器指代的元素，需要解引用

代码示例：

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    list<int> nums = {1, 3, 9, 13, 19, 98};

    auto iter = nums.begin();
    cout << *iter << "->";
    cout << *(++iter) << endl;

    return 0;
}
```

代码输出：

```c++
1->3
```

**3.访问所有元素**

*a.迭代器方式*

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    list<int> nums = {1, 3, 9, 13, 19, 98};

    auto iter = nums.begin();
    for (; iter != nums.end(); ++iter) {
        cout << *iter << " ";
    }
    cout << endl;

    return 0;
}
```

代码输出：

```c++
1 3 9 13 19 98
```

*b.范围for方式*

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    list<int> nums = {1, 3, 9, 13, 19, 98};

    for (auto val : nums) {
        cout << val << " ";
    }
    cout << endl;

    return 0;
}
```

代码输出：

```c++
1 3 9 13 19 98
```

*c.范围for语句访问二维链表*

访问二维链表时，对每一行的提取，通过**引用**的方式，提高运行效率。

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    list<list<int>> nums = {
        {1, 2, 3},
        {4, 5}
    };

    for (auto& row : nums) {
        for (auto val : row) {
            cout << val << " ";
        }
        cout << endl;
    }

    return 0;
}
```

代码输出：

```c++
1 2 3
4 5
```

说明：

* row的数据类型为`list<int>&`；
* row采用引用的方式，减少临时对象的创建，及内存数据的拷贝，从而提高运行效率。

## 查找元素

* list中无序元素

   * 若仅查找一次，遍历list中所有元素即可；

   * 若需多次查找，先利用list中的sort排序方法对list中的元素排序，再按照有序的方法进行查找。

* list中是有序元素，只需要使用二分查找法快速查找元素。
