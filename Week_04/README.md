课堂笔记


# 一、深度优先搜索、广度优先搜索的实现和特性


简单的搜索本质上和遍历是一回事，都要访问所有的节点，且需要保证每个节点仅访问一次，时间复杂度是O（n）


深度优先搜索可以通过递归和栈两种方式实现：


递归模板：

```javascript
visited = []
def recursion(root):
    if root:
       if root in visited:
          return
       visited.append(root)
       for node in root.childrens:
           recursion(node)
```

```javascript
#Python
visited = set() 

def dfs(node, visited):
    if node in visited: # terminator
    	# already visited 
    	return 

	visited.add(node) 

	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)
```

栈模板：


```javascript
visited,stack = [],[root]

def dfs(root):
    while stack:
          tmp = stack.pop()
          visited.append(tmp)
          for node in tmp.childrens:
              stack.push(node)
```

```javascript
#Python
def DFS(self, tree): 

	if tree.root is None: 
		return [] 

	visited, stack = [], [tree.root]

	while stack: 
		node = stack.pop() 
		visited.add(node)

		process (node) 
		nodes = generate_related_nodes(node) 
		stack.push(nodes) 

	# other processing work 
	...
```


广度优先搜索是逐层进行遍历的方法：

队列模板：

```javascript
visited,queue = [],[root]

def bfs(root):
    while queue:
          tmp = queue.popleft()
          visited.add(tmp)
          for node in tmp.childrens:
              queue.push(node)
```


```javascript
#Python
def BFS(graph, start, end):
    visited = set()
	queue = [] 
	queue.append([start]) 
	while queue: 
		node = queue.pop() 
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
		queue.push(nodes)
	# other processing work 
	...
```

# 二、贪心算法的实现和特性


贪心算法是一种在每一步选择中都采取在当前状态下最好或最优（即最有利）的选择，从而希望导致结果是全局最好或最优的算法


贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退。动态规划则会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能

贪心：当下做局部最优判断，不会回退
回溯：能够回退
动态规划：最优判断 + 回退


一旦一个问题可以通过贪心法来解决，那么贪心法一般是解决这个问题的最好办法。



# 三、二分查找的实现、特性


二分查找的前提：

1. 目标函数单调性

2. 存在上下界

3. 能够通过索引访问


代码模板：

```javascript
left,right = 0,len(array)-1
while left<=right:
      mid = (left+right)/2
      if array[mid] == target:
         return result or break
      elif array[mid] < target:
         left = mid + 1
      else:
         right = mid + 1
```

