function solution(absolutes, signs) {
    var answer = 0;
    var sign;
    for (var i=0;i<absolutes.length;i++){
        if (signs[i]==true){
            sign = 1
        }else{
            sign = -1
        }
        answer += sign * absolutes[i]
    }
    return answer;
}

consle.log(solution([4,7,12],	[true,false,true]))
console.log(solution([1,2,3],	[false,false,true]))