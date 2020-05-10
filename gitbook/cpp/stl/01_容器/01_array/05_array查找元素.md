# array查找元素

## 访问元素方法

仅列出常用访问元素的方法，其他方法请参考[cppreference](https://en.cppreference.com/w/cpp/container/array)。

**1.角标方式支持随机访问**

array成员函数声明

```c++
reference operator[]( size_type pos );
```

pos超出array对象支持的角标范围，将会出现段错误。因此，角标访问时，应注意检查pos的值。

代码示例：

```c++
#include <array>
#include <iostream>

using namespace std;

int main()
{
    constexpr int len = 3;
    array<int, len> a = {8, 13, 18};	// 常量表达式方式

    cout << a[2] << " ";
    cout << a[0] << endl;

    return 0;
}
```

代码输出：

```c++
18 8
```

**2.front和back访问前后元素**

array成员函数声明:

```c++
reference front();
reference back();
```

* front()：返回array连续存储的最靠前的元素的引用；
* back()：返回array连续存储的最靠后的元素的引用；

注：*如果array对象存储元素为0，front和back为未定义行为*。

代码示例：

```c++
#include <array>
#include <iostream>

using namespace std;

int main()
{
    constexpr int len = 3;
    array<int, len> a = {8, 13, 18};	// 常量表达式方式

    cout << a.back() << " ";
    cout << a.front() << endl;

    return 0;
}
```

代码输出：

```c++
18 8
```

**3.迭代器方式访问元素**

array成员函数声明：

```c++
iterator begin() noexcept;
iterator end() noexcept;

reverse_iterator rbegin() noexcept;
reverse_iterator rend() noexcept;
```

各迭代器指代位置如下图（来自[cppreference](https://en.cppreference.com/w/cpp/container/array/rbegin)）：

![](../../../images/stl/range-rbegin-rend.svg)

* 支持**随机访问**容器的迭代器，支持迭代器加减运算
* 访问迭代器指代的元素，需要解引用

代码示例：

```c++
#include <array>
#include <iostream>

using namespace std;

int main()
{
    constexpr int len = 6;
    array<int, len> a = {1, 3, 9, 13, 19, 98};

    auto iter = a.begin();
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
#include <array>
#include <iostream>

using namespace std;

int main()
{
    constexpr int len = 6;
    array<int, len> a = {1, 3, 9, 13, 19, 98};

    for (int i = 0; i < len; ++i) {
        cout << a[i] << " ";
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
#include <array>
#include <iostream>

using namespace std;

int main()
{
    constexpr int len = 6;
    array<int, len> a = {1, 3, 9, 13, 19, 98};

    auto iter = a.begin();
    for (; iter != a.end(); ++iter) {
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
#include <array>
#include <iostream>

using namespace std;

int main()
{
    constexpr int len = 6;
    array<int, len> a = {1, 3, 9, 13, 19, 98};

    for (auto val : a) {
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
