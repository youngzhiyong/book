# CMake之Hello

使用CMake基于CMakeLists.txt文件生成为hello.cpp构建的Makefile文件，并基于此Makefile文件，构建生成相应的可执行程序。

## 代码及CMake脚本编写

hello.cpp文件内容：

```c++
#include <iostream>

using namespace std;

int main()
{
    std::cout << "hello cmake!" << std::endl;

    return 0;
}
```

CMakeLists.txt文件内容：

```cmake
cmake_minimum_required(VERSION 3.16)    # 指定使用CMake的最小版本

project(cmake_hello VERSION 1.0.0)  # 工程cmake_hello的版本号

add_compile_options("-Wall")    # 指定工程的编译选项

add_executable(hello hello.cpp) # 使用提供的源文件（可以是多个），生成可执行程序hello。

```

## 构建

笔者当前仅使用了win10，因此以win10作为构建时的操作系统。

**准备**
下载安装以下工具：
* [MinGW](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/8.1.0/threads-posix/sjlj/x86_64-8.1.0-release-posix-sjlj-rt_v6-rev0.7z)
* [CMake](https://cmake.org/download/)

*建议：工具下载时，复制链接，使用迅雷工具下载，速度会更快。*

**生成Makefile文件和构建生成可执行程序**

在hello.cpp和CMakeLists.txt文件所在路径下执行如下命令：

```shell
mkdir build && cd build     # 创建build构建目录，避免污染源码
cmake .. -G"MinGW Makefiles"  # 在Linux中，无需使用-G命令参数。
make -j     # -j表示可多个任务job，并行构建相互独立的target
```

此时，已经在build目录下生成`hello.exe`可执行程序。
