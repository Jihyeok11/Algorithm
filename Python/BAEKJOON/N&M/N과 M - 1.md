# 문제 \[15649\]

### 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

-   1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

### 입력

첫째 줄에 자연수 N과 M이 주어진다.(1 ≤ M ≤ N ≤ 8)

### 출력

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

(수열은 사전 순으로 증가하는 순서로 출력해야 한다.)

### 예제 입력1

3 1

### 결과

1  
2  
3

### 예제 입력2

4 2

### 결과

1 2  
1 3  
1 4  
2 1  
2 3  
2 4  
3 1  
3 2  
3 4  
4 1  
4 2  
4 3

### 예제 입력3

4 4

### 결과

1 2 3 4  
1 2 4 3  
1 3 2 4  
1 3 4 2  
1 4 2 3  
1 4 3 2  
2 1 3 4  
2 1 4 3  
2 3 1 4  
2 3 4 1  
2 4 1 3  
2 4 3 1  
3 1 2 4  
3 1 4 2  
3 2 1 4  
3 2 4 1  
3 4 1 2  
3 4 2 1  
4 1 2 3  
4 1 3 2  
4 2 1 3  
4 2 3 1  
4 3 1 2  
4 3 2 1

### 문제 풀이

문제를 해석해 보자. 입력값으로 N과 M이 주어지고, 출력값들의 길이는 M이다. 그리고 규칙적으로 뒷자리부터 해서 점차 증가하는 결과가 나온다. 일단 리스트를 만들어 보자. 입력값 \[4 2\]를 기준으로 시도를 한다. 사용되는 숫자들은 1,2,3,4 이므로 List라는 이름으로 새로운 리스트를 만들고 초기값들을 설정해두자.

<table class="colorscripter-code-table" style="margin: 0; padding: 0; border: none; background-color: #222222; border-radius: 4px;" cellspacing="0" cellpadding="0"><tbody><tr><td style="padding: 6px; border-right: 2px solid #4f4f4f;"><div style="margin: 0; padding: 0; word-break: normal; text-align: right; color: #aaa; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; line-height: 130%;"><div style="line-height: 130%;">1</div><div style="line-height: 130%;">2</div><div style="line-height: 130%;">3</div><div style="line-height: 130%;">4</div></div></td><td style="padding: 6px 0; text-align: left;"><div style="margin: 0; padding: 0; color: #fefefe; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; line-height: 130%;"><div style="padding: 0 6px; white-space: pre; line-height: 130%;">N,M&nbsp;<span style="color: #fd0aac;"></span><span style="color: #f1ad0b;">=</span>&nbsp;map(<span style="color: #05f6d5;">int</span>,input().split())&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #b0b0b0;">#입력값&nbsp;N과&nbsp;M을&nbsp;받는다.</span></div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">List&nbsp;<span style="color: #fd0aac;"></span><span style="color: #f1ad0b;">=</span>&nbsp;[&nbsp;x<span style="color: #fd0aac;"></span><span style="color: #f1ad0b;">+</span><span style="color: #c302ed;">1</span>&nbsp;<span style="color: #f1ad0b;">for</span>&nbsp;x&nbsp;<span style="color: #f1ad0b;">in</span>&nbsp;<span style="color: #05f6d5;">range</span>(N)&nbsp;]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #b0b0b0;">#List는&nbsp;[1,2,3,4]가&nbsp;될&nbsp;것이다.</span></div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">use_check&nbsp;<span style="color: #fd0aac;"></span><span style="color: #f1ad0b;">=</span>&nbsp;[True]&nbsp;<span style="color: #fd0aac;"></span><span style="color: #f1ad0b;">*</span>&nbsp;N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #b0b0b0;">#&nbsp;이런&nbsp;문제같은&nbsp;경우&nbsp;사용&nbsp;여부를&nbsp;따지는게&nbsp;풀이에&nbsp;편하다.</span></div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">Answer&nbsp;<span style="color: #fd0aac;"></span><span style="color: #f1ad0b;">=</span>&nbsp;[]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #b0b0b0;">#&nbsp;나중에&nbsp;출력할&nbsp;리스트이다.</span></div></div></td><td style="vertical-align: bottom; padding: 0 2px 4px 0;"><a style="text-decoration: none; color: white;" href="http://colorscripter.com/info#e" target="_blank" rel="noopener"><span style="font-size: 9px; word-break: normal; background-color: #4f4f4f; color: white; border-radius: 10px; padding: 1px;">cs</span></a></td></tr></tbody></table>
초기값들을 설정해 두고, 이제 규칙을 찾아보자. 출력값은 `1 2` 로 시작하여 `1 3` , `1 4`를 거쳐 `4 3`이 나와야 한다. 즉 뒷자리부터 앞에 숫자를 제외하고 돌아가면서 사용해야 한다. 이제부터 함수를 정의해보자  
함수의 이름은 bubun으로 하였고, 만약 숫자를 사용하면 그에 해당하는 인덱스값을 False로 바꿔주어 True인 애들만 사용하게 만들었다.

