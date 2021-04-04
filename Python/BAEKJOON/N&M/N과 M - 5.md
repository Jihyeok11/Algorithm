# 문제 \[15654\]

##### 문제 설명
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

- N개의 자연수 중에서 M개를 고른 수열
  
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


-   예제 출력 2  

1 7
1 8
1 9
7 1
7 8
7 9
8 1
8 7
8 9
9 1
9 7
9 8

-   예제 입력 3  
4 4
1231 1232 1233 1234

-   예제 출력 3  

1231 1232 1233 1234
1231 1232 1234 1233
1231 1233 1232 1234
1231 1233 1234 1232
1231 1234 1232 1233
1231 1234 1233 1232
1232 1231 1233 1234
1232 1231 1234 1233
1232 1233 1231 1234
1232 1233 1234 1231
1232 1234 1231 1233
1232 1234 1233 1231
1233 1231 1232 1234
1233 1231 1234 1232
1233 1232 1231 1234
1233 1232 1234 1231
1233 1234 1231 1232
1233 1234 1232 1231
1234 1231 1232 1233
1234 1231 1233 1232
1234 1232 1231 1233
1234 1232 1233 1231
1234 1233 1231 1232
1234 1233 1232 1231

#### 문제 해석
입력값에 첫줄에는 N과 M을 준 후, 다음 줄에 N개에 해당하는 숫자들을 제공해준다. 제공받는 숫자들을 리스트에 담아두고, 이전과 같이 초기화를 실행해둔다. 초기화에 대한 설명은 N과 M 첫번째 문제에 설명을 해두었다.  첨부 = [https://codingabc.tistory.com/2]
제공받은 숫자들을 새로운 리스트 Answer에  append시켜서 순차적으로 Answer의 길이가 M이 될 때 print를 해줄 것이다. append 방식은 앞에서 먼저 append를 하면 그 숫자를 다음번에는 사용하지 않도록 만들어 줘야 하므로 boolean방식을 사용하면 편리할 것이다. 초기값들을 True로 바꿔주고  숫자를 사용하면 그에 대한 index 값을 False로 변경시켜준다. 끝으로 함수를 실행하여 결과값을 확인해본다.

<div class="colorscripter-code" style="color:#FEFEFE;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#222222;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px;border-right:2px solid #4f4f4f"><div style="margin:0;padding:0;word-break:normal;text-align:right;color:#aaa;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="line-height:130%">1</div><div style="line-height:130%">2</div><div style="line-height:130%">3</div><div style="line-height:130%">4</div><div style="line-height:130%">5</div><div style="line-height:130%">6</div><div style="line-height:130%">7</div><div style="line-height:130%">8</div><div style="line-height:130%">9</div><div style="line-height:130%">10</div><div style="line-height:130%">11</div><div style="line-height:130%">12</div><div style="line-height:130%">13</div><div style="line-height:130%">14</div><div style="line-height:130%">15</div><div style="line-height:130%">16</div><div style="line-height:130%">17</div><div style="line-height:130%">18</div><div style="line-height:130%">19</div><div style="line-height:130%">20</div><div style="line-height:130%">21</div><div style="line-height:130%">22</div><div style="line-height:130%">23</div></div></td><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#FEFEFE;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%">N,M&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;map(<span style="color:#05F6D5">int</span>,input().split())</div><div style="padding:0 6px; white-space:pre; line-height:130%">List&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;list(map(<span style="color:#05F6D5">int</span>,input().split()))</div><div style="padding:0 6px; white-space:pre; line-height:130%">List.sort()</div><div style="padding:0 6px; white-space:pre; line-height:130%">use_check&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;[True]<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">*</span>N</div><div style="padding:0 6px; white-space:pre; line-height:130%">Answer&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;[]</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#F1AD0B">def</span>&nbsp;bubun(idx):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;global&nbsp;Answer</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">if</span>&nbsp;idx&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span><span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>M:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#05F6D5">print</span>(<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">*</span>Answer)</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">else</span>:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">for</span>&nbsp;i&nbsp;<span style="color:#F1AD0B">in</span>&nbsp;<span style="color:#05F6D5">range</span>(N):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#F1AD0B">if</span>&nbsp;use_check[i]:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use_check[i]&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;False</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Answer.append(List[i])</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bubun(idx<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">+</span><span style="color:#C302ED">1</span>)A</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Answer.pop()</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use_check[i]&nbsp;<span style="color:#FD0AAC"></span><span style="color:#F1AD0B">=</span>&nbsp;True</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">bubun(<span style="color:#C302ED">0</span>)</div></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>





#### 출처
https://www.acmicpc.net/problem/15654
[https://www.acmicpc.net/problem/15654]