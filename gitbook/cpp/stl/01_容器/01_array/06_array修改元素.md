# array修改元素

修改元素，主要使用如下几种方法：

* 角标方式
* front和back方式
* 迭代器方式
  
上述方式的函数声明，请查看[array查找元素](./05_array查找元素.md)章节。

## 角标方式

```c++
#include <array>
#include <iostream>

using namespace std;

int main()
{
    constexpr int len = 6;
    array<int, len> a = {1, 3, 9, 13, 19, 98};

    cout << a[0] << "->";
    a[0] = 32;
    cout << a[0] << endl;

    return 0;
}
```

代码输出：

```c++
1->32
```

## front和back方式

仅能修改最前和最后的元素。

```c++
#include <array>
#include <iostream>

using namespace std;

int main()
{
    constexpr int len = 6;
    array<int, len> a = {1, 3, 9, 13, 19, 98};

    cout << a.front() << "->";
    a.front() = 32;
    cout << a.front() << endl;

    return 0;
}
```

代码输出：

```c++
1->32
```

## 迭代器方式

```c++
#include <array>
#include <iostream>

using namespace std;

int main()
{
    constexpr int len = 6;
    array<int, len> a = {1, 3, 9, 13, 19, 98};

    auto iter = a.begin();

    cout << *iter << "->";
    *iter = 32;
    cout << *iter << endl; 

    return 0;
}
```

代码输出：

```c++
1->32
```
