# vector创建对象

```c++
vector();
explicit vector(size_type count);
explicit vector(size_type count, const T& value = T(), const Allocator& alloc = Allocator());
vector(std::initializer_list<T> init, const Allocator& alloc = Allocator());
vector(InputIt first, InputIt last, const Allocator& alloc = Allocator());
```

注：仅介绍比较常规的对象创建方法。

**1.创建无元素对象**

定义对象后，采用尾部追加方式新增元素元素。

```c++
#include <vector>
#include <iostream>

using namespace std;

int main()
{
    vector<int> nums;
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
#include <vector>
#include <iostream>

using namespace std;

int main()
{
    vector<int> nums(3);

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
#include <vector>
#include <iostream>

using namespace std;

int main()
{
    vector<int> nums(5, 20);

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
#include <vector>
#include <iostream>

using namespace std;

int main()
{
    vector<int> nums = {1, 2, 3};
    // vector<int> nums {1, 2, 3}; // 等价形式

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

**5.使用可迭代对象创建vector对象**

```c++
#include <array>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
    array<int, 3> arr = {1, 2, 3};
    vector<int> nums(arr.begin(), arr.end());

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

**6.创建二维数组空容器**

```c++
#include <vector>
#include <iostream>

using namespace std;

int main()
{
    vector<int> rowNums = {1, 2, 3};
    vector<vector<int>> nums;

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

```c++
#include <vector>
#include <iostream>

using namespace std;

int main()
{
    vector<vector<int>> nums(2);

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
#include <vector>
#include <iostream>

using namespace std;

int main()
{
    // 每一行的元素个数可以不同，注意与C风格的二维数组区别
    vector<vector<int>> nums = {{1, 2}, {8}};

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
#include <vector>
#include <iostream>

using namespace std;

int main()
{
    // 2行3列
    vector<vector<int>> nums(2, vector<int>(3, 8));

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
#include <array>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
    vector<vector<int>> nums(2, {9, 2, 3});

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