<table class="colorscripter-code-table" style="margin: 0; padding: 0; border: none; background-color: #222222; border-radius: 4px;" cellspacing="0" cellpadding="0"><tbody><tr><td style="padding: 6px; border-right: 2px solid #4f4f4f;"><div style="margin: 0; padding: 0; word-break: normal; text-align: right; color: #aaa; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; line-height: 130%;"><div style="line-height: 130%;">1</div><div style="line-height: 130%;">2</div><div style="line-height: 130%;">3</div><div style="line-height: 130%;">4</div><div style="line-height: 130%;">5</div><div style="line-height: 130%;">6</div><div style="line-height: 130%;">7</div><div style="line-height: 130%;">8</div><div style="line-height: 130%;">9</div><div style="line-height: 130%;">10</div><div style="line-height: 130%;">11</div><div style="line-height: 130%;">12</div><div style="line-height: 130%;">13</div><div style="line-height: 130%;">14</div></div></td><td style="padding: 6px 0; text-align: left;"><div style="margin: 0; padding: 0; color: #fefefe; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; line-height: 130%;"><div style="padding: 0 6px; white-space: pre; line-height: 130%;"><span style="color: #f1ad0b;">def</span>&nbsp;bubun(idx):&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #b0b0b0;">#&nbsp;함수를&nbsp;정의</span></div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #f1ad0b;">if</span>&nbsp;idx<span style="color: #fd0aac;"></span><span style="color: #f1ad0b;">=</span><span style="color: #fd0aac;"></span><span style="color: #f1ad0b;">=</span>M:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #b0b0b0;">#&nbsp;idx&nbsp;값을&nbsp;0부터&nbsp;시작해서&nbsp;1개씩&nbsp;올릴것이다.&nbsp;idx가&nbsp;0인&nbsp;경우&nbsp;Answer의&nbsp;값들을&nbsp;print한다.</span></div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #05f6d5;">print</span>(<span style="color: #fd0aac;"></span><span style="color: #f1ad0b;">*</span>Answer)</div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #f1ad0b;">return</span></div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #f1ad0b;">else</span>:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #b0b0b0;">#&nbsp;idx&nbsp;값이&nbsp;M이&nbsp;아닌&nbsp;경우</span></div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #f1ad0b;">for</span>&nbsp;i&nbsp;<span style="color: #f1ad0b;">in</span>&nbsp;<span style="color: #05f6d5;">range</span>(N):&nbsp;&nbsp;&nbsp;&nbsp;</div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #f1ad0b;">if</span>&nbsp;<span style="color: #f1ad0b;">not</span>&nbsp;use_check[i]:&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #b0b0b0;">#&nbsp;만약&nbsp;True가&nbsp;아니면&nbsp;continue를&nbsp;통해&nbsp;for구문으로&nbsp;돌아간다.</span></div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continue&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #b0b0b0;">#&nbsp;True&nbsp;면&nbsp;통과</span></div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use_check[i]&nbsp;<span style="color: #fd0aac;"></span><span style="color: #f1ad0b;">=</span>&nbsp;False&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #b0b0b0;">#&nbsp;True&nbsp;였던&nbsp;i번째&nbsp;값을&nbsp;False로&nbsp;변경</span></div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Answer.append(List[i])&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #b0b0b0;">#&nbsp;i번째&nbsp;값을&nbsp;Answer에&nbsp;붙여준다.</span></div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bubun(idx<span style="color: #fd0aac;"></span><span style="color: #f1ad0b;">+</span><span style="color: #c302ed;">1</span>)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #b0b0b0;">#&nbsp;idx값을&nbsp;1만큼&nbsp;증가시켜&nbsp;재실행.&nbsp;처음&nbsp;시도시&nbsp;use_check=[F,T,T,T]&nbsp;,&nbsp;Answer&nbsp;=&nbsp;[1]&nbsp;로&nbsp;다시&nbsp;실행된다.</span></div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Answer.pop()&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #b0b0b0;">#&nbsp;한&nbsp;번&nbsp;사용하였으면&nbsp;이제&nbsp;반납을&nbsp;해준다.</span></div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use_check[i]&nbsp;<span style="color: #fd0aac;"></span><span style="color: #f1ad0b;">=</span>&nbsp;True&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #b0b0b0;">#&nbsp;False에서&nbsp;다시&nbsp;True로&nbsp;반납해준다.</span></div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;</div></div><div style="text-align: right; margin-top: -13px; margin-right: 5px; font-size: 9px; font-style: italic;"><a style="color: #4f4f4ftext-decoration:none;" href="http://colorscripter.com/info#e" target="_blank" rel="noopener">Colored by Color Scripter</a></div></td><td style="vertical-align: bottom; padding: 0 2px 4px 0;"><a style="text-decoration: none; color: white;" href="http://colorscripter.com/info#e" target="_blank" rel="noopener"><span style="font-size: 9px; word-break: normal; background-color: #4f4f4f; color: white; border-radius: 10px; padding: 1px;">cs</span></a></td></tr></tbody></table>
이제 결과값을 확인해보자. 정의된 함수를 사용하기 위해서 bubun(0)을 아래에서 실행해보자. 그러면 우리가 원하는 결과가 나온다는 것을 확인 할 수가 있다. 이제 완성된 코드를 써보자.

