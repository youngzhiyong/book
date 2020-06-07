# deque删除元素

deque删除元素，主要有以下几种方式：

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
#include <deque>
#include <iostream>

using namespace std;

void ShowNums(deque<int>& nums)
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
    deque<int> nums = {1, 2, 3};
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

* 删除容器非首尾部的元素，根据pos前后的元素个数，决定pos前面的元素还是pos后的元素进行移动；
* erase返回被删除元素的下一个元素的迭代器，若删除最后一个元素，将返回`end()`迭代器。

注：两种删除迭代器指代元素的方法

```c++
#include <deque>
#include <iostream>

using namespace std;

int main()
{
    deque<int> nums = {1, 2, 3, 4, 5};
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
#include <deque>
#include <iostream>

using namespace std;

int main()
{
    deque<int> nums = {1, 2, 3, 4, 5};
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
#include <deque>
#include <iostream>

using namespace std;

int main()
{
    deque<int> nums = {1, 2, 3, 4, 5};
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
