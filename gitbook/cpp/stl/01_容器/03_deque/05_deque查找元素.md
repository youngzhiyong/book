# deque查找元素

## 访问元素方法

仅列出常用访问元素的方法，其他方法请参考[cppreference](https://en.cppreference.com/w/cpp/container/deque)。

* 角标
* front和back
* 迭代器

**1.角标方式支持随机访问**

deque成员函数声明

```c++
reference operator[](size_type pos);
```

pos超出deque对象支持的角标范围，将会出现段错误。因此，角标访问时，应注意检查pos的值。

代码示例：

```c++
#include <deque>
#include <iostream>

using namespace std;

int main()
{
    deque<int> nums = {8, 13, 18};

    cout << nums[2] << " ";
    cout << nums[0] << endl;

    return 0;
}
```

代码输出：

```c++
18 8
```

**2.front和back访问前后元素**

deque成员函数声明:

```c++
reference front();
reference back();
```

* front()：返回deque最靠前的元素的引用；
* back()：返回deque最靠后的元素的引用；

注：*如果deque对象存储元素为0，front和back为未定义行为*。

代码示例：

```c++
#include <deque>
#include <iostream>

using namespace std;

int main()
{
    deque<int> nums = {8, 13, 18};

    cout << nums.back() << " ";
    cout << nums.front() << endl;

    return 0;
}
```

代码输出：

```c++
18 8
```

**3.迭代器方式访问元素**

deque成员函数声明：

```c++
iterator begin() noexcept;
iterator end() noexcept;

reverse_iterator rbegin() noexcept;
reverse_iterator rend() noexcept;
```

各迭代器指代位置如下图（来自[cppreference](https://en.cppreference.com/w/cpp/container/deque/rbegin)）：

![](../../../images/stl/range-rbegin-rend.svg)

* 支持随机访问容器的迭代器，支持迭代器加减运算
* deque的存储结构的特殊性，随机访问需要相关的计算才能得到目标位置，相对于vector的随机访问，deque效率较低
* 访问迭代器指代的元素，需要解引用

代码示例：

```c++
#include <deque>
#include <iostream>

using namespace std;

int main()
{
    deque<int> nums = {1, 3, 9, 13, 19, 98};

    auto iter = nums.begin();
    cout << *iter << "->" << *(iter + 3) << endl;

    return 0;
}
```

代码输出：

```c++
1->13
```

**4.访问所有元素**

*a.角标方式*

```c++
#include <deque>
#include <iostream>

using namespace std;

int main()
{
    deque<int> nums = {1, 3, 9, 13, 19, 98};

    for (int i = 0; i < nums.size(); ++i) {
        cout << nums[i] << " ";
    }
    cout << endl;

    return 0;
}
```

代码输出：

```c++
1 3 9 13 19 98
```

*b.迭代器方式*

```c++
#include <deque>
#include <iostream>

using namespace std;

int main()
{
    deque<int> nums = {1, 3, 9, 13, 19, 98};

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

*c.范围for方式*

```c++
#include <deque>
#include <iostream>

using namespace std;

int main()
{
    deque<int> nums = {1, 3, 9, 13, 19, 98};

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

*d.范围for语句访问二维数组*

访问二维数组时，对每一行的提取，通过**引用**的方式，提高运行效率。

```c++
#include <deque>
#include <iostream>

using namespace std;

int main()
{
    deque<deque<int>> nums = {
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

* row的数据类型为`deque<int>&`；
* row采用引用的方式，减少临时对象的创建，及内存数据的拷贝，从而提高运行效率。

## 查找元素

* deque中是无序元素，需要遍历所有元素，以此判断是否为需要查找的元素；
* deque中是有序元素，只需要使用二分查找法快速查找元素(此处不作介绍)。

deque中无序元素查找，在上述访问所有元素小节中，添加判定与目标值的一致性即可。
