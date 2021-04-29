function solution(lottos, win_nums) {
    var answer = [];
    var result = 0;
    var cntZero = 0;
    var lottoResult= [6,6,5,4,3,2,1]
    for(var i=0;i<6;i++){
        if (lottos[i]==0){
            cntZero += 1
        }else{
            if (win_nums.includes(lottos[i])){
                result += 1
            }
        }
    }
    answer.push(lottoResult[cntZero+result])
    answer.push(lottoResult[result])
    return answer
}
document.write(solution([44, 1, 0, 0, 31, 25],	[31, 10, 45, 1, 6, 19]))
document.write(solution([0, 0, 0, 0, 0, 0],	[38, 19, 20, 40, 15, 25]))
document.write(solution([45, 4, 35, 20, 3, 9],	[20, 9, 3, 45, 4, 35]))