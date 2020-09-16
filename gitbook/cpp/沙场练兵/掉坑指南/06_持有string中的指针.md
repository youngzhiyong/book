# 持有string中的指针

## 问题

```c++
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Route {
public:
    void MoveTo(string destination) 
    {
        // curAddr = destination;
        curAddr.replace(0, curAddr.length(), destination);
        SaveAddress();
    }

    void SaveAddress()
    {
        route.push_back(curAddr.c_str());
    }

    void ShowRoute()
    {
        for (auto pos : route) {
            cout << pos << "->";
        }
    }

private:
    string curAddr;
    vector<const char*> route;
};

int main()
{
    Route route;
    route.MoveTo("Shang Hai");
    route.MoveTo("Cheng Du");
    route.MoveTo("Bei Jing");

    route.ShowRoute();

    return 0;
}
```

代码输出：

```c++
Bei Jing->Bei Jing->Bei Jing->
```

上述代码中，什么原因导致不可预期结果？

## 答案

代码中保存string.c_str()返回的字符数组指针，`curAddr`字符串的内容被`replace`后，字符数组中的字符串被替换。但前几次保存的都是同一个内存地址，在`ShowRoute`时，输出相同的最后一个地址。

**FAQ：**

如果把`Bei Jing`改为`Bei Jing-Great Wall`，会出现什么情况呢？

答：
可能会出现，string中的字符数组空间，不足以存储较长的地址信息，需要新申请空间，导致之前保存到Route.route中的地址失效，输出乱码。

```c++
�/Z->�/Z->Bei Jing-Great Wall->
```

## 建议：

代码中**不应保存**string.c_str()返回的C-string的字符数组的指针。

