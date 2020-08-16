# override和final

override和final都是C++ 11新增的关键字，主要用于修饰子类覆盖父类虚函数时使用。

* override：标识子类函数是覆盖父类虚函数
* final：标识子类覆盖父类虚函数，后续子类不能再覆盖当前子类的该虚函数，称为该函数的最后一次覆盖。

## override

**override意义**

在C++ 11以前，不使用override，同样也能通过子类覆盖，实现虚特性，实现动态多态性。override出现的意义是什么呢？

大家先来观察下面的例子。

利用多态性，调用多个子类对象的Bubble函数

```c++
#include <vector>
#include <iostream>
using namespace std;

class Base {
public:
    virtual void Bubble()
    {
        cout << "base bubble" << endl;
    }
};

class Derive : public Base {
public:
    void Babble()
    {
        cout << "derive bubble" << endl;
    }
};

class Foo : public Base {
public:
    void Bubble()
    {
        cout << "Foo bubble" << endl;
    }
};

int main()
{
    Base base;
    Derive derive;
    Foo foo;
    vector<Base*> bubble = {
        &base, &derive, &foo
    };

    for (auto it : bubble) {
        it->Bubble();
    }

    return 0;
}
```

代码输出：

```c++
base bubble
base bubble
Foo bubble
```

分析：

* 在Derive类中，定义Bubble时，出现拼写错误，误写成了Babble。当然，修改之后，自然能达到预期值。

当然，上面的代码比较简单，一眼就能看出问题所在。但是，思考下面的场景：

* 编写大量代码后，一次性验证多项功能。
   * 可能验证的功能刚好出现问题，需要在浩瀚代码中寻找问题所在，相当困难。
   * 若验证功能都顺利通过，这就埋了一个bug。

* 编写嵌入式代码，验证过程中发现问题，但是再次修改验证成本较高。
   * 编译时间成本；
   * 设备更换版本的时间成本。

**FAQ1:**

是否能在编译期间，把此类问题拦截？

当然可以。使用C++ 11新引入的override关键字对子类覆盖父类的虚函数进行修饰。编译器在编译期间，发现override关键字后，将在其继承体系的父类中，查找与之相同定义的虚函数(返回值、函数名、形参列表)。未找到，将报告编译错误。

**FAQ2:**

为什么不加override关键字，就不报告编译错误呢？

* 首先，在父类中查找与之同名的虚函数，找到则子类中的该函数同样为虚函数，可实现运行时多态。
* 其次，父类中找不到虚函数，权当在当前子类中新定义一个函数而已。

上例中，编译器会当做新定义一个成员函数而已，不会报告错误。

**意义**

* 检查是否与父类中的虚函数定义(返回值、函数名、形参列表)相同，把问题拦截在编译期间。
* 降低子类隐藏父类函数风险。
* 继承链路较长时，增加可阅读性。

**override关键字**

使用方法：

```c++
class Father {
public:
    virtual void Fun() {}
};

class Son : public Father {
public:
    void Fun() override {}
};
```

举例：

```c++
#include <vector>
#include <iostream>
using namespace std;

class Base {
public:
    virtual void Bubble()
    {
        cout << "base bubble" << endl;
    }
};

class Derive : public Base {
public:
    void Babble() override
    {
        cout << "derive bubble" << endl;
    }
};

class Foo : public Base {
public:
    void Bubble() override
    {
        cout << "Foo bubble" << endl;
    }
};

int main()
{
    Base base;
    Derive derive;
    Foo foo;
    vector<Base*> bubble = {
        &base, &derive, &foo
    };

    for (auto it : bubble) {
        it->Bubble();
    }

    return 0;
}
```

编译输出：

```c++
test.cpp:15:10: error: 'void Derive::Babble()' marked override, but does not override
     void Babble() override
          ^
The terminal process terminated with exit code: 1
```

修改代码后：

代码输出：

```c++
base bubble
derive bubble
Foo bubble
```

***

## final

