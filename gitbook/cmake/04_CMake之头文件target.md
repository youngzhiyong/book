# CMake之头文件target

有时我们的代码功能都在头文件中实现，比如C++中的模板类及相关的成员函数定义或者简单的工具类函数。一般的library都是包含源文件(.cpp、.c)文件，因此我们要使用到[add_library](https://cmake.org/cmake/help/latest/command/add_library.html?highlight=add_library)的INTERFACE功能。

目录结构如下：

```
│  CMakeLists.txt  --- 根目录CMakeLists.txt文件①
│  main.cpp
│
└─calculator
    │  add.h
    └──CMakeLists.txt --- 模块目录CMakeLists.txt文件②
```
根目录CMakeLists.txt文件①内容如下：

```cmake
cmake_minimum_required(VERSION 3.16)

project(multi_targets VERSION 1.0.0)

set(CMAKE_CXX_COMPILER g++)

add_subdirectory(calculator) 

add_executable(multi_targets 
    main.cpp
)

target_link_libraries(multi_targets PRIVATE
    calculator_lib
)
```

main.cpp文件，与[CMake之多target](03_CMake之多target.md)内容相同。

add.h头文件内容如下：

```c++
#ifndef ADD_H
#define ADD_H

#include <cstdint>

uint64_t Add(uint32_t a, uint32_t b)
{
    return a + b;
}

#endif
```

模块目录CMakeLists.txt文件②内容如下：

```cmake
add_library(calculator_lib INTERFACE)

target_include_directories(calculator_lib
    INTERFACE  ${CMAKE_CURRENT_SOURCE_DIR}     
)
```

没有源文件，就将该target声明为interface，并指定该target的头文件所在路径为CMakeLists.txt所在的路径[CMAKE_CURRENT_SOURCE_DIR](05_CMake之CMake变量说明.md)。
