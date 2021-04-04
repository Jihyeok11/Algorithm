# 문제 \[15651\]

##### 문제 설명
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.

##### 입력

첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 7)

##### 출력

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

-   예제 입력 1  
    3 1
-   예제 출력 1  
    1  
    2  
    3

-   예제 입력 1  
    4 2
-   예제 출력 1  
    1 1
    1 2
    1 3
    1 4
    2 1
    2 2
    2 3
    2 4
    3 1
    3 2
    3 3
    3 4
    4 1
    4 2
    4 3
    4 4

-   예제 입력 1  
    3 3
-   예제 출력 1  
    1 1
    1 2
    1 3
    1 4
    2 1
    2 2
    2 3
    2 4
    3 1
    3 2
    3 3
    3 4
    4 1
    4 2
    4 3
    4 4

#### 문제 해석

이번 문제는 기존의 사용 여부가 필요가 없다. 그래서 True,False 기능만 삭제하고 append와 pop기능만 사용한다. 이번 문제는 간단하니 바로 코딩을 공개하고 끝내겠습니다.

<div class="colorscripter-code" style="color:#FEFEFE;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#222222;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px;border-right:2px solid #4f4f4f"><div style="margin:0;padding:0;word-break:normal;text-align:right;color:#aaa;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="line-height:130%">1</div><div style="line-height:130%">2</div><div style="line-height:130%">3</div><div style="line-height:130%">4</div><div style="line-height:130%">5</div><div style="line-height:130%">6</div><div style="line-height:130%">7</div><div style="line-height:130%">8</div><div style="line-height:130%">9</div><div style="line-height:130%">10</div><div style="line-height:130%">11</div><div style="line-height:130%">12</div><div style="line-height:130%">13</div><div style="line-height:130%">14</div><div style="line-height:130%">15</div><div style="line-height:130%">16</div></div></td><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#FEFEFE;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%">N,M&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;map(<span style="color:#05F6D5">int</span>,input().split())</div><div style="padding:0 6px; white-space:pre; line-height:130%">List&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;[]</div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#F1AD0B">for</span>&nbsp;i&nbsp;<span style="color:#F1AD0B">in</span>&nbsp;<span style="color:#05F6D5">range</span>(N):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;List.append(i<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">+</span><span style="color:#C302ED">1</span>)</div><div style="padding:0 6px; white-space:pre; line-height:130%">Answer&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;[]</div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#F1AD0B">def</span>&nbsp;bubun(idx):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;global&nbsp;Answer</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">if</span>&nbsp;idx&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span><span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;M:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#05F6D5">print</span>(<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">*</span>Answer)</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">else</span>:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">for</span>&nbsp;i&nbsp;<span style="color:#F1AD0B">in</span>&nbsp;<span style="color:#05F6D5">range</span>(N):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Answer.append(List[i])</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bubun(idx<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">+</span><span style="color:#C302ED">1</span>)</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Answer.pop()</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">bubun(<span style="color:#C302ED">0</span>)</div></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>



#### 출처


[https://www.acmicpc.net/problem/15651](https://www.acmicpc.net/problem/15651)

[