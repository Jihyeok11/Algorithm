function solution(array, commands) {
    var answer = [];
    var i,j,k,l,a,b,c;
    var li = []
    for (l=0;l<commands.length;l++){
        i=commands[l][0]-1
        j=commands[l][1]
        k=commands[l][2]-1
        li = array.slice(i,j)
        for (a=0;a<li.length-1;a++){
            for (b=a+1;b<li.length;b++){
                if (li[a] > li[b]){
                    c = li[a]
                    li[a] = li[b]
                    li[b] = c
                }
            }
        }
        answer.push(li[k])
    }
    return answer;
}

console.log(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))