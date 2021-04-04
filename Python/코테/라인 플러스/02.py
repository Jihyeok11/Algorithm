def solution(ball, order):
    reservation = []
    answer = []
    
    for i in order:
        left = ball[0]
        right = ball[-1]
        flag = True
        while flag == True and reservation:
            if left in reservation:
                reservation.pop(reservation.index(left))
                answer.append(ball.pop(0))
                left = ball[0]
            elif right in reservation:
                reservation.pop(reservation.index(right))
                answer.append(ball.pop())
                right = ball[-1]
            else:
                flag = False
        
        if i == left:
            answer.append(ball.pop(0))
        elif i == right:
            answer.append(ball.pop())
        else:
            reservation.append(i)
    print(answer)
    return answer



ball = [1, 2, 3, 4, 5, 6]
order = [6, 2, 5, 1, 4, 3]
result = [6, 5, 1, 2, 4, 3]
solution(ball, order)