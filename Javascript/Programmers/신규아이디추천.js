function solution(new_id) {
    var answer = '';
    var wordlist1 = [];
    var wordlist = [];
    var code, first;
    var dot_flag = false;
    // console.log('0'.charCodeAt(0))//48
    // console.log('9'.charCodeAt(0))//57
    // console.log('-'.charCodeAt(0))//45
    // console.log('_'.charCodeAt(0))//95
    // console.log('.'.charCodeAt(0))//4
    // console.log('{'.charCodeAt(0))//4
    // console.log('~'.charCodeAt(0))//4
    for(var i=0;i<new_id.length;i++){ // 1단계
        code = new_id[i]
        if ( code.charCodeAt(0)>=65 && code.charCodeAt(0)<=90){
            wordlist1.push(String.fromCharCode(code.charCodeAt(0)+32))
        } else if( (code.charCodeAt(0)>=97 && code.charCodeAt(0)<=122) ||
                (code.charCodeAt(0)>=48 && code.charCodeAt(0)<=57) || 
                (code.charCodeAt(0)==46) ||
                (code.charCodeAt(0)==45) || (code.charCodeAt(0)== 95) ){
            wordlist1.push(code)
        }
    }
    while (wordlist1.length){
        first = wordlist1.shift();
        if (first=="."){
            
            if (dot_flag==false){
                dot_flag=true;
                wordlist.push(first)
            }
        }
        else {
            dot_flag=false;
            wordlist.push(first)
        }
    }
    if (wordlist[0]=="."){ // 3단계
        wordlist.shift()
    }
    if (wordlist[wordlist.length-1]=="."){
        wordlist.pop()
    }
    if (wordlist.length==0){
        wordlist.push('a')
    }
    for (var i=0;i<wordlist.length;i++){// 6단계
        if (i==15){
            break;
        }
        answer += wordlist[i]
    }
    if (answer[answer.length -1] =="."){ 
        answer = answer.slice(0,-1)
    }
    while (answer.length<3){
        answer += answer[answer.length-1]
    }
    
    return answer;
}

console.log(solution("...!@BaT#*..y.abcdefghijklm",	"bat.y.abcdefghi"))
console.log(solution("z-+.^.",	"z--"))
console.log(solution("=.=",	"aaa"))
console.log(solution("123_.def",	"123_.def"))
console.log(solution("abcdefghijklmn.p",	"abcdefghijklmn"))