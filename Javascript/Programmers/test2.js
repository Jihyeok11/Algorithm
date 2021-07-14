function solution(money, cost) {
    var answer = 0;
    for (var i = 0; i < cost.length; i++) {
        var point = 0
        var vol = money
        for (var j = i; j < cost.length; j++) {
            if (vol - cost[j] >= 0) {
                point += 1
                vol -= cost[j]
            } else {
                break
            }
        }
        if (point > answer) {
            answer = point
        }
        if ( cost.length - i <= answer) {
            break
        }
    }
    
    return answer;
}


document.writeln(solution(420,	[0, 900, 0, 200, 150, 0, 30, 50]))