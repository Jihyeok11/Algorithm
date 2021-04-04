def solution(cards):
    answer = 0
    while cards:
        if cards: # 첫번째 드로우
            card = cards.pop(0)
            if card>=10:
                Player = [10]
            else:
                Player = [card]
        else:
            break
        if cards: # 두번째 드로우
            card = cards.pop(0)
            if card>=10:
                dealer = [10]
            else:
                dealer = [card]
        else:
            break
        if cards: # 세번째 드로우
            card = cards.pop(0)
            if card>=10:
                Player.append(10)
            else:
                Player.append(card)
        else:
            break
        if cards: # 네번째 드로우
            show  = cards.pop(0)
            if show>=10:
                dealer.append(10)
            else:
                dealer.append(show)
        else:
            break
            
        if 1 in Player and sum(Player)==11: # 둘 다 블랙젝
            answer += 3
            if 1 in dealer and sum(dealer)==11:
                answer -= 3
                # print("무승부",answer)

                continue # 돌아가    
            continue 
            
        if show==1 or show>=7: # 플레이어 조건 시작
            if 1 in Player:
                Sum = sum(Player) + 10
            else:
                Sum = sum(Player)
            while cards and Sum<17: # 17이상이 될 때 까지
                card = cards.pop(0)
                if card >= 10:
                    Player.append(10)
                    Sum += 10
                elif card == 1:
                    Player.append(1)
                    Sum += 10
                else:
                    Player.append(card)
                    Sum += card
        elif show == 2 or show ==3:
            if 1 in Player:
                Sum = sum(Player) + 10
            else:
                Sum = sum(Player)
            while cards and Sum>=12:
                card = cards.pop(0)
                if card >= 10:
                    Player.append(10)
                elif card == 1:
                    Player.append(1)
                    Sum += 10
                else:
                    Player.append(card)
                    Sum += card
        if 1 in Player:
            Player_sum = sum(Player) + 10
            if Player_sum > 21:
                Player_sum -= 10
        elif not 1 in Player:
            Player_sum = sum(Player)
        
        if Player_sum > 21: # 21 넘을 때
            if 1 in dealer:
                dealer_sum = sum(dealer)+10
                if dealer_sum > 21:
                    dealer_sum -= 10
            else:
                dealer_sum = sum(dealer)
            
            if dealer_sum > 21: # 무승부
                # print("무승부",Player_sum,dealer_sum)
                continue
            
            else: # 딜러 승
                answer -= 2
                # print("딜러승",Player_sum,dealer_sum)

                continue
            
        elif 1 in dealer: # 딜러한테 1이 있을 때
            dealer_sum = sum(dealer) + 10
            while dealer_sum < 17:
                if cards:
                    card = cards.pop(0)
                    if card >= 10:
                        dealer.append(10)
                        dealer_sum += 10
                    elif card == 1:
                        dealer.append(1)
                        dealer_sum += 11
                    else:
                        dealer.append(card)
                        dealer_sum += card
    
        elif not 1 in dealer: # 딜러한테 1 없을 때
            dealer_sum = sum(dealer)
            while dealer_sum < 17:
                if cards:
                    card = cards.pop(0)
                    if card >= 10:
                        dealer.append(10)
                        dealer_sum += 10
                    elif card == 1:
                        dealer.append(1)
                        dealer_sum += 11
                    else:
                        dealer.append(card)
                        dealer_sum += card
                else:
                    dealer_sum = 22
                    Player_sum = 22
                    continue
                
        
        if Player_sum == 21:
            if dealer_sum == 21:
                continue
            else:
                answer += 3
        
        elif Player_sum > dealer_sum:
            if Player_sum > 21:
                if dealer_sum > 21:
                    continue
                else:
                    answer -= 2
            else:
                answer += 2
        elif Player_sum < dealer_sum:
            if dealer_sum > 21:
                if Player_sum > 21:
                    continue
                else:
                    answer += 2
            else:
                answer -= 2
    
    
    return answer


cards = [12, 7, 11, 6, 2, 12]
cards = [1, 4, 10, 6, 9, 1, 8, 13]
# cards = [10, 13, 10, 1, 2, 3, 4, 5, 6, 2]
# cards = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
solution(cards)