# map::operator[]的使用

```c++
std::map<Key,T,Compare,Allocator>::operator[]

T& operator[]( const Key& key );
T& operator[]( Key&& key );
```

* 用途
  * 若map中**有**key值，则返回当前key值映射的value的引用。
  * 若map中**无**key值，则向map中inert一个key-value键值对。
    * key 必须支持拷贝构造（可自定义或者使用默认的），一般数据类型不涉及。
    * value 必须支持默认构造和拷贝构造。

**划重点**

新插入的value调用**默认构造函数**初始化，一般数据类型初始化为**0**。


**疑问** 

- 为什么key要支持拷贝构造，value要支持默认构造和拷贝构造？
我们先看一下map::operator[]的[源码](https://github.com/gcc-mirror/gcc/blob/master/libstdc%2B%2B-v3/include/bits/stl_map.h)实现：

    ```c++
    typedef _Key					key_type;
    typedef _Tp					mapped_type;
    typedef std::pair<const _Key, _Tp>		value_type;

    mapped_type&
      operator[](const key_type& __k)
      {
	    // concept requirements
	    __glibcxx_function_requires(_DefaultConstructibleConcept<mapped_type>)

	    iterator __i = lower_bound(__k);
	    // __i->first is greater than or equivalent to __k.
	    if (__i == end() || key_comp()(__k, (*__i).first))
    #if __cplusplus >= 201103L
        __i = _M_t._M_emplace_hint_unique(__i, std::piecewise_construct,
					        std::tuple<const key_type&>(__k),
					        std::tuple<>());
    #else
	    __i = insert(__i, value_type(__k, mapped_type())); // ①
    #endif
	    return (*__i).second;
      }
    ```

    分析标号为①所在行的代码：
    * `mapped_type()`：即键值对的value的默认构造函数初始化，创建一个临时对象；一般数据类型(int、char、double)等同样支持int()语句，初始化临时对象值为0。
    * `value_type`：是pair的别名，是将key和value构造成一个pair。将key和value传给pair的构造函数时，调用了key和value的拷贝构造函数。

    **总结**：整个插入过程，调用一次value的默认构造，调用一次key和value的拷贝构造，调用一次pair的构造函数，最终插入到红黑树中。

***

**示例**

1. 获取含key值的value。

    ```c++
    map<char, int> asciiMap;
    for (char chr = 'a'; chr <= 'z'; chr++) {
        asciiMap.insert({chr, chr});
    }
    
    cout << asciiMap['m'] << endl;  // 输出109

    ```
2. 向map中插入一个键值对。

    ```c++
    map<char, int> charCount;
    cout << charCount['a'] << endl;  // 输出:0
    charCount['b']++;
    cout << charCount['b'] << endl;  // 输出:1
    ```

    ```c++
    map<char, vector<int>> charPos;
    charPos['a'].push_back(3);
    charPos['a'].push_back(5);
    ```
