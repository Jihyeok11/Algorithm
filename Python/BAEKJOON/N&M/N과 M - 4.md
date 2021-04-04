# 문제 \[15651\]

##### 문제 설명

 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.
- 고른 수열은 비내림차순이어야 한다.
  - 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

##### 입력

첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)



##### 출력

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.



-  예제 입력 1 

3 1

-  예제 출력 1 

1

2

3



-  예제 입력 1 

4 2
-  예제 출력 1 

1 1
1 2
1 3
1 4
2 2
2 3
2 4
3 3
3 4
4 4




-  예제 입력 1 
3 3

-  예제 출력 1

1 1 1
1 1 2
1 1 3
1 2 2
1 2 3
1 3 3
2 2 2
2 2 3
2 3 3
3 3 3

#### 문제 해석
이번의 출력값들을 보면 앞에서부터 사용한 숫자들을 다시 사용할 수 있으나, 크기가 같거나 큰 값들을 사용하고 있다. 사용한 숫자를 다시 사용하고 있으므로 True, False 문제는 아닌 것 같다. 그러면 어떻게 해야 할까? 한번 숫자를 append 시키고, 다시 재귀로 돌아가 다시 같은 숫자를 append 시키고 길이가 M일 때 print를 하고 pop을 시켜보자. 그러면 입력이 `3 3`일 때를 확인하면 결과값으로 
```python
1 1 1
1 1 2
1 1 3
1 2 1
1 2 2
1 2 3
1 3 1
1 3 2
1 3 3
2 1 1
2 1 2
2 1 3
2 2 1
2 2 2
2 2 3
2 3 1
2 3 2
2 3 3
3 1 1
3 1 2
3 1 3
3 2 1
3 2 2
3 2 3
3 3 1
3 3 2
3 3 3
```
와 같은 결과가 나온다. 우리는 앞에서 사용한 숫자보다 같거나 큰 수를 사용해야 한다. 2를 앞에서 사용하면 1이 아닌 2나 3이 나와야 하지만 결과값은 전부다 표시하고 있습니다. 그러면 인덱스 범위를 idx부터 N까지로 변경시키고, pop이후에 idx값을 추가시키면 어떻게 될까? 자기 자신도 나오고 append값은 자기 자신과 같거나 그 이상이 나올 것이다. 한번 실행해 보자. 일단 코드를 공개하면 이와 같다.
<div class="colorscripter-code" style="color:#FEFEFE;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#222222;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px;border-right:2px solid #4f4f4f"><div style="margin:0;padding:0;word-break:normal;text-align:right;color:#aaa;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="line-height:130%">1</div><div style="line-height:130%">2</div><div style="line-height:130%">3</div><div style="line-height:130%">4</div><div style="line-height:130%">5</div><div style="line-height:130%">6</div><div style="line-height:130%">7</div><div style="line-height:130%">8</div><div style="line-height:130%">9</div><div style="line-height:130%">10</div><div style="line-height:130%">11</div><div style="line-height:130%">12</div><div style="line-height:130%">13</div><div style="line-height:130%">14</div><div style="line-height:130%">15</div><div style="line-height:130%">16</div><div style="line-height:130%">17</div></div></td><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#FEFEFE;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%">N,&nbsp;M&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;map(<span style="color:#05F6D5">int</span>,input().split())</div><div style="padding:0 6px; white-space:pre; line-height:130%">List&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;[x<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">+</span><span style="color:#C302ED">1</span>&nbsp;<span style="color:#F1AD0B">for</span>&nbsp;x&nbsp;<span style="color:#F1AD0B">in</span>&nbsp;<span style="color:#05F6D5">range</span>(N)]</div><div style="padding:0 6px; white-space:pre; line-height:130%">Answer&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;[]</div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#F1AD0B">def</span>&nbsp;bubun(idx):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">if</span>&nbsp;<span style="color:#05F6D5">len</span>(Answer)&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span><span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;M:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#05F6D5">print</span>(<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">*</span>Answer)</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">return</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">else</span>:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">for</span>&nbsp;i&nbsp;<span style="color:#F1AD0B">in</span>&nbsp;<span style="color:#05F6D5">range</span>(idx,N):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Answer.append(List[i])</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bubun(idx)</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Answer.pop()</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;idx<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">+</span><span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span><span style="color:#C302ED">1</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">bubun(<span style="color:#C302ED">0</span>)</div></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>



결과값을 확인해보면 우리가 원하던 결과값이 나온다는 것을 확인 할 수가 있다.

#### 출처

https://www.acmicpc.net/problem/15652

