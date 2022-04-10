# CMake之add_custom_target

在CMake中，用于定义用户target的函数，且不生成该target对应的文件。在该target中，可以执行相应的用户命令，即命令行下的shell命令，比如可以调用`cmake`，`python`和Linux下常用的终端命令行命令。

```cmake
add_custom_target(Name [ALL] [command1 [args1...]]
                  [COMMAND command2 [args2...] ...]
                  [DEPENDS depend depend depend ... ]
                  [BYPRODUCTS [files...]]
                  [WORKING_DIRECTORY dir]
                  [COMMENT comment]
                  [JOB_POOL job_pool]
                  [VERBATIM] [USES_TERMINAL]
                  [COMMAND_EXPAND_LISTS]
                  [SOURCES src1 [src2...]])
```

其中，较为常用的为：COMMAND、DEPENDS、WORKING_DIRECTORY和COMMENT。

示例：

```cmake
cmake_minimum_required(VERSION 3.16)

project(add_custorm_target_demo VERSION 1.0.0)

add_custom_target(ls_target 
    COMMAND "ls" "-al"
    WORKING_DIRECTORY "/home"
    COMMENT "${WORKING_DIRECTORY} exe ls -al"
)

add_custom_target(pwd_target 
    COMMAND "pwd"
    DEPENDS ls_target
    COMMENT "show current directory!"
)

add_custom_target(cd_target 
    COMMAND "cd" ${CMAKE_SOURCE_DIR}
    DEPENDS pwd_target
    COMMENT "change dir from /home to ${CMAKE_SOURCE_DIR}"
)
```

在命令行中，执行如下命令：

```shell
mkdir build && cd build
cmake ..
make cd_target
```

target间的依赖顺序是：`cd_target`->`pwd_target`->`ls_target`
构建顺序是：`ls_target`->`pwd_target`->`cd_target`


使用add_custorm_target，可以将各个开源软件的构建，纳入到CMake构建工程中。但，在介绍此功能前，先了解直接使用shell脚本完成开源软件和自研代码的构建。

后续两个章节，都是使用[CMake之find_package](07_CMake之find_package.md)章节中的Module模式中的例子做讲解。

## shell脚本构建开源和自研软件

其实，对于使用shell脚本组织，就非常的简单。就是，将例子中的各个shell命令，都整合到一个shell脚本文件即可。例如：

`./build.sh`一键构建脚本文件

```shell
# 构建开源软件
#!/usr/bin/env bash

mkdir -p build/calculator && cd build/calculator/
cmake ../../opensource/calculator/ -DCMAKE_INSTALL_PREFIX=../../output/calculator
make install -j  # 多线程构建

# 构建自研软件
mkdir -p build/src && cd build/src
cmake ../../ -DCMAKE_INSTALL_PREFIX=../../output/src
make install -j
```

**优点：** 脚本简单直接

**缺点：** 
> * 每次构建，所有开源软件都需构建一次。
> * 如果开源软件引入较多，或某个开源软件构建时间比较长，那么项目上势必影响工作效率。
> * 各个开源软件构建脚本未整合到CMAKE构建系统中，IDE工具(比如CLion、VSCode)无法使用CMAKE直接构建整个工程，或者选择某个target构建。


## add_custom_target连接开源软件和自研软件构建

a. 将build.sh文件中，开源软件的构建部分，提取到build_calculator.sh文件中。

b. `./src/CMakeLists.txt`文件内容修改为如下内容：

```cmake
add_custom_target(build_calculator
    COMMAND "bash" "build_calculator.sh"    # 构建开源软件命令
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}   # 执行构建的工作目录
    COMMENT "start build build_calculator target!"  # 执行 bash build_calculater.sh 命令前的提示信息
)

if (EXISTS "${CMAKE_SOURCE_DIR}/output/calculator/lib/cmake")
    # 如果存在开源软件安装完成cmake文件(FindCalculater.cmake)，不执行任何命令，仅提示和保证后续流程归一化，需包含`phony_build_calculator` 伪target。
    add_custom_target(phony_build_calculator
        COMMAND "echo" ">/dev/null" # 回显空，到/dev/null中，仅仅为了COMMENT中的内容能显示
        COMMENT "not need to build build_calculator target!"
    )
else()
    # 如果开源软件未安装
    # 1. 扫描出依赖：build_calculator，即生成build_calculator target
    # 2. 构建完依赖的target后，需要在相应目录，再次执行CMAKE命令
    # 注意 需要指定，执行`${CMAKE_COMMAND} ${CMAKE_SOURCE_DIR}`命令的工作目录，${CMAKE_COMMAND} ${CMAKE_SOURCE_DIR}`
    add_custom_target(phony_build_calculator
        COMMAND ${CMAKE_COMMAND} ${CMAKE_SOURCE_DIR}    # 再次执行CMAKE命令
        DEPENDS build_calculator
        WORKING_DIRECTORY ${CMAKE_BINARY_DIR}   # 指定为构建目录
        COMMENT "built build_calculator custom target, re-execute cmake command!"
    )
endif()

# 查找开源动态库 Calculator
if (EXISTS "${CMAKE_SOURCE_DIR}/output/calculator/lib/cmake")
    set(CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/output/calculator/lib/cmake)
    find_package(Calculator REQUIRED)
endif()

set(CMAKE_BUILD_TYPE "Debug")
set(CMAKE_CXX_FLAGS "-g")

add_executable(find_package_demo 
    main.cpp
)

add_dependencies(find_package_demo phony_build_calculator)  # 添加find_package_demo和phony_build_calculator依赖关系。
if (${Calculator_FOUND}) # 找到了才能够链接，未找到不能执行target_link_libraries，否则容易引起构建错误。
    # 开源软件构建完成后，Calculator_LIBRARY包含头文件目录属性和相应动态库。无需额外提供头文件目录。
    target_link_libraries(find_package_demo PUBLIC
        ${Calculator_LIBRARY}
    )
endif()

# install 可执行程序，到 CMAKE_INSTALL_PREFIX/bin目录下
install(TARGETS find_package_demo
    RUNTIME DESTINATION bin
)
```

使用add_custom_target后，可以将所有开源软件与自研代码，都纳入到CMAKE构建系统，IDE能很好的构建指定的target。

## 扩展

如果开源软件较多，每个开源软件都按照上述的代码实现，那将是冗长且多余的。可以考虑使用python代码生成相关代码：

* 提供一个json文件，包含各个开源软件包名、库名、支持`find_package`相关的路径、包名_FOUND等配置。
* 提供公共部分的CMAKE代码模板，涉及多个开源软件，因此需使用循环语句。
* python生成的CMAKE代码，更多的是设置每一个开源软件构建时的CMAKE变量。
