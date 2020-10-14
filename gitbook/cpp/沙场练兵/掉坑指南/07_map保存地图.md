# map保存地图

## 问题

将地图中节点的连接，使用邻接链表的方式保存。

```c++
1->2
3->4
2->5
2->6
```

下列代码是否能实现上述功能？

```c++
#include <map>
#include <vector>
#include <iostream>

using namespace std;

map<int, int> TransToLinks(vector<vector<int>>& nodes)
{
    map<int, int> links;
    for (auto node : nodes) {
        links[node[0]] = node[1];
    }

    return links;
}

void ShowLinks(map<int, int>& links)
{
    for (auto item : links) {
        cout << item.first << "->" << item.second << endl;
    }
}

int main()
{
    vector<vector<int>> nodes = {
        {1, 2}, {3, 4},
        {2, 5}, {2, 6}
    };

    auto links = TransToLinks(nodes);
    ShowLinks(links);

    return 0;
}
```

代码输出：

```c++
1->2
2->6
3->4
```

为何2->5号节点的连接丢失？

## 答案

因为C++中map的key具有**唯一性**。[cppreference](https://en.cppreference.com/w/cpp/container/map)中有如下描述：

```c++
std::map is a sorted associative container that contains key-value pairs with unique keys.
```

## FAQ

有哪些方法可以存储邻接链表呢？

答：可以采用如下方式，可以有更多的方式：

* 同样使用map，只不过类型为map<int, vector<int>>，map的key为起始节点，value使用vector存储多个目的节点

* 若节点的编号较小，可以使用数组的方式，以起始节点编号为数组下标，vector<vector<int>>
