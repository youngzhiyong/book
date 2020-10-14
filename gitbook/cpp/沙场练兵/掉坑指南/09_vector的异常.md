# vector的死循环

## 问题

请给出下列代码的输出结果：

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
    vector<int> nums = {0, 1, 2, 3, 5, 7, 8, 11};

    DelOddNums(nums);
    for (auto num : nums) {
        cout << num << " ";
    }
    
    return 0;
}
```

## 答案

程序出现异常，程序行为不可预期。

当前问题，与另外一个问题(vector删除元素)，代码基本相同，唯一区别就是nums的最后一个元素被改为11。

程序出现异常的原因，不正确的使用iter删除元素，导致删除最后一个元素11后，iter指向nums.end()，再次对iter累加后，导致iter不能和iter.end()判等。从而导致for循环一直成立，出现死循环。但是此后删除的非法iter，可能导致程序崩溃，程序运行结束。
