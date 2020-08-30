# deque增加元素

deque增加元素主要有以下几种方式：

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

* 以deque类型的对象容器作为类的成员，在初始化函数中，需要对其进行初始化时的常用方法之一。
* 若deque对象中已经持有元素，调用assign后，**原有的数据将丢失**。

a. 将容器元素个数置为count，并将每个元素初始化为value。

```c++
#include <deque>
#include <iostream>

using namespace std;

int main()
{
    deque<int> nums;

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

b. 将其他可迭代对象容器中的元素，初始化当前deque类型的容器。

```c++
#include <vector>
#include <deque>
#include <iostream>

using namespace std;

int main()
{
    vector<int> origin = {8, 9, 1};
    deque<int> nums;

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

c. 使用初始化列表方式对已定义的deque容器进行初始化。

```c++
#include <deque>
#include <iostream>

using namespace std;

int main()
{
    deque<int> nums;
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

* 在非首尾部插入元素，根据pos位置前后的元素个数，决定pos前面的元素还是pos后面的元素移动。

a. pos位置前插入一个元素

```c++
#include <deque>
#include <iostream>

using namespace std;

int main()
{
    deque<int> nums {8, 9, 1};
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
#include <deque>
#include <iostream>

using namespace std;

int main()
{
    deque<int> nums {8, 9, 1};

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
#include <deque>
#include <iostream>

using namespace std;

int main()
{
    deque<int> nums {8, 9, 1};

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
#include <deque>
#include <iostream>

using namespace std;

int main()
{
    deque<int> nums {8, 9, 1};

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

* emplace一次仅能插入**一个**deque的元素；而insert可插入多个元素。
* args的参数类型、参数个数，须与deque成员元素的构造函数的形参一致。
* 就地初始化新插入的元素，不再涉及创建临时元素对象的情况，因此效率比insert高。

```c++
#include <deque>
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
    deque<Student> students;
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

**4.向deque容器的尾部追加元素**

```c++
void push_back(const T& value);
```

```c++
#include <deque>
#include <iostream>

using namespace std;

int main()
{
    deque<deque<int>> nums;
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
#include <deque>
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
    deque<Student> students;
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


**6.向deque容器的首部追加元素**

```c++
void push_front(const T& value);
```

```c++
#include <deque>
#include <iostream>

using namespace std;

int main()
{
    deque<deque<int>> nums;
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
#include <deque>
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
    deque<Student> students;
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