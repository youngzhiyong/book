# list创建对象

```c++
list();
explicit list(size_type count);
explicit list(size_type count, const T& value = T(), const Allocator& alloc = Allocator());
list(std::initializer_list<T> init, const Allocator& alloc = Allocator());
list(InputIt first, InputIt last, const Allocator& alloc = Allocator());
```

注：仅介绍比较常规的对象创建方法。

**1.创建无元素对象**

定义对象后，采用尾部追加方式新增元素。

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    list<int> nums;
    for (int i = 0; i < 3; ++i) {
        nums.push_back(i);
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

**2.创建元素个数为n的对象**

注：n个对象均采用无参构造函数的方式初始化。若为基本类型，初始化为0。

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    list<int> nums(3);

    for (auto val : nums) {
        cout << val << " ";
    }

    return 0;
}
```

代码输出：

```c++
0 0 0 
```

**3.创建元素个数为n,且均初始化为value的对象**

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    list<int> nums(5, 20);

    for (auto val : nums) {
        cout << val << " ";
    }

    return 0;
}
```

代码输出：

```c++
20 20 20 20 20 
```

**4.使用初始化列表方式创建对象**

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    list<int> nums = {1, 2, 3};
    // list<int> nums {1, 2, 3}; // 等价形式

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

**5.使用可迭代对象创建list对象**

```c++
#include <vector>
#include <list>
#include <iostream>

using namespace std;

int main()
{
    vector<int> origin = {1, 2, 3};
    list<int> nums(origin.begin(), origin.end());

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

**6.创建二维链表空容器**

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    list<int> rowNums = {1, 2, 3};
    list<list<int>> nums;

    nums.push_back(rowNums);
    nums.push_back(rowNums);

    for (auto& row : nums) {
        for (int val : row) {
            cout << val << " ";
        }
        cout << endl;
    }

    return 0;
}
```

代码输出：

```c++
1 2 3
1 2 3
```

**7.创建二维数组n行元素**

vector和list相结合，可以充分利用vector和list的优点，补充各自的不足：

* vector可支持随机访问，能够快速的定位到修改位置；非末尾增删元素，时间复杂度较高。
* list可支持任意位置快速增删元素；但不支持随机访问。

```c++
#include <vector>
#include <list>
#include <iostream>

using namespace std;

int main()
{
    vector<list<int>> nums(2);

    nums[0].push_back(1);
    nums[1].push_back(3);

    for (auto& row : nums) {
        for (int val : row) {
            cout << val << " ";
        }
        cout << endl;
    }

    return 0;
}
```

代码输出：

```c++
1 
3
```

**8.使用初始化列表方式创建二维数组**

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    // 每一行的元素个数可以不同，注意与C风格的二维数组区别
    list<list<int>> nums = {{1, 2}, {8}};

    for (auto& row : nums) {
        for (int val : row) {
            cout << val << " ";
        }
        cout << endl;
    }

    return 0;
}
```

代码输出：

```c++
1 2 
8
```

**9.创建二维数组n*m个元素，每个元素值相同**

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    // 2行3列
    list<list<int>> nums(2, list<int>(3, 8));

    for (auto& row : nums) {
        for (int val : row) {
            cout << val << " ";
        }
        cout << endl;
    }

    return 0;
}
```

代码输出：

```c++
8 8 8 
8 8 8
```

**10.创建二维数组n*m个元素，每行元素之间相同**

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    list<list<int>> nums(2, {9, 2, 3});

    for (auto& row : nums) {
        for (int val : row) {
            cout << val << " ";
        }
        cout << endl;
    }

    return 0;
}
```

代码输出：

```c++
9 2 3
9 2 3
```

**建议：**

* list不支持随机访问，建议不要使用list创建二维数组；建议使用vector创建二维数组。

* 若创建n行，每行支持频繁增删元素，可使用[7.创建二维数组n行元素]()的方式。
