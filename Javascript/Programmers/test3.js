function tack(y,x, block, board) {
    var ret = 0;
    if (block == 0){
        board[y][x] = 1
        if (y+1<board.length && board[y+1][x]==0){
            board[y+1][x] = 1
            if (y+2 < board.length && board[y+2][x] == 0) {
                board[y+2][x] = 1
                for (var cy = y; cy < y+3; cy ++){
                    var flag = 1
                    for (var cx = 0; cx < board.length; cx++){
                        if (board[cy][cx] == 0 ){
                            flag = 0
                            break
                        }
                    }
                    if (flag==1){
                        ret += 1
                    }
                }
                board[y+2][x] = 0
                board[y+1][x] = 0
                board[y][x] = 0
                return ret
            }
            else {
                board[y+1][x] = 0
                board[y][x] = 0
                return -1
            }
        }
        else{
            board[y][x] = 0
            return -1;
        }
    }
    else if (block == 1){
        board[y][x] = 1
        if ( x+1 < board.length && board[y][x+1] == 0){
            board[y][x+1] = 1
            if (x+2 < board.length && board[y][x+2] == 0){
                board[y][x+2] = 1
                var flag = 1
                for (var cx = 0; cx<board.length; cx++){
                    if (board[y][cx] == 0){
                        flag = 0
                        break
                    }
                }
                if (flag==1){
                    ret += 1
                }
                board[y][x] = 0
                board[y][x+1] = 0
                board[y][x+2] = 0
                return ret
            }
            else {
                board[y][x] = 0
                board[y][x+1] = 0
                return -1
            }
        }
        else {
            board[y][x] = 0
            return -1
        }

    }
    else if (block == 2){
        board[y][x] = 1
        if (y+1 < board.length && board[y+1][x] == 0) {
            board[y+1][x] = 1
            if (x+1 < board.length && board[y+1][x+1] == 0) {
                board[y+1][x+1] = 1
                for (var cy = y; cy < y+2; cy++){
                    var flag = 1
                    for (var cx = 0; cx < board.length; cx++){
                        if (board[cy][cx] == 0){
                            flag = 0
                            break
                        }
                    }
                    if (flag ==1){
                        ret += 1
                    }
                }
                board[y][x] = 0
                board[y+1][x] = 0
                board[y+1][x+1] = 0
                return ret
            }else{
                board[y][x] = 0
                board[y+1][x] = 0
                return -1
            }
        }else {
            board[y][x] = 0
            return -1
        }
    }
    else if (block == 3){
        board[y][x] = 1
        if (y+1 < board.length && board[y+1][x] == 0) {
            board[y+1][x] = 1
            if (x-1 >= 0 && board[y+1][x-1] == 0) {
                board[y+1][x-1] = 1
                for (var cy = y; cy < y+2; cy++){
                    var flag = 1
                    for (var cx = 0; cx < board.length; cx++){
                        if (board[cy][cx] == 0){
                            flag = 0
                            break
                        }
                    }
                    if (flag ==1){
                        ret += 1
                    }
                }
                board[y][x] = 0
                board[y+1][x] = 0
                board[y+1][x-1] = 0
                return ret
            }else{
                board[y][x] = 0
                board[y+1][x] = 0
                return -1
            }
        }else {
            board[y][x] = 0
            return -1
        }
    }
    else if (block == 4){
        board[y][x] = 1
        if (x+1 < board.length && board[y][x+1] == 0) {
            board[y][x+1] = 1
            if (y+1 < board.length && board[y+1][x+1] == 0) {
                board[y+1][x+1] = 1
                for (var cy = y; cy < y+2; cy++){
                    var flag = 1
                    for (var cx = 0; cx < board.length; cx++){
                        if (board[cy][cx] == 0){
                            flag = 0
                            break
                        }
                    }
                    if (flag ==1){
                        ret += 1
                    }
                }
                board[y][x] = 0
                board[y][x+1] = 0
                board[y+1][x+1] = 0
                return ret
            }else{
                board[y][x] = 0
                board[y][x+1] = 0
                return -1
            }
        }else {
            board[y][x] = 0
            return -1
        }
    }
    else if (block == 5){
        board[y][x] = 1
        if (x-1 >=0 && board[y][x-1] == 0) {
            board[y][x-1] = 1
            if (y+1 < board.length && board[y+1][x-1] == 0) {
                board[y+1][x-1] = 1
                for (var cy = y; cy < y+2; cy++){
                    var flag = 1
                    for (var cx = 0; cx < board.length; cx++){
                        if (board[cy][cx] == 0){
                            flag = 0
                            break
                        }
                    }
                    if (flag ==1){
                        ret += 1
                    }
                }
                board[y][x] = 0
                board[y][x-1] = 0
                board[y+1][x-1] = 0
                return ret
            }else{
                board[y][x] = 0
                board[y][x-1] = 0
                return -1
            }
        }else {
            board[y][x] = 0
            return -1
        }
    }
}

function solution(block,board) {
    var answer = -1;
    for(var y = 0; y < board.length; y++){
        for (var x = 0; x < board[y].length; x++){
            if (board[y][x] == 0){
                console.log(y +"\t" + x)
                var res = tack(y,x,block,board)
                console.log(res + "\n")
                if (res > answer) {
                    answer = res
                }
            }
            if (answer == 3){
                break
            }
        }
        if (answer ==3 ) {
            break
        }
    }
    if (answer == 0){
        answer = -1
    }

    return answer;
}

// document.writeln(solution(5,	[[1,0,0,0],[1,0,0,1],[1,1,0,1],[1,1,0,1]]))
document.writeln(solution(4,	[[1,0,0,0],[1,0,0,1],[1,1,0,1],[1,1,0,1]]))