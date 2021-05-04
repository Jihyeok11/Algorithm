function solution(n, lost, reserve) {
    var answer = 0;
    var li = [];
    var i;
    for (i=0;i<n;i++){
        li.push(1)
    }
    for (i=0;i<lost.length;i++){
        li[lost[i]-1] -= 1
    }
    for (i=0;i<reserve.length;i++){
        li[reserve[i]-1] += 1
    }
    console.log(li)
    for (i=0;i<n;i++){
        if (li[i]>=1){
            answer += 1
        }else if (li[i]==0){
            if (i>0 && li[i-1]==2){
                answer += 1
            } else if (i<n-1 && li[i+1]==2){
                li[i+1] -= 1
                answer += 1
            }
        }
    }
    return answer;
}

document.writeln(solution(5,[2,4],[1,3,5]))
document.writeln(solution(5,[2,4],[3]))
document.writeln(solution(3,[3],[1]))