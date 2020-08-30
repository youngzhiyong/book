# for的死循环

## 问题

打印输出10次hello C/C++，真的是这样吗？

```c++
#include <iostream>
using namespace std;
int main()
{
    for (unsigned int i = 10; i >= 0; --i) {
        cout << "hello C/C++" << endl;
    }

    return 0;
}
```

## 答案

无限次数打印hello C/C++

## 原因分析

变量i的类型为无符号型，i一直都是＞0的值，i>=0条件将永久成立。

**修改方法**

删除代码中unsigned，使变量i成为有符号类型。
