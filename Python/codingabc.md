[lv3] 1003. 피보나치 함수(Python 파이썬 풀이)

```bash
아래부터
```


## 출처
https://www.acmicpc.net/problem/1012

## 결과


## 문제

차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다. 농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에, 한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다. 이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다. 특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 그 배추들 역시 해충으로부터 보호받을 수 있다.

(한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있다고 간주한다)

한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어놓았다. 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다.

예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다.

(0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.)


### 입력

입력은 여러 개의 테스트 케이스로 이루어져 있으며, 각 줄마다 1 이상 99999 이하의 정수가 주어진다. 입력의 마지막 줄에는 0이 주어지며, 이 줄은 문제에 포함되지 않는다.

### 출력

각 줄마다 주어진 수가 팰린드롬수면 'yes', 아니면 'no'를 출력한다.

### 제한

- 1 ≤ w, h ≤ 1,000
- 1 ≤ x ≤ w-1
- 1 ≤ y ≤ h-1
- x, y, w, h는 정수


#### 예제 입력  

```
121
1231
12421
0
```

#### 예제 출력  

```
yes
no
yes
```

### 해석


### 소스 코드

<div class="colorscripter-code" style="color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#272727;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px;border-right:2px solid #4f4f4f"><div style="margin:0;padding:0;word-break:normal;text-align:right;color:#aaa;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="line-height:130%">1</div><div style="line-height:130%">2</div><div style="line-height:130%">3</div><div style="line-height:130%">4</div><div style="line-height:130%">5</div><div style="line-height:130%">6</div><div style="line-height:130%">7</div><div style="line-height:130%">8</div><div style="line-height:130%">9</div><div style="line-height:130%">10</div><div style="line-height:130%">11</div><div style="line-height:130%">12</div><div style="line-height:130%">13</div><div style="line-height:130%">14</div><div style="line-height:130%">15</div><div style="line-height:130%">16</div><div style="line-height:130%">17</div></div></td><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">import</span>&nbsp;sys</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">def</span>&nbsp;most_value(idx,&nbsp;w,&nbsp;v):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;global&nbsp;answer,&nbsp;n,&nbsp;k</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">if</span>&nbsp;v&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">&gt;</span>&nbsp;answer:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;answer&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;v</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">for</span>&nbsp;i&nbsp;<span style="color:#ff3399">in</span>&nbsp;<span style="color:#4be6fa">range</span>(idx,&nbsp;n):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">if</span>&nbsp;w&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">+</span>&nbsp;li[idx][<span style="color:#c10aff">0</span>]&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">&gt;</span>&nbsp;k:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">return</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;most_value(i<span style="color:#0086b3"></span><span style="color:#ff3399">+</span><span style="color:#c10aff">1</span>,&nbsp;w&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">+</span>&nbsp;li[idx][<span style="color:#c10aff">0</span>],&nbsp;v&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">+</span>&nbsp;li[idx][<span style="color:#c10aff">1</span>])</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">n,&nbsp;k&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;map(<span style="color:#4be6fa">int</span>,&nbsp;sys.stdin.readline().split())</div><div style="padding:0 6px; white-space:pre; line-height:130%">li&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;sorted(list(list(map(<span style="color:#4be6fa">int</span>,&nbsp;sys.stdin.readline().split()))&nbsp;<span style="color:#ff3399">for</span>&nbsp;_&nbsp;<span style="color:#ff3399">in</span>&nbsp;<span style="color:#4be6fa">range</span>(n)),&nbsp;key<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>lambda&nbsp;x:x[<span style="color:#c10aff">0</span>])</div><div style="padding:0 6px; white-space:pre; line-height:130%">answer&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;<span style="color:#c10aff">0</span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">for</span>&nbsp;i&nbsp;<span style="color:#ff3399">in</span>&nbsp;<span style="color:#4be6fa">range</span>(n):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;most_value(i<span style="color:#0086b3"></span><span style="color:#ff3399">+</span><span style="color:#c10aff">1</span>,&nbsp;li[i][<span style="color:#c10aff">0</span>],&nbsp;li[i][<span style="color:#c10aff">1</span>])</div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#4be6fa">print</span>(answer)</div></div><div style="text-align:right;margin-top:-13px;margin-right:5px;font-size:9px;font-style:italic"><a href="http://colorscripter.com/info#e" target="_blank" style="color:#4f4f4ftext-decoration:none">Colored by Color Scripter</a></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>

