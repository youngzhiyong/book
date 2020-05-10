# array创建对象

注：无明确定义的构造函数、析构函数和赋值操作符重载

**1.定义array对象，未初始化**

没有明确的初始化，array对象中存储的各元素值均为**随机值**。

```c++
#include <array>
#include <iostream>

using namespace std;

int main()
{
    array<int, 3> a;
    for (auto val : a) {
        cout << val << " ";
    }
    cout << endl;

    return 0;
}
```

代码输出：

```c++
65535 3 0
```

**2.使用聚合初始化方式**

聚合方式初始化相应位置的值即为给出的值。其他位置的值调用T类型的默认构造函数(无参构造函数)；若T为一般数据类型，则初始化为0。

聚合初始化：无初始化数据
```c++
#include <array>
#include <iostream>

using namespace std;

int main()
{
    array<int, 3> a {};     // 聚合方式初始化
    for (auto val : a) {
        cout << val << " ";
    }
    cout << endl;

    return 0;
}
```

代码输出：

```c++
0 0 0
```
聚合初始化方式：部分初始化数据

```c++
#include <array>
#include <iostream>

using namespace std;

int main()
{
    array<int, 3> a {1};
    // array<int, 3> a = {1};	// 等价形式
    for (auto val : a) {
        cout << val << " ";
    }
    cout << endl;

    return 0;
}
```

代码输出：

```c++
1 0 0
```

**3.定义array对象后，在使用fill填充**

```c++
void fill( const T& value ); 
constexpr void fill( const T& value );
```

使用value值填充array中的所有元素。

```c++
#include <array>
#include <iostream>

using namespace std;

int main()
{
    array<int, 3> a;
    a.fill(10);
    for (auto val : a) {
        cout << val << " ";
    }
    cout << endl;

    return 0;
}
```

代码输出：

```c++
10 10 10
```
