# vector增加元素

**1.vector空对象，assign增加元素**

```c++
void assign(size_type count, const T& value);
template<class InputIt>
void assign(InputIt first, InputIt last);
void assign(std::initializer_list<T> ilist); 
```

以vector类型的对象容器作为类的成员，在初始化函数中，需要对其进行初始化时的常用方法之一。

a. 将容器元素个数置为count，并将每个元素初始化为value。

```c++
#include <vector>
#include <iostream>

using namespace std;

int main()
{
    vector<int> nums;

    nums.assign(3, 9);
    for (auto val : nums) {
            cout << val << " ";
    }

    return 0;
}
```

代码输出：

```c++
9 9 9
```

b. 将其他可迭代对象容器中的元素，初始化当前vector类型的容器。

```c++
#include <vector>
#include <iostream>

using namespace std;

int main()
{
    vector<int> origin = {8, 9, 1};
    vector<int> nums;

    nums.assign(origin.begin(), origin.end());
    for (auto val : nums) {
            cout << val << " ";
    }

    return 0;
}
```

代码输出：

```c++
8 9 1
```

c. 使用初始化列表方式对已定义的vector容器进行初始化。

```c++
#include <vector>
#include <iostream>

using namespace std;

int main()
{
    vector<int> nums;
    nums.assign({8, 9, 1});

    for (auto val : nums) {
            cout << val << " ";
    }

    return 0;
}
```

代码输出：

```c++
8 9 1
```

**2.**

```c++
iterator insert(iterator pos, const T& value);
iterator insert(const_iterator pos, size_type count, const T& value);

template<class InputIt>
iterator insert(const_iterator pos, InputIt first, InputIt last);

iterator insert(const_iterator pos, std::initializer_list<T> ilist);
```

```c++
template<class... Args> 
iterator emplace(const_iterator pos, Args&&... args);
```

```c++
void push_back(const T& value);
```

```c++
template<class... Args>
void emplace_back(Args&&... args);
```

```c++
void resize(size_type count);
void resize(size_type count, const value_type& value);
```

