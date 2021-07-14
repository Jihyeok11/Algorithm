function solution(k, rates) {
    var answer = k;
    var ba = [k, true]
    for (var i = 0; i < rates.length; i++) {
        baLeng = ba.length / 2;
        for (var j = 0; j < baLeng; j ++) {
            var money = ba.shift();
            var dollar = ba.shift();
            ba.push(money)
            ba.push(dollar)
            if (dollar == false) {
                ba.push(money + rates[i])
                ba.push(true)
                if (money + rates[i] > answer) {
                    answer = money + rates[i]
                }
            }
            if (money >= rates[i] && dollar) {
                ba.push(money - rates[i])
                ba.push(false)
            }
        }
    }
    return answer;
}

document.writeln(solution(1000,	[1200, 1000, 1100, 1200, 900, 1000, 1500, 900, 750, 1100]))
document.writeln(solution(1500,	[1500, 1400, 1300, 1200]))