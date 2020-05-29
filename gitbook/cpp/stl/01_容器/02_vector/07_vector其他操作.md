# vector其他操作

## 容量

**1. 获取存储元素个数信息**

```c++
bool empty() const;
size_type size() const;
size_type max_size() const;
size_type capacity() const;
```

* `empty`:判定vector容器中是否为空。
* `size`:获取容器中当前**元素个数**。
* `max_size`:获取容器能存放当前类型元素最大个数，取决于系统和库代码的实现。
* `capacity`:获取当前已分配存储空间能容纳元素的个数。

```c++
#include <vector>
#include <iostream>

using namespace std;

template<typename T>
void Show(const vector<T>& nums)
{
    cout.flags(ios::boolalpha);
    cout << "empty:" << nums.empty() << endl;
    cout << "size:" << nums.size() << endl;
    cout << "sizeof(T):" << sizeof(T) << " max_size:" << nums.max_size() << endl;
    cout << "capacity:" << nums.capacity() << endl;
}

int main()
{
    vector<int> intNums = {
        1, 2, 3, 4
    };

    cout << "Type=int info as follows:" << endl;
    Show(intNums);
    cout << endl;

    vector<long long> llNums = {
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
sizeof(T):4 max_size:1073741823
capacity:4

Type=long long info as follows:
empty:false
size:4
sizeof(T):8 max_size:536870911
capacity:6
```

**FAQ**
a. intNums中存储的元素个数与llNums中元素个数相同，为何capacity却不相同？

* intNums容器在整个生命周期中，元素个数始终保持与初始定义时个数相同，不需要为其进行预分配；
* llNums容器，在初始定义时为3个，而后期使用push_back增加元素，而在push_back操作中，会为其预分配相应的存储空间。

**2. 预分配存储空间**

```c++
void reserve(size_type new_cap);
```

* 场景：可确定需要存储元素个数；
* 功能：**预分配存储空间**，减少新增元素过程中的频繁申请、释放内存动作，适当提高运行效率（效果不是很明显）；
* 影响：增大capacity，对size和max_size无影响。

*a. 未使用reserve，新增100万个元素*

```c++
#include <vector>
#include <ctime>
#include <iostream>

using namespace std;

// 统计运行fun函数耗时，返回值单位:秒
double ElapsedTime(void (*fun)())
{
    clock_t start = clock();
    fun();
    clock_t end = clock();

    return (end - start) * 1.0 / CLOCKS_PER_SEC;
}

void Foo()
{
    const int count = 1e7;
    vector<int> nums;

    cout << "size:" << nums.size() << endl;
    cout << "capacity:" << nums.capacity() << endl;

    for (int i = 0; i < count; ++i) {
        nums.push_back(i);
    }
}

int main()
{
    auto elapsed = ElapsedTime(Foo);
    cout << "elapsed time = " << (elapsed * 1000) << "ms" << endl;

    return 0;
}
```

代码输出：

```c++
size:0
capacity:0
elapsed time = 1276ms
```

*b. 使用reserve，新增100万个元素*

```c++
#include <vector>
#include <ctime>
#include <iostream>

using namespace std;

double ElapsedTime(void (*fun)())
{
    clock_t start = clock();
    fun();
    clock_t end = clock();

    return (end - start) * 1.0 / CLOCKS_PER_SEC;
}

void Foo()
{
    const int count = 1e7;
    vector<int> nums;
    nums.reserve(count);        // 使用reserve

    cout << "size:" << nums.size() << endl;
    cout << "capacity:" << nums.capacity() << endl;

    for (int i = 0; i < count; ++i) {
        nums.push_back(i);
    }
}

int main()
{
    auto elapsed = ElapsedTime(Foo);
    cout << "elapsed time = " << (elapsed * 1000) << "ms" << endl;

    return 0;
}
```

代码输出：

```c++
size:0
capacity:10000000
elapsed time = 389ms
```

*c. 未使用reserve，内存多次申请释放*

```c++
#include <vector>
#include <iostream>

using namespace std;

template<typename T>
class Allocator {
public:
    typedef T value_type;
    Allocator() = default;
    Allocator(const Allocator<T>&) {}

    T* allocate(size_t n) 
    {
        cout << "allocate elements:" << n << endl;
        return static_cast<int*>(::operator new(n * sizeof(T)));
    }

    void deallocate(T* ptr, size_t n)
    {
        cout << "deallocate elements:" << n << endl;
        ::operator delete(ptr);
    }
};

int main()
{
    const int count = 100;
    vector<int, Allocator<int>> nums;
    for (int i = 0; i < count; ++i) {
        nums.push_back(i);
    }

    return 0;
}
```

