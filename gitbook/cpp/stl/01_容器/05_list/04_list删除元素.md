# list删除元素

list删除元素，主要有以下几种方式：

* clear
* erase
* pop_front
* pop_back

**1.删除容器中所有的元素**

```c++
void clear();
```

调用clear后：

* 容器中不包含任何元素；
* `size()`返回0；

```c++
#include <list>
#include <iostream>

using namespace std;

void ShowNums(list<int>& nums)
{
    cout << "size:" << nums.size() << endl;

    cout << "val:";
    for (auto val : nums) {
        cout << val << " ";
    }
    cout << endl;
}

int main()
{
    list<int> nums = {1, 2, 3};
    ShowNums(nums);
    nums.clear();
    ShowNums(nums);

    return 0;
}
```

代码输出：

```c++
size:3
val:1 2 3
size:0
val:
```

**2.删除容器中指定元素或指定区间元素**

```c++
iterator erase(iterator pos);
iterator erase(iterator first, iterator last);
```

* erase返回被删除元素的下一个元素的迭代器，若删除最后一个元素，将返回`end()`迭代器。

注：两种删除迭代器指代元素的方法

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    list<int> nums = {1, 2, 3, 4, 5};
    for (auto iter = nums.begin(); iter != nums.end(); ) {
        if (*iter & 0x1) {
            iter++;
            continue;
        }

        iter = nums.erase(iter);    // 通用方法
        // nums.erase(iter++);      // 等价形式
    }

    for (auto val : nums) {
        cout << val << " ";
    }

    return 0;
}
```

代码输出：

```c++
1 3 5
```

**3.删除容器中的第一个元素**

```c++
void pop_front();
```

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    list<int> nums = {1, 2, 3, 4, 5};
    nums.pop_front();

    for (auto val : nums) {
        cout << val << " ";
    }

    return 0;
}
```

代码输出：

```c++
2 3 4 5
```

**4.删除容器中的最后一个元素**

```c++
void pop_back();
```

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    list<int> nums = {1, 2, 3, 4, 5};
    nums.pop_back();

    for (auto val : nums) {
        cout << val << " ";
    }

    return 0;
}
```

代码输出：

```c++
1 2 3 4
```

**5.vector&deque&lists删除元素性能对比**

*a.在首部删除元素*

```c++
#include <vector>
#include <deque>
#include <list>
#include <ctime>
#include <iostream>

using namespace std;

template<typename T>
void DelElements(T& container, int count)
{
    for (int i = 0; i < count; ++i) {
        container.erase(container.begin());
    }
}

// 统计运行fun函数耗时，返回值单位:毫秒
template<typename T>
double ElapsedTimeMs(void (*fun)(T&, int), T& container, int count)
{
    clock_t start = clock();
    fun(container, count);
    clock_t end = clock();

    return (end - start) * 1.0 / CLOCKS_PER_SEC * 1000;
}

int main()
{
    const int count = 500000;
    vector<int> vect(count);
    cout << "vector elapsed:" << ElapsedTimeMs(DelElements, vect, count) << "ms" << endl; 

    deque<int> que(count);
    cout << "deque elapsed:" << ElapsedTimeMs(DelElements, que, count) << "ms" << endl; 

    list<int> lst(count);
    cout << "list elapsed:" << ElapsedTimeMs(DelElements, lst, count) << "ms" << endl; 

    return 0;
}
```

代码输出：

```c++
vector elapsed:146978ms
deque elapsed:156ms
list elapsed:78ms
```

*b.在尾部删除元素*

```c++
#include <vector>
#include <deque>
#include <list>
#include <ctime>
#include <iostream>

using namespace std;

template<typename T>
void DelElements(T& container, int count)
{
    for (int i = 0; i < count; ++i) {
        container.pop_back();
    }
}

// 统计运行fun函数耗时，返回值单位:毫秒
template<typename T>
double ElapsedTimeMs(void (*fun)(T&, int), T& container, int count)
{
    clock_t start = clock();
    fun(container, count);
    clock_t end = clock();

    return (end - start) * 1.0 / CLOCKS_PER_SEC * 1000;
}

int main()
{
    const int count = 500000;
    vector<int> vect(count);
    cout << "vector elapsed:" << ElapsedTimeMs(DelElements, vect, count) << "ms" << endl; 

    deque<int> que(count);
    cout << "deque elapsed:" << ElapsedTimeMs(DelElements, que, count) << "ms" << endl; 

    list<int> lst(count);
    cout << "list elapsed:" << ElapsedTimeMs(DelElements, lst, count) << "ms" << endl; 

    return 0;
}
```

代码输出：

```c++
vector elapsed:16ms
deque elapsed:15ms
list elapsed:62ms
```
