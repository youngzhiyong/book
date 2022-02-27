# CMake之多target

一个工程中，一般包含多个target库，和一个可执行程序target。

## 一个target库+一个可执行程序target

目录结构如下：

```
.
│  CMakeLists.txt   --- 根目录CMakeLists.txt文件①
│  main.cpp
│
└─calculator
    │  add.cpp
    │  CMakeLists.txt --- 模块目录CMakeLists.txt文件②
    │
    └─include
            add.h
```

根目录CMakeLists.txt文件①的内容如下：

```cmake
cmake_minimum_required(VERSION 3.16)

project(multi_targets VERSION 1.0.0)

set(CMAKE_CXX_COMPILER g++)

add_library(calculator_lib OBJECT)

add_subdirectory(calculator) 

add_executable(multi_targets 
    main.cpp
)

target_link_libraries(multi_targets PRIVATE
    calculator_lib
)
```

* [add_library](https://cmake.org/cmake/help/latest/command/add_library.html)库target类型:
  * OBJECT: 仅仅是编译源文件和包含头文件路径，而**不会**生成一个库文件target。——推荐
  * STATIC: 编译源文件和包含头文件路径，且生成一个**静态**库文件。
  * SHARED：编译源文件和包含头文件路径，且生成一个**动态**库文件。

* [target_link_libraries](https://cmake.org/cmake/help/latest/command/target_link_libraries.html)，链接以来的其他target(库)。链接时，最好采用PRIVATE方式，否则容易引起重定义问题链接时，最好采用PRIVATE方式，否则容易引起重定义问题。

模块目录CMakeLists.txt文件②内容如下：

```cmake
target_include_directories(calculator_lib
    PUBLIC include      
)

target_sources(calculator_lib
    PRIVATE add.cpp
)
```

*注：`target_sources`，最好采用PRIVATE的方式包含源文件，避免引起重定义。*

main.cpp、add.h、add.cpp等都与[CMake之单target](02_CMake之单target.md)中的内容相同。


## 多个target库+一个可执行程序target

多个target库，与单个target库类似，此处不做赘述。