代码输出：

```c++
allocate elements:1
allocate elements:2
deallocate elements:1  
allocate elements:4
deallocate elements:2  
allocate elements:8
deallocate elements:4  
allocate elements:16
deallocate elements:8  
allocate elements:32
deallocate elements:16
allocate elements:64
deallocate elements:32
allocate elements:128  
deallocate elements:64
deallocate elements:128
```

*d. 使用reserve，内存申请释放一次*

```c++
#include <vector>
#include <iostream>

using namespace std;

template<typename T>
class Allocator {
public:
    typedef T value_type;
    Allocator() = default;
    Allocator(const Allocator<T>&) {}

    T* allocate(size_t n) 
    {
        cout << "allocate elements:" << n << endl;
        return static_cast<int*>(::operator new(n * sizeof(T)));
    }

    void deallocate(T* ptr, size_t n)
    {
        cout << "deallocate elements:" << n << endl;
        ::operator delete(ptr);
    }
};

int main()
{
    const int count = 100;
    vector<int, Allocator<int>> nums;
    nums.reserve(count);                // 使用reserve
    for (int i = 0; i < count; ++i) {
        nums.push_back(i);
    }

    return 0;
}
```

代码输出：

```c++
allocate elements:100
deallocate elements:100
```

**3. 伸缩容器存储元素空间**

```c++
void resize(size_type count);
void resize(size_type count, const value_type& value);
```

* `count < size()`：缩减容器大小为count个有效元素；
* `count > size()`：使用value/默认值填充新增至count个元素，原数据值保持不变。

*a.缩减容器元素个数*

```c++
#include <vector>
#include <iostream>

using namespace std;

int main()
{
    const int count = 100;
    vector<int> nums;
    for (int i = 0; i < count; ++i) {
        nums.push_back(i);
    }

    cout << nums.size() << " " << nums.capacity() << endl;
    nums.resize(5);
    cout << nums.size() << " " << nums.capacity() << endl;

    return 0;
}
```

代码输出：

```c++
100 128
5 128
```

**注：**
缩减容器中的元素个数，不影响预分配的存储空间，与原容器的capacity保持一致。

*b. 增大容器元素个数*

```c++
#include <vector>
#include <iostream>

using namespace std;

int main()
{
    const int count = 100;
    vector<int> nums;
    for (int i = 0; i < count; ++i) {
        nums.push_back(i);
    }

    cout << nums.size() << " " << nums.capacity() << endl;
    nums.resize(count * 2);
    cout << nums.size() << " " << nums.capacity() << endl;

    return 0;
}
```

代码输出：

```c++
100 128
200 200
```

**注：**

增大容器元素个数，size的值与capacity的值相同。

## vector比较

vector容器与容器之间可以直接比较大小，无需再次实现vector容器间的比较函数。

```c++
template<class T, class Alloc>
bool operator==(const std::vector<T,Alloc>& lhs,
                 const std::vector<T,Alloc>& rhs);
template<class T, class Alloc>
constexpr bool operator==(const std::vector<T,Alloc>& lhs,
                           const std::vector<T,Alloc>& rhs);
template<class T, class Alloc>
bool operator!=(const std::vector<T,Alloc>& lhs,
                 const std::vector<T,Alloc>& rhs);
template<class T, class Alloc>
bool operator<(const std::vector<T,Alloc>& lhs,
                const std::vector<T,Alloc>& rhs);
template<class T, class Alloc>
bool operator<=(const std::vector<T,Alloc>& lhs,
                 const std::vector<T,Alloc>& rhs);
template<class T, class Alloc>
bool operator>(const std::vector<T,Alloc>& lhs,
                const std::vector<T,Alloc>& rhs);
template<class T, class Alloc>
bool operator>=(const std::vector<T,Alloc>& lhs,
                 const std::vector<T,Alloc>& rhs);
```

* 满足上述条件的，返回true；否则返回false。

```c++
#include <vector>
#include <iostream>

using namespace std;

int main()
{
    vector<int> nums1 = {1, 2, 3};
    vector<int> nums2 = {1, 2, 3, 4};

    cout.flags(ios::boolalpha);
    cout << "nums1 < nums2:" << (nums1 < nums2) << endl;

    return 0;
}
```

代码输出：

```c++
nums1 < nums2:true
```
