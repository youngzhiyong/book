# list修改元素

修改元素，主要使用如下几种方法：

* front和back方式
* 迭代器方式
  
上述方式的函数声明，请查看[list查找元素](./05_list查找元素.md)章节。

## front和back方式

仅能修改最前和最后的元素。

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    list<int> nums = {1, 3, 9, 13, 19, 98};

    cout << nums.front() << "->";
    nums.front() = 32;
    cout << nums.front() << endl;

    return 0;
}
```

代码输出：

```c++
1->32
```

## 迭代器方式

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    list<int> nums = {1, 3, 9, 13, 19, 98};

    auto iter = nums.begin();

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
