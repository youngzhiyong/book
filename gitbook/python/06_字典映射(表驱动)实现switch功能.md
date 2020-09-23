# 字典映射(表驱动)实现switch功能

本文介绍python中可以使用字典的方式实现和C/C++的表驱动相同的功能，并且代码更加简洁。

c/c++的表驱动代码:

```c++
#include <map>
#include <iostream>

using namespace std;

void foo1(int key)
{
    cout << "foo1:" << key  << endl;
}

void foo2(int key)
{
    cout << "foo2:" << key << endl;
}

int main()
{
    // 表驱动
    map<int, void (*)(int)> callTbl = {
        make_pair(1, foo1),
        make_pair(2, foo2)
    };

    for (auto& item : callTbl) {
        item.second(item.first);
    }

    return 0;
}
```

python字典驱动的方式：

```python
#coding=utf-8

def foo1(key):
    print(f"{foo1.__name__}:{key}")

def foo2(key):
    print(f"{foo2.__name__}:{key}")

def main():
    # 表驱动
    callTbl = {
        1: foo1,
        2: foo2
    }

    for key, fun in callTbl.items():
        fun(key)

if __name__ == "__main__":
    main()
```

以上两段代码运行结果均为：

```python
foo1:1
foo2:2
```
