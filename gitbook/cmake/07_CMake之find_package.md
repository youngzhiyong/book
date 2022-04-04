# CMake之find_package

通过find_package引入开源软件的库（动态或者静态库，或者仅包含头文件的库）。CMake官方，在cmake安装路径下的/share/cmake-\<version>/Modules目录中，为我们提供了许多寻找依赖包的Find\<PackageName>.cmake命名的文件。具体相关模块的介绍，可以查看[官方文档:cmake-modules](https://cmake.org/cmake/help/latest/manual/cmake-modules.7.html)。

*注：在全量源码构建时，一般不会，也不能用cmake预定义的路径下的Find\<PackageName>.cmake文件。*

由于Windows中，编写动态库，并使用动态库，代码书写比较麻烦。因此，这一章节，将在[win10 + wsl2 + Ubuntu](08_CMake之win10+WSL+Ubuntu环境搭建.md)环境下，实现相关的demo。

find_package一般支持两种查找库的方式：

* Module模式
* Config模式

## Module模式

cmake将在`CMAKE_MODULE_PATH`路径下查找`Find<PackageName>.cmake`文件。如果在Module模式下未找到，将采用Config模式继续查找`PackageName`。

**注意**

* `CMAKE_MODULE_PATH`：必须指明到`Find<PackageName>.cmake`文件所在的**具体详细的路径**。
* `find_package`函数中的`PackageName`与`Find<PackageName>.cmake`文件名中的`PackageName`保持一致。
* `find_package`函数中，最好使用`REQUIRED`参数，在未找到`PackageName`，将报告错误，提前识别构建工程中的错误。


在Module模式中，定义的`Find<PackageName>.cmake`文件内容，需要定义以下几个变量：

* `<PackageName>_FOUND`: bool值，表示当前`PackageName`是否已找到。
* `<PackageName>_INCLUDE_DIR`或者`<PackageName>_INCLUDES`: 表示当前对外提供的头文件接口所在的头文件目录。
* `<PackageName>_LIBRARIES`或者`<PackageName>_LIBRARY`:表示提供的动态库集合。

当然，在`Find<PackageName>.cmake`文件中的几个变量，可另起他名，但在使用时，就不太方便。因此，还是建议使用约定俗成的变量名称。

### 示例
整个目录结构如下：

```cmd
.
├── CMakeLists.txt
├── opensource
│   └── calculator
│       ├── CMakeLists.txt
│       ├── FindCalculator.cmake
│       ├── add.cpp
│       └── include
│           └── add.h
└── src
    ├── CMakeLists.txt
    └── main.cpp
```

各个cpp文件和头文件与之前相同，其他的CMakeLists.txt和cmake文件将一一列举。

`./CMakeLists.txt`文件内容：

```cmake
cmake_minimum_required(VERSION 3.16)

project(find_package_demo VERSION 1.0.0)

set(CMAKE_CXX_COMPILER g++)

add_subdirectory(src) 
```

`./src/CMakeLists.txt`文件内容：

```cmake
# 查找开源动态库 Calculator
set(CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/output/calculator/lib/cmake)
message(STATUS ${CMAKE_MODULE_PATH})
find_package(Calculator REQUIRED)

set(CMAKE_BUILD_TYPE "Debug")
set(CMAKE_CXX_FLAGS "-g")

add_executable(find_package_demo 
    main.cpp
)

target_link_libraries(find_package_demo PRIVATE
    ${Calculator_LIBRARY}
)

# install 可执行程序，到 CMAKE_INSTALL_PREFIX/bin目录下
install(TARGETS find_package_demo
    RUNTIME DESTINATION bin
)
```

`./opensource/calculator/CMakeFiles.txt`文件内容：

```cmake
cmake_minimum_required(VERSION 3.16)

project(calculator VERSION 1.0.0)

set(CMAKE_BUILD_TYPE "Debug")
# 添加下面的编译选项，在Linux环境下，三方动态库支持调试
set(CMAKE_CXX_FLAGS "-g -rdynamic")

add_library(calculator SHARED)

target_include_directories(calculator
    PUBLIC include     
)

target_sources(calculator
    PRIVATE add.cpp
)

# install 整个include目录到 CMAKE_INSTALL_PREFIX目录
install(DIRECTORY include
    DESTINATION ${CMAKE_INSTALL_PREFIX}
)

# install 动态库到 CMAKE_INSTALL_PREFIX/lib目录下
install(TARGETS calculator
    LIBRARY DESTINATION lib 
)

# install FindCalculaor.cmake到 CMAKE_INSTALL_PREFIX/lib/cmake目录下
install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/FindCalculator.cmake
    DESTINATION lib/cmake
)
```

`./opensource/calculator/FindCalculator.cmake`文件内容：

```cmake
get_filename_component(Calculator_BASE "${CMAKE_CURRENT_LIST_DIR}/../.." ABSOLUTE)

set(Calculator_INCLUDE ${Calculator_BASE}/include)
set(Calculator_LIBRARY "Calculator::Add")   # 多个库，均可在列表中包含
set(Calculator_VERSION "v0.0.1")

add_library(Calculator::Add SHARED IMPORTED)
set_target_properties(Calculator::Add PROPERTIES
    INTERFACE_INCLUDE_DIRECTORIES ${Calculator_BASE}/include 
    IMPORTED_LOCATION ${Calculator_BASE}/lib/libcalculator.so 
)

set(Calculator_FOUND true)

# 下列纯属打印，以便在使用find_package后，能证实该库已找到
message(STATUS "Calculator_INCLUDE = ${Calculator_INCLUDE}")
message(STATUS "Calculator_LIBRARY = ${Calculator_LIBRARY}")
message(STATUS "Calculator_VERSION = ${Calculator_VERSION}")
```

开源软件构建命令如下：

```
mkdir -p build/calculator && cd build/calculator/
cmake ../../opensource/calculator/ -DCMAKE_INSTALL_PREFIX=../../output/calculator
make -j  # 多线程构建
make install
```

calculator安装在output目录下的结果如下：

```
output/
└── calculator
    ├── include
    │   └── add.h
    └── lib
        ├── cmake
        │   └── FindCalculator.cmake
        └── libcalculator.so
```

再构建自研代码，命令如下：

```
mkdir -p build/src && cd build/src
cmake ../../ -DCMAKE_INSTALL_PREFIX=../../output/src
make -j
make install
```

最终，生成可执行程序后，output目录的结构如下：

```
output/
├── calculator
│   ├── include
│   │   └── add.h
│   └── lib
│       ├── cmake
│       │   └── FindCalculator.cmake
│       └── libcalculator.so
└── src
    └── bin
        └── find_package_demo
```

需要将`libcalculator.so`库所在路径，追加到`LD_LIBRARY_PATH`环境变量，然后才能执行被`install`后的`find_package_demo`程序，其原因有两点：

* 因为此处我们的开源库，是以SHARED动态库的方式提供
* 一旦程序被install后，可执行程序中的rpath路径被去掉，导致程序不可以直接找到相应的动态库。(可使用`ldd  find_package_demo`命令对比查看安装前后的区别)

*注：在执行install前，build/src目录中`find_package_demo`程序是可直接运行的。*

当然，我们也可以使用开源库的静态库方式，这样可执行程序将静态库链接到可执行程序中。其改动为：

* CMakeLists.txt中的`SHARED`->`STATIC`；
* FindCalculator.cmake中的`SHARED`->`STATIC`；
* FindCalculator.cmake的`libcalculator.so`->`libcalculator.a`

不过，我们一般不采用静态库方式。因为：

* 静态库是直接链接到可执行程序中，使得可执行程序可独立运行。但是，这将增加可执行程序文件大小。如果很多可执行程序，都依赖此静态库，那所有可执行程序中，都包含此静态库的内容。动态库，仅链接，不将动态库的内容合入到可执行程序文件。因此，多个依赖此动态库可执行程序，仅依赖一个动态库文件。
* 静态库被包含在可执行程序中，有多个可执行程序运行实例，将存在多个静态库的实例；动态库，仅仅在内存中只有一份代码实例(动态库中定义的数据，多个可执行程序在内存中各自独立一份)，可被多个可执行程序共用。
* 相比静态库，使用动态库方式，在处理开源软件使用的开源协议时，更具有灵活性。


## Config模式

Config模式下，相对于Module模式，支持仅提供搜索的起始目录，CMake可进行递归的进行搜索`<lowercasePackageName>-config.cmake`或者`<PackageName>Config.cmake`文件的功能。搜索的路径，可参考[CMake官网find_package的Config Mode Search Procedure小节](https://cmake.org/cmake/help/latest/command/find_package.html#search-procedure)。

Config模式下，搜索路径的指定，一般常用如下：

* `<PackageName>_ROOT`：只需提供给搜索根目录即可，详情请参考官网[\<PackageName>_ROOT](https://cmake.org/cmake/help/latest/envvar/PackageName_ROOT.html#envvar:%3CPackageName%3E_ROOT)

* `CMAKE_PREFIX_PATH`：只需提供给搜索根目录即可，详情参考官网[CMAKE_PREFIX_PATH](https://cmake.org/cmake/help/latest/envvar/CMAKE_PREFIX_PATH.html#envvar:CMAKE_PREFIX_PATH)

* `<PackageName>_DIR`：需要精确指出`<lowercasePackageName>-config.cmake`或者`<PackageName>Config.cmake`文件的位置。

**注意：**

* 强制使用config模式，需要在`find_package`时，带上`CONFIG`参数。
* 使用递归搜索的功能，需要按照[CMake官网find_package的Config Mode Search Procedure小节](https://cmake.org/cmake/help/latest/command/find_package.html#search-procedure)支持的文件位置，存放`<lowercasePackageName>-config.cmake`或者`<PackageName>Config.cmake`文件。



### 示例

整个目录结构与Module模式小节类似，只是将`FindCalculator.cmake`文件，替换成`CalculatorConfig.cmake`文件，相应的`CMakeLists.txt`文档，做少许变更。

```shell
.
├── CMakeLists.txt
├── opensource
│   └── calculator
│       ├── CMakeLists.txt
│       ├── CalculatorConfig.cmake
│       ├── add.cpp
│       └── include
│           └── add.h
└── src
    ├── CMakeLists.txt
    └── main.cpp
```

`./opensource/calculator/CMakeFiles.txt`文件内容少许变更：

**将**

```cmake
# install FindCalculaor.cmake到 CMAKE_INSTALL_PREFIX/lib/cmake目录下
install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/FindCalculator.cmake
    DESTINATION lib/cmake
)
```

**变更为：**

```cmake
# install CalculatorConfig.cmake到 CMAKE_INSTALL_PREFIX/cmake目录下
install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/CalculatorConfig.cmake
    DESTINATION cmake
)
```

`./opensource/calculator/CalculatorConfig.cmake`文件，是将原来的`./opensource/calculator/FindCalculator.cmake`文件重命名，并因`CalculatorConfig.cmake`文件安装路径变更，做相应改动：

**将**

```cmake
get_filename_component(Calculator_BASE "${CMAKE_CURRENT_LIST_DIR}/../.." ABSOLUTE)
```

**变更为：**

```cmake
get_filename_component(Calculator_BASE "${CMAKE_CURRENT_LIST_DIR}/.." ABSOLUTE)
```

使用前面提供的opensource的构建命令，构建后，output目录结构如下：

```shell
.
└── calculator
    ├── cmake
    │   └── CalculatorConfig.cmake
    ├── include
    │   └── add.h
    └── lib
        └── libcalculator.so
```

因为config模式，支持查找`<PackageName>_ROOT`目录和子目录下的`CalculatorConfig.cmake`文件。

`./src/CMakeLists.txt`文件内容：

**将**

```cmake
# 查找开源动态库 Calculator
set(CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/output/calculator/lib/cmake)
message(STATUS ${CMAKE_MODULE_PATH})
find_package(Calculator REQUIRED)
```

**变更为**

```cmake
# 查找开源动态库 Calculator
set(Calculator_ROOT ${CMAKE_SOURCE_DIR}/output)
message(STATUS "Calculator_ROOT=${Calculator_ROOT}")
find_package(Calculator CONFIG REQUIRED)
```

使用前面的提供的自研代码构建脚本，完成构建，最终的output目录结构如下：

```shell
.
├── calculator
│   ├── cmake
│   │   └── CalculatorConfig.cmake
│   ├── include
│   │   └── add.h
│   └── lib
│   │   └── libcalculator.so
└── src
    └── bin
        └── find_package_demo
```
