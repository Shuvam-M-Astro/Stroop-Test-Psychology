def response(prms,key,trl,rt,fbStim):
    
    tooSlow = prms["time"]["slow"]
    tooFast = prms["time"]["fast"]
    if key == trl["corr_key"] and tooFast < rt < tooSlow:
        corr = 1
        fbStim.text = "Correct"
    elif key != trl["corr_key"] and tooFast < rt < tooSlow:
        corr = 2
        fbStim.text = "Incorrect"
    elif rt >= tooSlow:
        corr = 3
        fbStim.text = "Too Slow"
    elif rt < tooFast:
        corr = 4
        fbStim.text = "Too Fast"
        
    return corr
   