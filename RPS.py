def player(prev_play, opponent_history=[], play_order={}):
    if not prev_play:
        prev_play = 'R'
        opponent_history.clear()
        play_order.clear()
        
    opponent_history.append(prev_play)
    
    for i in range(1, 6):
        if len(opponent_history) > i:
            pattern = "".join(opponent_history[-(i+1):])
            play_order[pattern] = play_order.get(pattern, 0) + 1
            
    prediction = 'P'
    
    for i in range(5, 0, -1):
        if len(opponent_history) >= i:
            last_moves = "".join(opponent_history[-i:])
            potential_plays = [
                last_moves + "R",
                last_moves + "P",
                last_moves + "S",
            ]
            
            sub_order = {k: play_order[k] for k in potential_plays if k in play_order}
            
            if sub_order:
                prediction = max(sub_order, key=sub_order.get)[-1]
                break
                
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    
    return ideal_response[prediction]