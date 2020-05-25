# vector其他操作

## 容量

```c++
bool empty() const;
size_type size() const;
size_type max_size() const;
void reserve(size_type new_cap);
size_type capacity() const;

void resize(size_type count);
void resize(size_type count, const value_type& value);
```

* empty:判定vector容器中是否为空。
* size:获取容器中当前**元素个数**。
* max_size:获取容器能存放当前类型元素最大个数,取决于系统和库代码的实现。
* **reserve**:大致得知容器即将存储的元素个数时，通过reserve**预分配存储空间**，减少新增元素过程中的频繁申请、释放内存动作，提高运行效率。reserve，增大capacity，对size和max_size无影响。
* capacity:获取当前已分配存储空间能容纳元素的个数。
* resize:count比当前容器中元素小，将缩减容器大小，保证从前往后数count个元素；count比当前容器大，则可使用value为其填充新增，亦可采用默认值填充。


## vector比较——非vector成员函数

