# 一、位运算
含义    | 运算符
-------- | -----
左移 |  <<
右移 |  >>
与 | & 
或 |  /
非 | ~
异或 |  ^

异或

x ^ 0 = x
x ^ 1s = ~x
x ^ (~x) = 1s
x ^ x = 0
c = a ^ b , a = c ^ b ,  b = a ^ c
a ^ b ^ c = a ^ c ^ b = c ^ b ^ a


指定位置的位运算

1. 将 x 最右边的 n 位清零：x & (~0 << n)
2. 获取 x 的第 n 位值（0 或者 1）：(x >> n) & 1
3. 获取 x 的第 n 位的幂值：(1 << n) & x
4. 仅将第 n 位置为 1：x | (1 << n)
5. 仅将第 n 位置为 0：x & ~(1 << n)
6. 将 x 最高位至第 n 位（含）清零：~(1s << n) & x 或 ((1 << n) - 1) & x


位运算要点：


1. 判断奇偶：
x % 2 == 1 —> (x & 1) == 1
x % 2 == 0 —> (x & 1) == 0
2. x >> 1 —> x / 2.
即： x = x / 2; —> x = x >> 1;
mid = (left + right) / 2; —> mid = (left + right) >> 1;
3. X = X & (X-1) 清零最低位的 1
4. X & -X => 得到最低位的 1
5. X & ~X => 0

# 二、布隆过滤器


## Bloom Filter vs Hash Table

一个很长的二进制向量和一系列随机映射函数。布隆过滤器可以用于检索
一个元素是否在一个集合中。
优点是空间效率和查询时间都远远超过一般的算法，
缺点是有一定的误识别率和删除困难。

```javascript
# Python 
from bitarray import bitarray 
import mmh3 
class BloomFilter: 
	def __init__(self, size, hash_num): 
		self.size = size 
		self.hash_num = hash_num 
		self.bit_array = bitarray(size) 
		self.bit_array.setall(0) 
	def add(self, s): 
		for seed in range(self.hash_num): 
			result = mmh3.hash(s, seed) % self.size 
			self.bit_array[result] = 1 
	def lookup(self, s): 
		for seed in range(self.hash_num): 
			result = mmh3.hash(s, seed) % self.size 
			if self.bit_array[result] == 0: 
				return "Nope" 
		return "Probably" 
bf = BloomFilter(500000, 7) 
bf.add("dantezhao") 
print (bf.lookup("dantezhao")) 
print (bf.lookup("yyj")) 
```

# 三、LRU Cache

两个要素： 大小 、替换策略

O(1) 查询
O(1) 修改、更新

```javascript
# Python 

class LRUCache(object): 

	def __init__(self, capacity): 
		self.dic = collections.OrderedDict() 
		self.remain = capacity

	def get(self, key): 
		if key not in self.dic: 
			return -1 
		v = self.dic.pop(key) 
		self.dic[key] = v   # key as the newest one 
		return v 

	def put(self, key, value): 
		if key in self.dic: 
			self.dic.pop(key) 
		else: 
			if self.remain > 0: 
				self.remain -= 1 
			else:   # self.dic is full
				self.dic.popitem(last=False) 
		self.dic[key] = value
```

# 四、排序算法

1. 比较类排序：
通过比较来决定元素间的相对次序，由于其时间复杂度不能突破
O(nlogn)，因此也称为非线性时间比较类排序。
2. 非比较类排序：
不通过比较来决定元素间的相对次序，它可以突破基于比较排序的时
间下界，以线性时间运行，因此也称为线性时间非比较类排序。

## 初级排序     O(n^2)

1. 选择排序（Selection Sort）
每次找最小值，然后放到待排序数组的起始位置。
2. 插入排序（Insertion Sort）
从前到后逐步构建有序序列；对于未排序数据，在已排序序列中从后
向前扫描，找到相应位置并插入。
3. 冒泡排序（Bubble Sort）
嵌套循环，每次查看相邻的元素如果逆序，则交换


## 快速排序（Quick Sort）   O(N*LogN)
数组取标杆 pivot，将小元素放 pivot左边，大元素放右侧，然后依
次对右边和右边的子数组继续快排；以达到整个序列有序。

## 归并排序（Merge Sort）— 分治    O(N*LogN)
1. 把长度为n的输入序列分成两个长度为n/2的子序列；
2. 对这两个子序列分别采用归并排序；
3. 将两个排序好的子序列合并成一个最终的排序序列

```javascript
#Python 快速排序

def quick_sort(begin, end, nums):
    if begin >= end:
        return
    pivot_index = partition(begin, end, nums)
    quick_sort(begin, pivot_index-1, nums)
    quick_sort(pivot_index+1, end, nums)
    
def partition(begin, end, nums):
    pivot = nums[begin]
    mark = begin
    for i in range(begin+1, end+1):
        if nums[i] < pivot:
            mark +=1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[begin], nums[mark] = nums[mark], nums[begin]
    return mark
```


```javascript
#Python 归并排序

def mergesort(nums, left, right):
    if right <= left:
        return
    mid = (left+right) >> 1
    mergesort(nums, left, mid)
    mergesort(nums, mid+1, right)
    merge(nums, left, mid, right)

def merge(nums, left, mid, right):
    temp = []
    i = left
    j = mid+1
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i +=1
        else:
            temp.append(nums[j])
            j +=1
    while i<=mid:
        temp.append(nums[i])
        i +=1
    while j<=right:
        temp.append(nums[j])
        j +=1
    nums[left:right+1] = temp
```
