function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    var first,truck,last;
    var trucks = [];
    var total_weight = 0;
    while(truck_weights.length ){
        first = truck_weights[0];
        if (trucks.length==bridge_length){
            last = trucks.pop()
            total_weight -= last
        }
        if (total_weight + first <= weight){
            first = truck_weights.shift();
            trucks.unshift(first);
            total_weight += first;
        } else if (total_weight + first > weight){
            trucks.unshift(0)
        }
        answer += 1
        
    } answer += bridge_length
    return answer;
}

var bridge_length, weight, truck_weights;
var problem = [
    [2,10,[7,4,5,6]],
    [100,100,[10]],
    [100,100,[10,10,10,10,10,10,10,10,10,10]]
]
for (i=0;i<problem.length; i++){
    bridge_length = problem[i][0];
    weight = problem[i][1];
    truck_weights = problem[i][2];
    alert(solution(bridge_length, weight, truck_weights));
}