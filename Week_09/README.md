# 一、高级动态规划

## 递归、分治、回溯、动态规划复习：

## 递归 - 函数自己调用自己
```javascript
public void recur(int level, int param) {
	 // terminator
	 if (level > MAX_LEVEL) {
		 // process result
		 return;
	 }
	 // process current logic
	 process(level, param);
	 // drill down
	 recur(level: level + 1, newParam);
	 // restore current status

}
```

## 分治
```javascript
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

## 动态规划 Dynamic Programming
```javascript
1.“Simplifying a complicated problem by breaking it down into
simpler sub-problems”
(in a recursive manner)

2. Divide & Conquer + Optimal substructure
 分治  + 最优子结构
3. 顺推形式： 动态递推

DP 顺推模板
function DP():
	 dp = [][] # ⼆维情况
	 for i = 0 .. M {
		 for j = 0 .. N { 
		 	dp[i][j] = _Function(dp[i’][j’]…)
		 }
	 }
	 return dp[M][N]; 
```

# 二、字符串

## 字符串匹配算法

1. 暴力法（brute force） - o(mn)
2. Rabin-Karp 算法
3. KMP算法
