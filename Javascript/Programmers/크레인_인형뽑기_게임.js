function solution(board, moves) {
    var answer = 0;
    var basket = [];
    var a = 0;
    for (var i = 0; i< moves.length; i++){
        a = moves[i]-1;
        for (var j =0; j<board[0].length; j++){
            if (board[j][a] != 0){
                if (basket[basket.length-1] == board[j][a]){
                    basket.pop();
                    answer += 2;
                } else {
                    basket.push(board[j][a]);
                }
                board[j][a] = 0;
                break;
            }
        }
    }
    return answer;
}

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]);