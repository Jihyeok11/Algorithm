# 문제 \[15651\]

##### 문제 설명

 N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

- N개의 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.
- 고른 수열은 비내림차순이어야 한다.
  - 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

##### 입력

첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

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

-   예제 입력 1  
	4 2
    9 8 7 1

-   예제 출력 1  
    1 1
    1 7
    1 8
    1 9
    7 7
    7 8
    7 9
    8 8
    8 9
    9 9


-   예제 입력 1  
    4 4
    1231 1232 1233 1234

-   예제 출력 1  

    1231 1231 1231 1231
    1231 1231 1231 1232
    1231 1231 1231 1233
    1231 1231 1231 1234
    1231 1231 1232 1232
    1231 1231 1232 1233
    1231 1231 1232 1234
    1231 1231 1233 1233
    1231 1231 1233 1234
    1231 1231 1234 1234
    1231 1232 1232 1232
    1231 1232 1232 1233
    1231 1232 1232 1234
    1231 1232 1233 1233
    1231 1232 1233 1234
    1231 1232 1234 1234
    1231 1233 1233 1233
    1231 1233 1233 1234
    1231 1233 1234 1234
    1231 1234 1234 1234
    1232 1232 1232 1232
    1232 1232 1232 1233
    1232 1232 1232 1234
    1232 1232 1233 1233
    1232 1232 1233 1234
    1232 1232 1234 1234
    1232 1233 1233 1233
    1232 1233 1233 1234
    1232 1233 1234 1234
    1232 1234 1234 1234
    1233 1233 1233 1233
    1233 1233 1233 1234
    1233 1233 1234 1234
    1233 1234 1234 1234
    1234 1234 1234 1234

#### 문제 해석
이번 문제는 N과 M(7)과는 살짝 다른 문제이다. 앞에서부터 append를 시키는데, 뒤에 숫자는 앞에서 사용한 숫자보다 크거나 같아야 한다. 자기 자신을 다시 사용해야 하므로, boolean을 사용하지 않고 풀 수 있다. 일단 초기는 앞에서 사용했던 것과 동일하다.
<div class="colorscripter-code" style="color:#FEFEFE;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#222222;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px;border-right:2px solid #4f4f4f"><div style="margin:0;padding:0;word-break:normal;text-align:right;color:#aaa;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="line-height:130%">1</div><div style="line-height:130%">2</div><div style="line-height:130%">3</div><div style="line-height:130%">4</div><div style="line-height:130%">5</div><div style="line-height:130%">6</div></div></td><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#FEFEFE;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%">N,M&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;map(<span style="color:#05F6D5">int</span>,input().split())</div><div style="padding:0 6px; white-space:pre; line-height:130%">List&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;sorted(list(map(<span style="color:#05F6D5">int</span>,input().split())))</div><div style="padding:0 6px; white-space:pre; line-height:130%">Answer&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;[]</div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#F1AD0B">def</span>&nbsp;bubun(idx):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">if</span>&nbsp;<span style="color:#05F6D5">len</span>(Answer)&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span><span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;M:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#05F6D5">print</span>(<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">*</span>Answer)</div></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>

이번에는 자기 자신의 인덱스를 재귀 때 다시 사용하므로 range 값을 idx부터로 사용하고, 멈추는 조건을 길이가 M일 때로 설정해 두자. 즉 아래와 같은 코드가 될 것이다.
<div class="colorscripter-code" style="color:#FEFEFE;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#222222;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px;border-right:2px solid #4f4f4f"><div style="margin:0;padding:0;word-break:normal;text-align:right;color:#aaa;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="line-height:130%">1</div><div style="line-height:130%">2</div><div style="line-height:130%">3</div><div style="line-height:130%">4</div><div style="line-height:130%">5</div><div style="line-height:130%">6</div><div style="line-height:130%">7</div><div style="line-height:130%">8</div><div style="line-height:130%">9</div><div style="line-height:130%">10</div><div style="line-height:130%">11</div><div style="line-height:130%">12</div></div></td><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#FEFEFE;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#F1AD0B">def</span>&nbsp;bubun(idx):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">if</span>&nbsp;<span style="color:#05F6D5">len</span>(Answer)&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span><span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;M:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#05F6D5">print</span>(<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">*</span>Answer)</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">else</span>:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">for</span>&nbsp;i&nbsp;<span style="color:#F1AD0B">in</span>&nbsp;<span style="color:#05F6D5">range</span>(idx,N):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Answer.append(List[i])</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bubun(idx)</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Answer.pop()</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;idx&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">+</span><span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;<span style="color:#C302ED">1</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">bubun(<span style="color:#C302ED">0</span>)</div></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>


#### 출처

https://www.acmicpc.net/problem/15657