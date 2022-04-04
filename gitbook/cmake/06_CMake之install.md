# CMake之install

将生成的库、可执行程序和相关接口头文件发布出去，install到固定的目录。其中，install的所有安装根目录，均是以`CMAKE_INSTALL_PREFIX`变量所表示的目录作为根目录。

详细的install介绍，可去[CMake官网](https://cmake.org/cmake/help/latest/search.html?q=)搜索。

对于我们最常用的，主要是以下几种形式：

```cmake
install(TARGETS <target>... [...])
install({FILES | PROGRAMS} <file>... [...])
install(DIRECTORY <dir>... [...])
```

同样以之前的代码工程为例，简要介绍几种install的用法

代码工程目录结构：

```
.
│  CMakeLists.txt   --- 根目录CMakeLists.txt文件①
│  config.json
│  main.cpp
│
└─calculator
    │  add.cpp
    │  CMakeLists.txt --- 模块目录CMakeLists.txt文件②
    │
    └─include
            add.h
```

其中，main.cpp、add.cpp、add.h和模块目录CMakeLists.txt文件②的内容，和[CMake之多target](03_CMake之多target.md)章节相同。config.json文件内容为空，仅仅用于示例需求。

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

# install 可执行程序到 CMAKE_INSTALL_PREFIX/bin目录下
install(TARGETS multi_targets
    RUNTIME DESTINATION bin
)

# install 动态库到 CMAKE_INSTALL_PREFIX/lib目录下
install(TARGETS calculator_lib
    LIBRARY DESTINATION lib 
)

# install 配置文安装件到 CMAKE_INSTALL_PREFIX/config目录下
install(FILES config.json
    DESTINATION config
)

# install 整个include目录到 CMAKE_INSTALL_PREFIX目录下
install(DIRECTORY calculator/include
    DESTINATION ${CMAKE_INSTALL_PREFIX}
)
```
