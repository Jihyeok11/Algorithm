# 문제 \[15655\]

##### 문제 설명
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

- N개의 자연수 중에서 M개를 고른 수열
- 고른 수열은 오름차순이어야 한다. 


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

-   예제 입력 2  
4 2
9 8 7 1

- 예제 출력 2  

  1 7
  1 8
  1 9
  7 8
  7 9
  8 9

- 예제 입력 3  
  4 4
  1231 1232 1233 1234

- 예제 출력 3  
  1231 1232 1233 1234


#### 문제 해석

 이번 문제는 첫줄의 입력값으로 N과 M이 주어지고 다음 줄에서 N개 숫자들을 제공해 준다. 이전 문제와 같이 List라는 이름의 리스트에 숫자들을 저장해둔다. 초기값들을 설정해 둔다.

 <div class="colorscripter-code" style="color:#FEFEFE;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#222222;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px;border-right:2px solid #4f4f4f"><div style="margin:0;padding:0;word-break:normal;text-align:right;color:#aaa;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="line-height:130%">1</div><div style="line-height:130%">2</div><div style="line-height:130%">3</div><div style="line-height:130%">4</div><div style="line-height:130%">5</div></div></td><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#FEFEFE;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%">N,M&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;map(<span style="color:#05F6D5">int</span>,input().split())</div><div style="padding:0 6px; white-space:pre; line-height:130%">List&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;list(map(<span style="color:#05F6D5">int</span>,input().split()))</div><div style="padding:0 6px; white-space:pre; line-height:130%">List.sort()</div><div style="padding:0 6px; white-space:pre; line-height:130%">Answer&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;[]</div><div style="padding:0 6px; white-space:pre; line-height:130%">use_check&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;[True]&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">*</span>&nbsp;N</div></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>

초기값들의 설명은 가장 첫 문제에서 주석을 달아 설명해두었다. (확인이 필요할 시 https://codingabc.tistory.com/2 )

이번 문제에서는 앞에서 사용된 숫자의 인덱스 값을 True에서 False로 바꾸고, False일 시, 사용하지 않도록 설정해두어야 한다. 그래서 아래와 같은 코드를 짜보았다.

<div class="colorscripter-code" style="color:#FEFEFE;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#222222;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px;border-right:2px solid #4f4f4f"><div style="margin:0;padding:0;word-break:normal;text-align:right;color:#aaa;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="line-height:130%">1</div><div style="line-height:130%">2</div><div style="line-height:130%">3</div><div style="line-height:130%">4</div><div style="line-height:130%">5</div><div style="line-height:130%">6</div><div style="line-height:130%">7</div><div style="line-height:130%">8</div><div style="line-height:130%">9</div><div style="line-height:130%">10</div><div style="line-height:130%">11</div><div style="line-height:130%">12</div><div style="line-height:130%">13</div><div style="line-height:130%">14</div><div style="line-height:130%">15</div><div style="line-height:130%">16</div><div style="line-height:130%">17</div></div></td><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#FEFEFE;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#F1AD0B">def</span>&nbsp;bubun(idx):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;global&nbsp;Answer</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">if</span>&nbsp;idx&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span><span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;M:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#05F6D5">print</span>(<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">*</span>Answer)</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">return</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">else</span>:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">for</span>&nbsp;i&nbsp;<span style="color:#F1AD0B">in</span>&nbsp;<span style="color:#05F6D5">range</span>(idx,N):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">if</span>&nbsp;<span style="color:#F1AD0B">not</span>&nbsp;use_check[i]&nbsp;:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continue</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use_check[i]&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;False</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Answer.append(List[i])</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bubun(idx<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">+</span><span style="color:#C302ED">1</span>)</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Answer.pop()</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">for</span>&nbsp;j&nbsp;<span style="color:#F1AD0B">in</span>&nbsp;<span style="color:#05F6D5">range</span>(i<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">+</span><span style="color:#C302ED">1</span>,N):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use_check[j]&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;True</div></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>

가장 아래 for구문은 앞에서 사용한 숫자 다음의 숫자들을 다시 True로 바꿔주는 과정이다. 그래야만 한 싸이클이 돌고 다음 숫자들이 True로 되어있기 때문에 다시 사용할 수 있다.

마지막으로 전체 코딩을 확인해보면 끝이다. 코드를 공개하고 이번 포스팅을 마치겠다.

<div class="colorscripter-code" style="color:#FEFEFE;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#222222;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px;border-right:2px solid #4f4f4f"><div style="margin:0;padding:0;word-break:normal;text-align:right;color:#aaa;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="line-height:130%">1</div><div style="line-height:130%">2</div><div style="line-height:130%">3</div><div style="line-height:130%">4</div><div style="line-height:130%">5</div><div style="line-height:130%">6</div><div style="line-height:130%">7</div><div style="line-height:130%">8</div><div style="line-height:130%">9</div><div style="line-height:130%">10</div><div style="line-height:130%">11</div><div style="line-height:130%">12</div><div style="line-height:130%">13</div><div style="line-height:130%">14</div><div style="line-height:130%">15</div><div style="line-height:130%">16</div><div style="line-height:130%">17</div><div style="line-height:130%">18</div><div style="line-height:130%">19</div><div style="line-height:130%">20</div><div style="line-height:130%">21</div><div style="line-height:130%">22</div><div style="line-height:130%">23</div><div style="line-height:130%">24</div><div style="line-height:130%">25</div></div></td><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#FEFEFE;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%">N,M&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;map(<span style="color:#05F6D5">int</span>,input().split())</div><div style="padding:0 6px; white-space:pre; line-height:130%">List&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;list(map(<span style="color:#05F6D5">int</span>,input().split()))</div><div style="padding:0 6px; white-space:pre; line-height:130%">List.sort()</div><div style="padding:0 6px; white-space:pre; line-height:130%">Answer&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;[]</div><div style="padding:0 6px; white-space:pre; line-height:130%">use_check&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;[True]&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">*</span>&nbsp;N</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#F1AD0B">def</span>&nbsp;bubun(idx):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;global&nbsp;Answer</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">if</span>&nbsp;idx&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span><span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;M:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#05F6D5">print</span>(<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">*</span>Answer)</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">return</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">else</span>:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">for</span>&nbsp;i&nbsp;<span style="color:#F1AD0B">in</span>&nbsp;<span style="color:#05F6D5">range</span>(idx,N):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">if</span>&nbsp;<span style="color:#F1AD0B">not</span>&nbsp;use_check[i]&nbsp;:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continue</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use_check[i]&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;False</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Answer.append(List[i])</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bubun(idx<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">+</span><span style="color:#C302ED">1</span>)</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Answer.pop()</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">for</span>&nbsp;j&nbsp;<span style="color:#F1AD0B">in</span>&nbsp;<span style="color:#05F6D5">range</span>(i<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">+</span><span style="color:#C302ED">1</span>,N):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use_check[j]&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;True</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">bubun(<span style="color:#C302ED">0</span>)</div></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>



#### 출처
https://www.acmicpc.net/problem/15655


