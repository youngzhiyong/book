# array其他操作

## 容量

```c++
std::array<T,N>

constexpr bool empty() const noexcept;
constexpr size_type size() const noexcept;
constexpr size_type max_size()  noexcept;
```

* `emtpty`:array容器为空，返回true；不为空，返回false；
* `size`:返回array容器的元素个数N；
* `max_size()`:因为array的元素个数固定，返回array容器的元素个数N。

```c++
#include <array>
#include <iostream>

using namespace std;

int main()
{
    constexpr int len = 6;
    array<int, len> a = {1, 3, 9, 13, 19, 98};

    cout << "empty:" << a.empty() << endl;
    cout << "size:" << a.size() << endl;
    cout << "max_size:" << a.max_size() << endl;

    return 0;
}
```

代码输出：

```c++
empty:0
size:6
max_size:6
```

## array比较——非array成员函数

```c++
template< class T, std::size_t N >
bool operator==( const std::array<T,N>& lhs,
                 const std::array<T,N>& rhs );
template< class T, std::size_t N >
template< class T, std::size_t N >
bool operator!=( const std::array<T,N>& lhs,
                 const std::array<T,N>& rhs );
template< class T, std::size_t N >
bool operator<( const std::array<T,N>& lhs,
                const std::array<T,N>& rhs );
template< class T, std::size_t N >
bool operator<=( const std::array<T,N>& lhs,
                 const std::array<T,N>& rhs );
template< class T, std::size_t N >
bool operator>( const std::array<T,N>& lhs,
                const std::array<T,N>& rhs );
template< class T, std::size_t N >
bool operator>=( const std::array<T,N>& lhs,
                 const std::array<T,N>& rhs );
```

* 满足上述条件的，返回true；否则返回false。

```c++
#include <array>
#include <iostream>

using namespace std;

int main()
{
    constexpr int len = 6;
    array<int, len> a = {1, 3, 9, 13, 19, 98};
    array<int, len> b = {1, 3, 8, 13, 19, 98};

    cout.flags(ios::boolalpha);
    cout << "a > b " << (a > b) << endl;

    return 0;
}
```

输出结果：

```c++
a > b true
```
