# list其他操作

## 容量

**1. 获取存储元素个数信息**

```c++
bool empty() const;
size_type size() const;
size_type max_size() const;
```

* `empty`:判定list容器中是否为空。
* `size`:获取容器中当前**元素个数**。
* `max_size`:获取容器能存放当前类型元素最大个数，取决于系统和库代码的实现。

```c++
#include <list>
#include <iostream>

using namespace std;

template<typename T>
void Show(const list<T>& nums)
{
    cout.flags(ios::boolalpha);
    cout << "empty:" << nums.empty() << endl;
    cout << "size:" << nums.size() << endl;
    cout << "sizeof(T):" << sizeof(T) << " max_size:" << nums.max_size() << endl;
}

int main()
{
    list<int> intNums = {
        1, 2, 3, 4
    };

    cout << "Type=int info as follows:" << endl;
    Show(intNums);
    cout << endl;

    list<long long> llNums = {
        1, 2, 3
    };

    llNums.push_back(4);

    cout << "Type=long long info as follows:" << endl;
    Show(llNums);
    cout << endl;

    return 0;
}
```

代码输出：

```c++
Type=int info as follows:
empty:false
size:4
sizeof(T):4 max_size:357913941

Type=long long info as follows:
empty:false
size:4
sizeof(T):8 max_size:268435455
```

**2. 伸缩容器存储元素空间**

```c++
void resize(size_type count);
void resize(size_type count, const value_type& value);
```

* `count < size()`：缩减容器大小为count个有效元素；
* `count > size()`：使用value默认值填充新增至count个元素，原数据值保持不变。

*a.缩减容器元素个数*

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    const int count = 100;
    list<int> nums;
    for (int i = 0; i < count; ++i) {
        nums.push_back(i);
    }

    cout << nums.size() << endl;
    nums.resize(5);
    cout << nums.size() << endl;

    return 0;
}
```

代码输出：

```c++
100
5
```

*b. 增大容器元素个数*

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    const int count = 2;
    list<int> nums;
    for (int i = 0; i < count; ++i) {
        nums.push_back(i);
    }

    nums.resize(count * 2);

    for (auto val : nums) {
        cout << val << " ";
    }

    return 0;
}
```

代码输出：

```c++
0 1 0 0
```

## list比较

list容器与容器之间可以直接比较大小，无需再次实现list容器间的比较函数。

```c++
template<class T, class Alloc>
bool operator==(const std::list<T,Alloc>& lhs,
                 const std::list<T,Alloc>& rhs);
template<class T, class Alloc>
constexpr bool operator==(const std::list<T,Alloc>& lhs,
                           const std::list<T,Alloc>& rhs);
template<class T, class Alloc>
bool operator!=(const std::list<T,Alloc>& lhs,
                 const std::list<T,Alloc>& rhs);
template<class T, class Alloc>
bool operator<(const std::list<T,Alloc>& lhs,
                const std::list<T,Alloc>& rhs);
template<class T, class Alloc>
bool operator<=(const std::list<T,Alloc>& lhs,
                 const std::list<T,Alloc>& rhs);
template<class T, class Alloc>
bool operator>(const std::list<T,Alloc>& lhs,
                const std::list<T,Alloc>& rhs);
template<class T, class Alloc>
bool operator>=(const std::list<T,Alloc>& lhs,
                 const std::list<T,Alloc>& rhs);
```

* 满足上述条件的，返回true；否则返回false。

*a. 一维链表比较大小*

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    list<int> nums1 = {1, 2, 3};
    list<int> nums2 = {1, 2, 3, 4};

    cout.flags(ios::boolalpha);
    cout << "nums1 < nums2:" << (nums1 < nums2) << endl;

    return 0;
}
```

代码输出：

```c++
nums1 < nums2:true
```

*b. 二维链表比较大小*

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    list<list<int>> nums1 = {{1, 2}, {3, 4}};
    list<list<int>> nums2 = {{1, 2}, {3, 5}};

    cout.flags(ios::boolalpha);
    cout << "nums1 < nums2:" << (nums1 < nums2) << endl;

    return 0;
}
```

代码输出：

```c++
nums1 < nums2:true
```

## list的sort排序

参见[03_算法/排序/02_含排序算法容器的排序]
