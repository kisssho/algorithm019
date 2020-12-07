# 一、动态规划

## 代码本质上是寻找重复性

1. 人脑递归低效、很累
2. 找到最近最简方法，将其拆解成可重复解决的问题
3. 数学归纳法思维（抵制人肉递归的诱惑）



## 递归、分治、动态规划都是递归

动态规划（Dynamic programming） = 分治 + 最优子结构

动态规划和递归或者分治没有根本上的区别（关键看有无最优的子结构）

共性：找到重复子问题

差异性：最优子结构、中途可以淘汰次优解




```javascript
# Python 递归模板
def recursion(level, param1, param2, ...): 
    # recursion terminator 
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level 
    process(level, data...) 
    # drill down 
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed
```

```javascript
# Python 分治模板
def divide_conquer(problem, param1, param2, ...): 
	# recursion terminator 
	 if problem is None: 
	print_result 
	return 
	
	 # prepare data 
	 data = prepare_data(problem) 
	 subproblems = split_problem(problem, data) 
	
	 # conquer subproblems 
	 subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
	 subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
	 subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
	 …
	
	 # process and generate the final result 
	 result = process_result(subresult1, subresult2, subresult3, …)
	
	 # revert the current level states
```
