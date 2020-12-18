# 一、字典树

## 特点

1. 结点不存储值
2. 由跟结点到另一个结点的路径连起来的值为该结点的值
3. 从同一个点出发，每条路径所代表的值都能不一样


## 核心：

1. 本质上通过空间来换时间
2. 可以通过使用公共前缀来降低查询的开销以达到提高效率的目的

```javascript
# Python 代码模板
class Trie(object):
  
	def __init__(self): 
		self.root = {} 
		self.end_of_word = "#" 
 
	def insert(self, word): 
		node = self.root 
		for char in word: 
			node = node.setdefault(char, {}) 
		node[self.end_of_word] = self.end_of_word 
 
	def search(self, word): 
		node = self.root 
		for char in word: 
			if char not in node: 
				return False 
			node = node[char] 
		return self.end_of_word in node 
 
	def startsWith(self, prefix): 
		node = self.root 
		for char in prefix: 
			if char not in node: 
				return False 
			node = node[char] 
		return True
```

# 二、并查集

## 定义：

1. 建立并查集，它由多个集合组成

2. 两个群体能够合并的一个条件是不能有交集

3. 判断两个个体是否处于一个群体的方法是看看它们各自的代表是否相同

```javascript
# Python 
def init(p): 
	# for i = 0 .. n: p[i] = i; 
	p = [i for i in range(n)] 
 
def union(self, p, i, j): 
	p1 = self.parent(p, i) 
	p2 = self.parent(p, j) 
	p[p1] = p2 
 
def parent(self, p, i): 
	root = i 
	while p[root] != root: 
		root = p[root] 
	while p[i] != i: # 路径压缩 ?
		x = i; i = p[i]; p[x] = root 
	return root
```

# 三、高级搜索

## 初级搜索：DFS、BFS



## 如何变成高级搜索：

1. 优化方向：去掉重复的部分、剪枝
2. 使用新的搜索方式：双向搜索、启发式搜索

```javascript
DFS 代码模板
#Python 递归写法
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


#Python 非递归写法
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
```javascript
BFS 代码模板
# Python
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
```javascript
# Python A*
def AstarSearch(graph, start, end):
	pq = collections.priority_queue() # 优先级 —> 估价函数
	pq.append([start]) 
	visited.add(start)
	while pq: 
		node = pq.pop() # can we add more intelligence here ?
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
   unvisited = [node for node in nodes if node not in visited]
		pq.push(unvisited)
```

# 四、AVL树和红黑树的实现和特点
## AVL树

操作：
1. 平衡因子 0,1，-1，左子树高度减去右子树的高度
2. 通过旋转操作来进行平衡


## 红黑树

红黑树是一种近似平衡的二叉搜索树（Binary Search Tree），它能够确保任何一
个结点的左右子树的高度差小于两倍。具体来说，红黑树是满足如下条件的二叉
搜索树：
1. 每个结点要么是红色，要么是黑色
2. 根结点是黑色
3. 每个叶结点（NIL结点，空结点）是黑色的。
4. 不能有相邻接的两个红色结点
5. 从任一结点到其每个叶子的所有路径都包含相同数目的黑色结点
