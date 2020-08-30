# list增加元素

list增加元素主要有以下几种方式：

* assign
* insert
* emplace
* push_back
* emplace_back
* push_front
* emplace_front

**1. assign空对象，assign增加元素**

```c++
void assign(size_type count, const T& value);
template<class InputIt>
void assign(InputIt first, InputIt last);
void assign(std::initializer_list<T> ilist); 
```

* 若list对象中已经持有元素，调用assign后，**原有的数据将丢失**。

a. 将容器元素个数置为count，并将每个元素初始化为value。

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    list<int> nums;

    nums.assign(3, 9);
    for (auto val : nums) {
        cout << val << " ";
    }

    return 0;
}
```

代码输出：

```c++
9 9 9
```

b. 将其他可迭代对象容器中的元素，初始化当前list类型的容器。

```c++
#include <vector>
#include <list>
#include <iostream>

using namespace std;

int main()
{
    vector<int> origin = {8, 9, 1};
    list<int> nums;

    nums.assign(origin.begin(), origin.end());
    for (auto val : nums) {
        cout << val << " ";
    }

    return 0;
}
```

代码输出：

```c++
8 9 1
```

c. 使用初始化列表方式对已定义的list容器进行初始化。

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    list<int> nums;
    nums.assign({8, 9, 1});

    for (auto val : nums) {
        cout << val << " ";
    }

    return 0;
}
```

代码输出：

```c++
8 9 1
```

**2.在容器的pos位置之前插入元素**

```c++
iterator insert(iterator pos, const T& value);
iterator insert(const_iterator pos, size_type count, const T& value);

template<class InputIt>
iterator insert(const_iterator pos, InputIt first, InputIt last);

iterator insert(const_iterator pos, std::initializer_list<T> ilist);
```

* 在非首尾部插入元素，只需要修改前后node的指针的指向，时间复杂度为$O(1)$。

a. pos位置前插入一个元素

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    list<int> nums {8, 9, 1};
    nums.insert(nums.begin(), 3);
    nums.insert(nums.end(), 3);

    for (auto val : nums) {
        cout << val << " ";
    }

    return 0;
}
```

代码输出：

```c++
3 8 9 1 3
```

b. 在pos前插入多个相同元素

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    list<int> nums {8, 9, 1};

    auto iter = nums.begin();
    iter++;
    nums.insert(iter, 3, 10);

    for (auto val : nums) {
        cout << val << " ";
    }

    return 0;
}
```

代码输出：

```c++
8 10 10 10 9 1
```

c. 在pos前插入可迭代对象

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    list<int> nums {8, 9, 1};

    auto iter = nums.begin();
    iter++;

    int addNums[] = {10, 92};
    nums.insert(iter, begin(addNums), end(addNums));

    for (auto val : nums) {
        cout << val << " ";
    }

    return 0;
}
```

代码输出：

```c++
8 10 92 9 1
```

d. 使用初始化列表方式在pos位置前插入元素

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    list<int> nums {8, 9, 1};

    auto iter = nums.begin();
    iter++;

    nums.insert(iter, {10, 92});

    for (auto val : nums) {
        cout << val << " ";
    }

    return 0;
}
```

代码输出：

```c++
8 10 92 9 1
```

**3.在pos位置前插入就地(in-place at a location)初始化的元素**

```c++
template<class... Args>
iterator emplace(const_iterator pos, Args&&... args);
```

* emplace一次仅能插入**一个**list的元素；而insert可插入多个元素。
* args的参数类型、参数个数，须与list成员元素的构造函数的形参一致。
* 就地初始化新插入的元素，不再涉及创建临时元素对象的情况，因此效率比insert高。

```c++
#include <list>
#include <iostream>

using namespace std;

class Student {
public:
    Student(string name, int age): name(name), age(age) {}

    void Show()
    {
        cout << name << " " << age << endl;
    }

private:
    string name;
    int age;
};

int main()
{
    list<Student> students;
    students.emplace(students.begin(), "cpp", 38);

    for (auto student : students) {
        student.Show();
    }

    return 0;
}
```

代码输出：

```c++
cpp 38
```

**4.向list容器的尾部追加元素**

```c++
void push_back(const T& value);
```

```c++
#include <vector>
#include <list>
#include <iostream>

using namespace std;

int main()
{
    list<vector<int>> nums;
    nums.push_back({1, 2});
    nums.push_back({3, 4});

    for (auto& row : nums) {
        for (auto val : row) {
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
3 4 
```

**5.在尾部追加就地(in-place at a location)初始化的元素**

```c++
template<class... Args>
void emplace_back(Args&&... args);
```

* 在尾部追加元素，与push_back类似，只是emplace_back是使用就地初始化的方式，更加高效。

