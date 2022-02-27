# 多文件单target

在平常写C++工程代码时，不止一个源文件，而是多个源文件和头文件组成。在此节中，借助简单的C++代码，简要介绍CMake单Target的场景。

[TOC]

## 单文件单target

main.cpp文件

```c++
#include <cstdint>
#include <iostream>

uint64_t Add(uint32_t a, uint32_t b)
{
    return a + b;
}

int main()
{
    auto result = Add(2, 3);
    std::cout << result << std::endl;
    return 0;
}
```

CMakeLists.txt文件：

```CMake
cmake_minimum_required(VERSION 3.16)

project(single_target VERSION 1.0.0)

add_compile_options("-std=c++11")

add_executable(single_target main.cpp)

```

构建命令：

```shell
mkdir build && cd build     # build目录中构建，避免污染源码
cmake .. -G"MinGW Makefiles" # Linux系统下，无需-G参数
make -j
```

## 多文件单target

在平常工作中，不可能所有的功能，都堆砌在main.cpp文件。因此，需要根据功能将各功能代码划分不同的模块。

add.h头文件

```c++
#include <cstdint>

uint64_t Add(uint32_t a, uint32_t b);
```

add.cpp源文件

```c++
#include "add.h"

uint64_t Add(uint32_t a, uint32_t b)
{
    return a + b;
}
```

main.cpp源文件

```c++
#include <iostream>
#include "add.h"

int main()
{
    auto result = Add(2, 3);
    std::cout << result << std::endl;
    return 0;
}
```

CMakeLists.txt文件

```cmake
cmake_minimum_required(VERSION 3.16)

project(multi_file_single_target VERSION 1.0.0)

set(CMAKE_CXX_COMPILER g++)

add_executable(multi_file_single_target 
    add.cpp
    main.cpp
)
```

工程构建命令，与前述小节相同，此处不再赘述。

## 多文件多目录单target

上一节，是将所有的文件都平铺在一个目录。一般开发过程中，都会根据不同模块，划分不同目录。

最简单的目录结构如下：

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

根目录CMakeLists.txt文件①内容如下：

```cmake
cmake_minimum_required(VERSION 3.16)

project(multi_file_single_target VERSION 1.0.0)

set(CMAKE_CXX_COMPILER g++)

add_executable(multi_file_single_target 
    main.cpp
)

# 整个工程是单个target，因此该步骤位于add_executable之后
add_subdirectory(calculator) 
```

模块目录CMakeLists.txt文件②内容如下：

```cmake
target_include_directories(multi_file_single_target
    PUBLIC include      
)

target_sources(multi_file_single_target
    PRIVATE add.cpp
)
```

其中，main.cpp、add.h和add.cpp等文件，所在路径与之前不同，但内容和前一小节是一样的，此处不在赘述。

工程构建命令，与前述小节相同，此处不再赘述。

