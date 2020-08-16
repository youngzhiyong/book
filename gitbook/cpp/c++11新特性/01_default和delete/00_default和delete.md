# = default和 = delete

## = default

default主要用于修饰类的特殊方法(默认(无参)构造函数、析构函数、拷贝构造函数、赋值操作符重载函数、移动构造函数、移动赋值操作符重载函数)，其意义如下：

* 简化代码书写
* 提高运行效率：比如拷贝构造函数，不做深拷贝的情况下使用default修饰后，能够default修饰后，编译器能优化成member-wise的拷贝，提高效率。

**1.默认(无参)构造函数**

*a.未包含自定义构造函数*

```c++
#include <iostream>
using namespace std;

class Foo {
public:
    int a;
    int b;
};

int main()
{
    Foo foo;
    cout << foo.a << "--" << foo.b << endl;

    return 0;
}
```

代码输出：

```c++
2293640--4202446
```

*b.包含自定义构造函数*

```c++
#include <iostream>
using namespace std;

class Foo {
public:
    Foo(int a, int b): a(a), b(b) {}

    int a;
    int b;
};

int main()
{
    Foo foo;
    cout << foo.a << "--" << foo.b << endl;

    return 0;
}
```

编译输出：

```c++
test.cpp: In function 'int main()':
test.cpp:14:9: error: no matching function for call to 'Foo::Foo()'
     Foo foo;
         ^
test.cpp:14:9: note: candidates are:
test.cpp:6:5: note: Foo::Foo(int, int)
     Foo(int a, int b): a(a), b(b) {}
     ^
test.cpp:6:5: note:   candidate expects 2 arguments, 0 provided
test.cpp:4:7: note: constexpr Foo::Foo(const Foo&)

......
```

一旦含自定义构造函数，编译器将不再生成默认构造函数，此时需要定义一个默认(无参)构造函数，可修改为：

```c++
#include <iostream>
using namespace std;

class Foo {
public:
    Foo() = default;    // Foo() {}
    Foo(int a, int b): a(a), b(b) {}

    int a;
    int b;
};

int main()
{
    Foo foo;
    cout << foo.a << "--" << foo.b << endl;

    return 0;
}
```

代码输出：

```c++
2293640--4202446
```

**c.类外声明**

```c++
#include <iostream>
using namespace std;

class Foo {
public:
    Foo();
    Foo(int a, int b) {}
};

Foo::Foo() = default;

int main()
{
    Foo foo;

    return 0;
}
```

**2.非默认构造函数**

```c++
#include <iostream>
using namespace std;

class Foo {
public:
    Foo(int a, int b) = default;
};

int main()
{
    return 0;
}
```

编译输出：

```c++
test.cpp:6:25: error: 'Foo::Foo(int, int)' cannot be defaulted
     Foo(int a, int b) = default;
                         ^
The terminal process terminated with exit code: 1
```

## = delete

显示的禁用某个函数，没有特殊函数和类成员函数的要求。

**1.禁用某些参数列表的构造函数**

限制对某些参数类型构造函数的使用。

```c++
#include <iostream>
using namespace std;

class Foo {
public:
    Foo() {}
    Foo(int a) {}
    Foo(char a) = delete;
};

int main()
{
    Foo foo('a');

    return 0;
}
```

编译输出：

```c++
test.cpp: In function 'int main()':
test.cpp:13:16: error: use of deleted function 'Foo::Foo(char)'
     Foo foo('a');
                ^
test.cpp:8:5: note: declared here
     Foo(char a) = delete;
     ^
The terminal process terminated with exit code: 1
```

**2.禁用拷贝构造、移动构造、赋值操作符重载函数、移动赋值操作符重载**

仅支持对象的创建，限制对象间的拷贝，常见于限制对象所有权的转移，比如：C++ 11中的多线程的互斥锁；单例设计模式类的定义中。

*a.未使用delete实现的单例*

```c++
#include <iostream>
using namespace std;

class Singleton {
public:
    static Singleton& Instance()
    {
        static Singleton singleton;
        return singleton;
    }

private:
    Singleton() {}
    Singleton(const Singleton& other) {}
    Singleton(Singleton&& other) {}
    Singleton& operator=(const Singleton& other) {}
    Singleton& operator=(Singleton&& other) {}
};

int main()
{
    Singleton& single1 = Singleton::Instance();
    Singleton& single2 = Singleton::Instance();

    cout << "addr=" << &single1 << ":" << &single2 << endl;

    return 0;
}
```

代码输出：

```c++
addr=0x403030:0x403030
```

*b.使用delete实现的单例*

```c++
#include <iostream>
using namespace std;

class Singleton {
public:
    static Singleton& Instance()
    {
        static Singleton singleton;
        return singleton;
    }

private:
    Singleton() {}
    Singleton(const Singleton& other) = delete;
    Singleton(Singleton&& other) = delete; 
    Singleton& operator=(const Singleton& other) = delete; 
    Singleton& operator=(Singleton&& other) = delete; 
};

int main()
{
    Singleton& single1 = Singleton::Instance();
    Singleton& single2 = Singleton::Instance();

    cout << "addr=" << &single1 << ":" << &single2 << endl;

    return 0;
}
```

代码输出：

```c++
addr=0x403030:0x403030
```

**3.类中特殊函数禁用后的呈现**

**4.禁用某些参数列表的重载函数**

*a.禁用类中某些参数列表的重载函数*

```c++
#include <iostream>
using namespace std;

class Foo {
public:
    void foo(int a) {}
    void foo(char a) {}
    void foo(int a, int b) {}
    void foo(char a, char b) {}
    void foo(int a, char b) = delete;
    void foo(char a, int b) = delete;
};

int main()
{
    char a = 'a';
    int b = 3;

    Foo foo;
    foo.foo(a, b);

    return 0;
}
```

编译输出：

```c++
test.cpp: In function 'int main()':
test.cpp:20:17: error: use of deleted function 'void Foo::foo(char, int)'
     foo.foo(a, b);
                 ^
test.cpp:11:10: note: declared here
     void foo(char a, int b) = delete;
          ^
The terminal process terminated with exit code: 1
```

*b.禁用某些参数列表的全局重载函数*

```c++
#include <iostream>
using namespace std;

void Foo(int a) {}
void Foo(char a) {}
void Foo(int a, int b) {}
void Foo(char a, char b) {}
void Foo(int a, char b) = delete;
void Foo(char a, int b) = delete;

int main()
{
    char a = 'a';
    int b = 3;

    Foo(a, b);

    return 0;
}
```

编译输出：

```c++
test.cpp: In function 'int main()':
test.cpp:16:13: error: use of deleted function 'void Foo(char, int)'
     Foo(a, b);
             ^
test.cpp:9:6: note: declared here
 void Foo(char a, int b) = delete;
      ^
The terminal process terminated with exit code: 1
```
