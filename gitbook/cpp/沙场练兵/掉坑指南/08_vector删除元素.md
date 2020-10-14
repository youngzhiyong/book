# vector删除元素

## 问题

下列代码删除奇数元素，代码的输出结果是什么？

```c++
#include <vector>
#include <iostream>

using namespace std;

void DelOddNums(vector<int>& nums)
{
    auto iter = nums.begin();
    for (; iter != nums.end(); ++iter) {
        if (*iter & 0x1) {
            iter = nums.erase(iter);
        }
    }
}

int main()
{
    vector<int> nums = {0, 1, 2, 3, 5, 7, 8, 10};

    DelOddNums(nums);
    for (auto num : nums) {
        cout << num << " ";
    }
    
    return 0;
}
```

## 答案

代码输出：

```c++
0 2 5 8 10
```

## FAQ

代码输出为何没有删除所有奇数元素？

因为`iter = nums.erase(iter)`语句，删除奇数后，返回的是删除元素的下一个元素。比如，删除元素3，返回指向5的iter迭代器。再经过for语句中的`++iter`语句后，iter迭代器指向元素7，从而成功的跳过元素5。

通用的方式为：

```c++
void DelOddNums(vector<int>& nums)
{
    auto iter = nums.begin();
    for (; iter != nums.end();) {
        if (*iter & 0x1) {
            iter = nums.erase(iter);
            continue;
        }

        ++iter;
    }
}
```
