学习笔记

# 一、递归的实现、特性以及思维要点


递归本身就类似于循环，都是找到问题的重复性。

做题格式：

```javascript
def recurion(level,param1,param2,...):

	#recursion terminator
	if level>MAX_LEVEL:
		process_result
		return

	#process logic in current level
	process(level,data...)

	#drill down
	self.recursion(level+l,p1,...)

	#reverse the current level status if needed
```

注意事项：

1. 不要人肉进行递归（最大误区）
2. 找到最近最简方法，将其拆解成可重复解决的问题（重复子问题）
3. 数学归纳法思维
# 二、分治、回溯的实现和特性

分治和回溯属于递归的特殊情况。无论分治，回溯还是递归，都是找重复性


```javascript
def divide_conquer(problem,param1,param2,...):
	# recursion terminator
	if problem is None:
	print_result
	return
	# prepare data
	data = prepare_data(problem)
	subproblems = split_problem(problem,data)
	
	#conquer subproblems
	subresult1 = self.divide_conquer(subproblems[0],p1,...)
	subresult2 = self.divide_conquer(subproblems[1],p1,...)
	subresult3 = self.divide_conquer(subproblems[2],p1,...)
	...
	# process and generate the final result
	result = process_result(subresult1,subresult2,subresult3,...)
```


回溯法采用试错的思想，它尝试分布的去解决一个问题。在分布解决问题的过程中，当它通过尝试发现现有的分布答案不能得到有效的正确的解答时，它将取消上一步甚至是上几步的计算，再通过其它的可能的分布解答再次尝试寻找问题的答案

回溯法通常用最简单的递归方法来实现，在反复重复上述的步骤后可能出现两种情况：

1. 找到一个可能存在的正确的答案；
2. 在尝试了所有可能的分步方法后宣告该问题没有答案。
