# 回溯算法Backtracking

## 什么是回溯算法？
有递归（Recursion）就有回溯（Backtracking）。相辅相成。
回溯通常出现在递归函数的下面。

二叉树在递归函数下都有回溯，有的问题用了，有的问题没有。

## 使用原因以及解决的问题
### 回溯搜索效率
纯暴力搜索，并不高效。
有些问题能暴力搜索出结果就已经不错了。

### 可解决的问题：
- 排列（Permutation）
- 组合（Combination）
- 切割（Split String）
- 子集（Subset）
- 棋盘：N皇后，数独等


## 如何理解
回溯可以抽象成树形结构，便于理解。

回溯是递归，而递归一定有终止。所以可以抽象成n叉树。
- Width：树的宽度是每个节点所处理集合的大小。通常用for loop遍历。
- Depth: 树的深度是递归来处理的，一层层向上返回。

## 模板
- 一般递归函数没有返回值。
- 除了子集问题是在每一个node节点收集结果外，其他问题在leaf节点收集结果。

```python3
def backtracking(path，choice_list, params..):
    if cond: # termination condition
        # store solution
        return

    for node in choices:
        # process node
        backtracking(path，choice_list, params..) # recursion
        # remove node
    return
```

1. 确定递归的参数和返回值 identify the params and return in backtracking
    - `result` is a reference or can be modified in-place? 
      - if reference, need to pass in as param and return
      - if can be modified in place, then no need to pass as param or return
2. 确定终止条件 identify the termination condition
   - `result = solution.copy()` 
     - need to copy one solution found (set or list), do not use `result = solution`. The latter is a reference s.t. result changes as solution adds and pops
   - `add + recursion + pop` OR just `recustion`
     - check if the solution can be reverted without add and pop. For example, `ls + [substr]` as param can be reverted to `ls` in recursion.
3. 写出单层搜索的逻辑 identify the choices at each level

