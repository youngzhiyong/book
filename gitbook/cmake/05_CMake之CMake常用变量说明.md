# CMake之CMake变量说明

1. CMAKE_SOURCE_DIR：整个CMake工程最顶层的CMakeLists.txt文件所在路径。
2. CMAKE_CURRENT_SOURCE_DIR：当前CMakeLists.txt文件所在路径。
3. CMAKE_CURRENT_LIST_DIR：当前*.cmake文件所在路径。
4. CMAKE_CURRENT_BINARY_DIR：构建当前CMakeLists.txt文件所在路径。
5. CMAKE_INSTALL_PREFIX：执行make install命令时安装的根目录的路径。
6. CMAKE_MODULE_PATH：find_package的module模式时，Find\<PackageName>.cmake文件所在路径。
7. CMAKE_PREFIX_PATH: CMake的环境变量，存放CMake的搜索路径列表，可提供给find_package(), find_program(), find_library(), find_file(), 和find_path()等函数使用。
