# set创建对象

```c++
set();

explicit set(const Compare& comp, const Allocator& alloc = Allocator());

template< class InputIt >
set(InputIt first, InputIt last, const Compare& comp = Compare(), const Allocator& alloc = Allocator());

set(std::initializer_list<value_type> init, const Compare& comp = Compare(), const Allocator& alloc = Allocator());
```

注：仅介绍比较常规的对象创建方法。

**1.创建无元素对象**

```c++
#include <set>
#include <iostream>

using namespace std;

int main()
{
    set<int> nums;
    for (int i = 0; i < 3; ++i) {
        nums.insert(i);
    }

    for (auto val : nums) {
        cout << val << " ";
    }

    return 0;
}
```

代码输出：

```c++
0 1 2
```

**2.创建一个按照Compare作为排序规则的set对象**

注：Compare方法必须是一个严格的**弱排序规则**，否则在某些场景下出现排序结果错误问题。

**弱排序：**

以小于为例：

```c++
小于：a < b
大于：b < a
等于：!(a < b) && !(b < a)
```

*a. 利用已有函数作为排序规则*

```c++
include <vector>
#include <set>
#include <algorithm>
#include <functional>
#include <iostream>

using namespace std;

int main()
{
    auto compare = greater<int>();
    set<int, greater<int>> nums(compare);
    for (int i = 0; i < 5; ++i) {
       nums.insert(i); 
    }

    for (auto val : nums) {
        cout << val << " ";
    }

    return 0;
}
```

代码输出：

```c++
4 3 2 1 0
```

*b. 使用自定义排序规则*

```c++
#include <set>
#include <algorithm>
#include <functional>
#include <iostream>

using namespace std;

int main()
{
    auto compare = [](int lhd, int rhd) {
        return lhd < rhd;
    };

    set<int, decltype(compare)> nums(compare);
    for (int i = 0; i < 3; ++i) {
       nums.insert(i); 
    }

    for (auto val : nums) {
        cout << val << " ";
    }

    return 0;
}
```

代码输出：

```c++
0 1 2
```

*c.自定义弱排序规则同样会被用于判定元素的唯一性*

```c++
#include <set>
#include <algorithm>
#include <functional>
#include <iostream>

using namespace std;

int main()
{
    auto compare = [](int lhd, int rhd) {
        return (lhd & 0x1) < (rhd & 0x1);
    };

    set<int, decltype(compare)> nums(compare);
    for (int i = 0; i < 10; ++i) {
       nums.insert(i); 
    }

    for (auto val : nums) {
        cout << val << " ";
    }

    return 0;
}
```

运行结果：

```c++
0 1
```

分析：

对原有值取最低位进行比较，而比较的时候原始值都为偶数时，在调用compare方法时，将会出现`!(a < b) && !(b < a)`的状况，导致被误认为a==b，在进行唯一性处理后，所有偶数仅为一个0，奇数仅为1个1。

**警示**

排序规则使用自定义排序规则时：

* 保证compare的弱排序性
* 使用自定义排序规则出现的副作用


**3.使用可迭代对象创建set对象**

```c++
#include <vector>
#include <set>
#include <iostream>

using namespace std;

int main()
{
    vector<int> origin = {8, 20, 3};
    set<int> nums(origin.begin(), origin.end());

    for (auto val : nums) {
        cout << val << " ";
    }

    return 0;
}
```

代码输出：

```c++
3 8 20
```

**4.使用初始化列表方式创建对象**

```c++
#include <set>
#include <iostream>

using namespace std;

int main()
{
    set<int> nums = {1, 2, 3};
    // set<int> nums {1, 2, 3}; // 等价形式

    for (auto val : nums) {
        cout << val << " ";
    }

    return 0;
}
```

代码输出：

```c++
1 2 3
```
