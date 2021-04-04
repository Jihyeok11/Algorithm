
# 문제 \[15651\]

##### 문제 설명

 N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

- N개의 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.

##### 입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 7)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.



##### 출력

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.


-   예제 입력 1  
    3 1
    4 5 2

-   예제 출력 1  
    2
    4
    5

- 예제 입력 2  
    4 2
	9 8 7 1
	
-   예제 출력 2  
    1 1
    1 7
    1 8
    1 9
    7 1
    7 7
    7 8
    7 9
    8 1
    8 7
    8 8
    8 9
    9 1
    9 7
    9 8
    9 9

-   예제 입력 3  
    3 3
    1231 1232 1233

-   예제 출력 3  
    1231 1231 1231
    1231 1231 1232
    1231 1231 1233
    1231 1232 1231
    1231 1232 1232
    1231 1232 1233
    1231 1233 1231
    1231 1233 1232
    1231 1233 1233
    1232 1231 1231
    1232 1231 1232
    1232 1231 1233
    1232 1232 1231
    1232 1232 1232
    1232 1232 1233
    1232 1233 1231
    1232 1233 1232
    1232 1233 1233
    1233 1231 1231
    1233 1231 1232
    1233 1231 1233
    1233 1232 1231
    1233 1232 1232
    1233 1232 1233
    1233 1233 1231
    1233 1233 1232
    1233 1233 1233


#### 문제 해석
이번 문제는 이전 숫자들이 사용했는지의 대한 여부가 필요가 없다. 그래서 boolean구문을 삭제하고 append와 pop을 시켜주면 된다. 쉬운 문제였으니 바로 코드를 공개하고 포스팅을 마치겠다.

<div class="colorscripter-code" style="color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#272727;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px;border-right:2px solid #4f4f4f"><div style="margin:0;padding:0;word-break:normal;text-align:right;color:#aaa;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="line-height:130%">1</div><div style="line-height:130%">2</div><div style="line-height:130%">3</div><div style="line-height:130%">4</div><div style="line-height:130%">5</div><div style="line-height:130%">6</div><div style="line-height:130%">7</div><div style="line-height:130%">8</div><div style="line-height:130%">9</div><div style="line-height:130%">10</div><div style="line-height:130%">11</div><div style="line-height:130%">12</div><div style="line-height:130%">13</div><div style="line-height:130%">14</div></div></td><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%">N,M&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;map(<span style="color:#4be6fa">int</span>,input().split())</div><div style="padding:0 6px; white-space:pre; line-height:130%">List&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;sorted(list(map(<span style="color:#4be6fa">int</span>,input().split())))</div><div style="padding:0 6px; white-space:pre; line-height:130%">Answer&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;[]</div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">def</span>&nbsp;bubun(idx):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">if</span>&nbsp;idx&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span><span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;M:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#4be6fa">print</span>(<span style="color:#0086b3"></span><span style="color:#ff3399">*</span>Answer)</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">else</span>:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">for</span>&nbsp;i&nbsp;<span style="color:#ff3399">in</span>&nbsp;<span style="color:#4be6fa">range</span>(N):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Answer.append(List[i])</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bubun(idx<span style="color:#0086b3"></span><span style="color:#ff3399">+</span><span style="color:#c10aff">1</span>)</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Answer.pop()</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">bubun(<span style="color:#c10aff">0</span>)</div></div><div style="text-align:right;margin-top:-13px;margin-right:5px;font-size:9px;font-style:italic"><a href="http://colorscripter.com/info#e" target="_blank" style="color:#4f4f4ftext-decoration:none">Colored by Color Scripter</a></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>
 

 

#### 출처
https://www.acmicpc.net/problem/15656