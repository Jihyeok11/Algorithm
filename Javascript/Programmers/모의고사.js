function solution(answers) {
    var p;
    var answer = [];
    var basket = [0,0,0]
    p = [
        [1,2,3,4,5] , [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for (var j =0;j<3;j++){
        for (var i=0; i<answers.length; i++){
            if (p[j][i%(p[j].length)] == answers[i]){
                basket[j] += 1
            }
        }
    }
    var Maxval = Math.max(...basket)
    for (i=0;i<3;i++){
        if (Maxval == basket[i]){
            answer.push(i+1)
        }
    }
    console.log(basket)
    return answer;
}


var answers = [1,2,3,4,5]
alert(solution(answers))