<table class="colorscripter-code-table" style="margin: 0; padding: 0; border: none; background-color: #222222; border-radius: 4px;" cellspacing="0" cellpadding="0"><tbody><tr><td style="padding: 6px; border-right: 2px solid #4f4f4f;"><div style="margin: 0; padding: 0; word-break: normal; text-align: right; color: #aaa; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; line-height: 130%;"><div style="line-height: 130%;">1</div><div style="line-height: 130%;">2</div><div style="line-height: 130%;">3</div><div style="line-height: 130%;">4</div><div style="line-height: 130%;">5</div><div style="line-height: 130%;">6</div><div style="line-height: 130%;">7</div><div style="line-height: 130%;">8</div><div style="line-height: 130%;">9</div><div style="line-height: 130%;">10</div><div style="line-height: 130%;">11</div><div style="line-height: 130%;">12</div><div style="line-height: 130%;">13</div><div style="line-height: 130%;">14</div><div style="line-height: 130%;">15</div><div style="line-height: 130%;">16</div><div style="line-height: 130%;">17</div><div style="line-height: 130%;">18</div><div style="line-height: 130%;">19</div><div style="line-height: 130%;">20</div><div style="line-height: 130%;">21</div><div style="line-height: 130%;">22</div><div style="line-height: 130%;">23</div></div></td><td style="padding: 6px 0; text-align: left;"><div style="margin: 0; padding: 0; color: #fefefe; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; line-height: 130%;"><div style="padding: 0 6px; white-space: pre; line-height: 130%;">N,M&nbsp;<span style="color: #fd0aac;"></span><span style="color: #f1ad0b;">=</span>&nbsp;map(<span style="color: #05f6d5;">int</span>,input().split())</div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">List&nbsp;<span style="color: #fd0aac;"></span><span style="color: #f1ad0b;">=</span>&nbsp;[]</div><div style="padding: 0 6px; white-space: pre; line-height: 130%;"><span style="color: #f1ad0b;">for</span>&nbsp;i&nbsp;<span style="color: #f1ad0b;">in</span>&nbsp;<span style="color: #05f6d5;">range</span>(N):</div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;&nbsp;&nbsp;&nbsp;List.append(i<span style="color: #fd0aac;"></span><span style="color: #f1ad0b;">+</span><span style="color: #c302ed;">1</span>)</div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;</div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">use_check&nbsp;<span style="color: #fd0aac;"></span><span style="color: #f1ad0b;">=</span>&nbsp;[True]&nbsp;<span style="color: #fd0aac;"></span><span style="color: #f1ad0b;">*</span>&nbsp;N</div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">check&nbsp;<span style="color: #fd0aac;"></span><span style="color: #f1ad0b;">=</span>&nbsp;[<span style="color: #c302ed;">0</span>&nbsp;<span style="color: #f1ad0b;">for</span>&nbsp;_&nbsp;<span style="color: #f1ad0b;">in</span>&nbsp;<span style="color: #05f6d5;">range</span>(N)]</div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">Answer&nbsp;<span style="color: #fd0aac;"></span><span style="color: #f1ad0b;">=</span>&nbsp;[]</div><div style="padding: 0 6px; white-space: pre; line-height: 130%;"><span style="color: #f1ad0b;">def</span>&nbsp;bubun(idx):</div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #f1ad0b;">if</span>&nbsp;idx<span style="color: #fd0aac;"></span><span style="color: #f1ad0b;">=</span><span style="color: #fd0aac;"></span><span style="color: #f1ad0b;">=</span>M:</div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #05f6d5;">print</span>(<span style="color: #fd0aac;"></span><span style="color: #f1ad0b;">*</span>Answer)</div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #f1ad0b;">return</span></div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #f1ad0b;">else</span>:</div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #f1ad0b;">for</span>&nbsp;i&nbsp;<span style="color: #f1ad0b;">in</span>&nbsp;<span style="color: #05f6d5;">range</span>(N):</div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #f1ad0b;">if</span>&nbsp;<span style="color: #f1ad0b;">not</span>&nbsp;use_check[i]:</div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continue</div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use_check[i]&nbsp;<span style="color: #fd0aac;"></span><span style="color: #f1ad0b;">=</span>&nbsp;False</div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Answer.append(List[i])</div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bubun(idx<span style="color: #fd0aac;"></span><span style="color: #f1ad0b;">+</span><span style="color: #c302ed;">1</span>)</div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Answer.pop()</div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use_check[i]&nbsp;<span style="color: #fd0aac;"></span><span style="color: #f1ad0b;">=</span>&nbsp;True</div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">&nbsp;</div><div style="padding: 0 6px; white-space: pre; line-height: 130%;">bubun(<span style="color: #c302ed;">0</span>)</div></div></td><td style="vertical-align: bottom; padding: 0 2px 4px 0;"><a style="text-decoration: none; color: white;" href="http://colorscripter.com/info#e" target="_blank" rel="noopener"><span style="font-size: 9px; word-break: normal; background-color: #4f4f4f; color: white; border-radius: 10px; padding: 1px;">cs</span></a></td></tr></tbody></table>
#### 이번 포스팅을 마치며

사용했는지 여부를 판별하는 use\_check개념이 생각보다 제대로 안잡혀 있다는 것을 알았다. 다른 문제들을 풀어가면서 고쳐보도록 하겠다.

### 출처

# [https://www.acmicpc.net/problem/15649](https://www.acmicpc.net/problem/15649)

[

15649번: N과 M (1)

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다. 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

www.acmicpc.net



](https://www.acmicpc.net/problem/15649)