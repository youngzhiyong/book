# set简介

set是一种使用**红黑树**存储管理所有元素的关联容器，可根据提供的Compare方法对容器中包含的所有元素进行**自动排序**。容器中的所有元素具有**唯一性**。

**特点：**

* 自动排序
* 元素唯一性
* 插入/删除n个元素，时间复杂度为$O(nlogn)$

**类声明：**

```c++
template<
    class Key,
    class Compare = std::less<Key>,
    class Allocator = std::allocator<Key>
> class set;

// 头文件包含
#include <set>
```

**容器相关操作：**

* 增：set容器中增加n个元素，涉及红黑树的调整，时间复杂度为$O(nlogn)$

* 删：set容器中删除n个元素，设计红黑树的调整，时间复杂度为$O(nlogn)$

* 查：在红黑树中查找某元素，时间复杂度为$O(logn)$

* 改：迭代器方式修改

**应用场景：**

* 容器内元素值保持唯一
* 每次新增/删除一个元素，容器内保持有序