```c++
#include <list>
#include <iostream>

using namespace std;

class Student {
public:
    Student(string name, int age): name(name), age(age) {}

    void Show()
    {
        cout << name << " " << age << endl;
    }

private:
    string name;
    int age;
};

int main()
{
    list<Student> students;
    students.emplace_back("cpp", 38);

    for (auto student : students) {
        student.Show();
    }

    return 0;
}
```

代码输出：

```c++
cpp 38
```


**6.向list容器的首部追加元素**

```c++
void push_front(const T& value);
```

```c++
#include <list>
#include <iostream>

using namespace std;

int main()
{
    list<list<int>> nums;
    nums.push_front({3, 4});
    nums.push_front({1, 2});

    for (auto& row : nums) {
        for (auto val : row) {
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
3 4 
```

**7.在首部追加就地(in-place at a location)初始化的元素**

```c++
template<class... Args>
void emplace_front(Args&&... args);
```

* 在首部追加元素，与push_front类似，只是emplace_front是使用就地初始化的方式，更加高效。

```c++
#include <list>
#include <iostream>

using namespace std;

class Student {
public:
    Student(string name, int age): name(name), age(age) {}

    void Show()
    {
        cout << name << " " << age << endl;
    }

private:
    string name;
    int age;
};

int main()
{
    list<Student> students;
    students.emplace_front("cpp", 38);

    for (auto student : students) {
        student.Show();
    }

    return 0;
}
```

代码输出：

```c++
cpp 38
```

**8.vector&deque&list增加元素性能对比**

*a.在首部增加元素*

```c++
#include <vector>
#include <deque>
#include <list>
#include <ctime>
#include <iostream>

using namespace std;

template<typename T>
void AddElements(T& container, int count)
{
    for (int i = 0; i < count; ++i) {
        container.insert(container.begin(), i);
    }
}

// 统计运行fun函数耗时，返回值单位:毫秒
template<typename T>
double ElapsedTimeMs(void (*fun)(T&, int), T& container, int count)
{
    clock_t start = clock();
    fun(container, count);
    clock_t end = clock();

    return (end - start) * 1.0 / CLOCKS_PER_SEC * 1000;
}

int main()
{
    const int count = 500000;
    vector<int> vect;
    cout << "vector elapsed:" << ElapsedTimeMs(AddElements, vect, count) << "ms" << endl; 

    deque<int> que;
    cout << "deque elapsed:" << ElapsedTimeMs(AddElements, que, count) << "ms" << endl; 

    list<int> lst;
    cout << "list elapsed:" << ElapsedTimeMs(AddElements, lst, count) << "ms" << endl; 

    return 0;
}
```

代码输出：

```c++
vector elapsed:124809ms
deque elapsed:47ms
list elapsed:93ms
```

*b.在尾部增加元素*

```c++
#include <vector>
#include <deque>
#include <list>
#include <ctime>
#include <iostream>

using namespace std;

template<typename T>
void AddElements(T& container, int count)
{
    for (int i = 0; i < count; ++i) {
        container.push_back(i);
    }
}

// 统计运行fun函数耗时，返回值单位:毫秒
template<typename T>
double ElapsedTimeMs(void (*fun)(T&, int), T& container, int count)
{
    clock_t start = clock();
    fun(container, count);
    clock_t end = clock();

    return (end - start) * 1.0 / CLOCKS_PER_SEC * 1000;
}

int main()
{
    const int count = 500000;
    vector<int> vect;
    cout << "vector elapsed:" << ElapsedTimeMs(AddElements, vect, count) << "ms" << endl; 

    deque<int> que;
    cout << "deque elapsed:" << ElapsedTimeMs(AddElements, que, count) << "ms" << endl; 

    list<int> lst;
    cout << "list elapsed:" << ElapsedTimeMs(AddElements, lst, count) << "ms" << endl; 

    return 0;
}
```

代码输出：

```c++
vector elapsed:31ms
deque elapsed:16ms
list elapsed:109ms
```

耗时分析：

* 首部增加：deque > list > vector

   * vector：pos及以后的元素都将被移动；存储空间不足时，新分配存储空间，将旧空间中的元素都搬移到新存储空间。时间复杂度为$O(n)$。

   * deque：基本不涉及元素的搬移，只有当存储空间不足时，新申请定长的元素存储区用于存储新增的元素。时间复杂度为$O(1)$。

   * list：不涉及元素搬移；每新增一个元素，将新申请一个存储元素的node空间。时间复杂度为O(1)。

* 尾部增加：deque > vector> list
   
   * vector：基本不涉及元素搬移，只有当存储空间不足时，新分配存储空间，将旧空间中的元素都搬移到新存储空间。时间复杂度为$O(1)$。

   * deque：基本不涉及元素的搬移，只有当存储空间不足时，新申请定长的元素存储区用于存储新增的元素。时间复杂度为$O(1)$。

   * list：不涉及元素搬移；每新增一个元素，将新申请一个存储元素的node空间。时间复杂度为O(1)。
