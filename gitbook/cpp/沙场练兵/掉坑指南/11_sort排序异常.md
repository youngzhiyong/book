# sort排序异常

## 问题

下列代码根据字符的个数进行排序，下列代码是否能达到期望结果？为什么？

```c++
#include <vector>
#include <unordered_map>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

int main()
{
    string str("abcdefghijklmnopq");

    unordered_map<char, int> counter;
    for (auto chr : str) {
        counter[chr]++;
    }

    auto comp = [](auto& lhd, auto& rhd) {
        return lhd.second <= rhd.second;
    };

    vector<pair<char, int>> sortedChar(counter.begin(), counter.end());

    sort(sortedChar.begin(), sortedChar.end(), comp);
    for (auto& item : sortedChar) {
        cout << item.first << ":" << item.second << endl;
    }

    return 0;
}
```

## 答案

不能达到预期结果，并且程序运行结果异常，可能在某些情况会出现core dump。

C++ STL中的sort函数的排序，使用了3种方式：

* 若参与排序的元素个数≤16，采用插入排序的方式完成排序；
* 若参与排序的元素个数＞16，采用快速排序的方式；
* 若快速排序递归层次达到一定深度，则采用堆排序的方式。

其中，快速排序位于[stl_algo.h](https://github.com/gcc-mirror/gcc/blob/d9375e490072d1aae73a93949aa158fcd2a27018/libstdc%2B%2B-v3/include/bits/stl_algo.h)头文件中的部分代码如下：

```c++
// 代码路径：sort -> __sort -> __introsort_loop -> __unguarded_partition_pivot -> __unguarded_partition
template<typename _RandomAccessIterator, typename _Compare>
_RandomAccessIterator __unguarded_partition(_RandomAccessIterator __first, _RandomAccessIterator __last,
			                                _RandomAccessIterator __pivot, _Compare __comp)
{
    while (true) {
        while (__comp(__first, __pivot))    // ①
            ++__first;
        --__last;
        while (__comp(__pivot, __last))     // ②
            --__last;
        if (!(__first < __last))
            return __first;
        std::iter_swap(__first, __last);
        ++__first;
    }
}
```

上例中的comp函数为不是严格弱排序的比较函数，因此在sort函数执行时，**代码①和②的while条件将一直能满足，导致first和last都越界**，从而引起程序异常，且可能导致段错误，出现core dump。

