# CMake之win10+WSL+Ubuntu环境搭建

整个安装步骤分为：

* Win10中开启WSL功能
* 下载并安装Ubuntu系统
* 配置Ubuntu源
* 开发工具安装

## Win10中开启WSL功能

这一步骤，网上有很多介绍，此处不做一一介绍。只是在开启WSL功能后，需要安装[WSL2 Linux kernel update package for x64 machines](https://docs.microsoft.com/en-us/windows/wsl/install-manual#downloading-distros)。

## 下载并安装Ubuntu系统

**下载**

网上很多提供的是在Windows的应用商店下载ubuntu。应用商店中，需要注册账号，且受限于国外网站网速。此处，提供不在应用商店下载的网址，请查看[微软官方文档](https://docs.microsoft.com/en-us/)，查找路径：搜索"WSL"->搜索结果选择"Install WSL"->选择"Manual installation steps for older versions"章节的"Downloading distributions"小节]。亦可乘坐[直达列车](https://docs.microsoft.com/en-us/windows/wsl/install-manual#downloading-distros)到达。

*注：确定版本后，复制相应版本链接，推荐使用迅雷下载，相比浏览器直接下载，简直天壤之别。*

**安装**

以Ubuntu20.04为例：

将下载完成的文件，增加`.zip`后缀，解压缩文件。并将`Ubuntu_2004.2021.825.0_x64.appxa`的将`appx`后缀，更改为`zip`后缀，解压到软件安装路径。

执行解压后的ubuntu.exe文件，就可进入Ubuntu系统。


## 配置Ubuntu源

此处推荐，使用[华为云镜像](https://mirrors.huaweicloud.com/home)提供的源。

* 进入华为云镜像，搜索Ubuntu
* 选择相应版本的Ubuntu，根据指导配置相应的镜像源。

此处，直接将华为云镜像中，提供的步骤列出：

> 1、备份配置文件：
> ```shell
> sudo cp -a /etc/apt/sources.list /etc/apt/sources.list.bak
> ```
> 2、修改sources.list文件，将http://archive.ubuntu.com和http://security.ubuntu.com替换成http://repo.huaweicloud.com，可以参考如下命令：
> ```shell
> sudo sed -i "s@http://.*archive.ubuntu.com@http://repo.huaweicloud.com@g" /etc/apt/sources.list
> sudo sed -i "s@http://.*security.ubuntu.com@http://repo.huaweicloud.com@g" /etc/apt/sources.list
> ```
> 3、执行`apt-get update`更新索引


## 开发工具安装

**Ubuntu**

```shell
sudo apt install gcc g++ cmake
```

**Windows**

安装VScode，并在VScode中安装可以连接WSL Ubuntu的`Remote - WSL`插件和支持C/C++开发的插件`C/C++`，`CMake`。
