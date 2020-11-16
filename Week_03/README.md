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
