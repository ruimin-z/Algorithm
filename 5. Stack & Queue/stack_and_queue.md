# 栈与队列 Stack and Queue




## 1. 基础知识


```
以下是以C++为例，使用其他编程语言的同学也对应思考一下，自己使用的编程语言里栈和队列是什么样的。

1. C++中stack 是容器么？
2. 我们使用的stack是属于哪个版本的STL？
3. 我们使用的STL中stack是如何实现的？
4. stack 提供迭代器来遍历stack空间么？
```


```text
首先大家要知道 栈和队列是STL（C++标准库）里面的两个数据结构。

C++标准库是有多个版本的，要知道我们使用的STL是哪个版本，才能知道对应的栈和队列的实现原理。

那么来介绍一下，三个最为普遍的STL版本：

1. HP STL 其他版本的C++ STL，一般是以HP STL为蓝本实现出来的，HP STL是C++ STL的第一个实现版本，而且开放源代码。

2. P.J.Plauger STL 由P.J.Plauger参照HP STL实现出来的，被Visual C++编译器所采用，不是开源的。

3. SGI STL 由Silicon Graphics Computer Systems公司参照HP STL实现，被Linux的C++编译器GCC所采用，SGI STL是开源软件，源码可读性甚高。

接下来介绍的栈和队列也是SGI STL里面的数据结构， 知道了使用版本，才知道对应的底层实现。
```


```text
栈提供push 和 pop 等等接口，所有元素必须符合先进后出规则，所以栈不提供走访功能，也不提供迭代器(iterator)。 不像是set 或者map 提供迭代器iterator来遍历所有元素。

栈是以底层容器完成其所有的工作，对外提供统一的接口，底层容器是可插拔的（也就是说我们可以控制使用哪种容器来实现栈的功能）。

所以STL中栈往往不被归类为容器，而被归类为container adapter（容器适配器）。

那么问题来了，STL 中栈是用什么容器实现的？

从下图中可以看出，栈的内部结构，栈的底层实现可以是vector，deque，list 都是可以的， 主要就是数组和链表的底层实现。
```




## 2. 题型


## 3. 思路




## 4.题目

### 4.1 Basics

#### [232. Implement Queue using Stacks用栈实现队列](https://leetcode.com/problems/implement-queue-using-stacks/description/)


#### [225. Implement Stack using Queues用队列实现栈](https://leetcode.com/problems/implement-stack-using-queues/)


### 4.2 Statck Applications
#### [20. Valid Parentheses有效的括号](https://leetcode.com/problems/valid-parentheses/description/) - Easy

#### [1047. Remove All Adjacent Duplicates In String删除字符串中的所有相邻重复项 ](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/) - Easy

#### [150. Evaluate Reverse Polish Notation逆波兰表达式求值](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/) - Medium


### 4.3 Queue Application

#### [239. Sliding Window Maximum滑动窗口最大值](https://leetcode.com/problems/sliding-window-maximum/description/) - Hard


#### [347. Top K Frequent Elements前K个高频元素](https://leetcode.com/problems/top-k-frequent-elements/description/) - Medium



## 5. 总结



