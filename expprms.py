def expprms():
    # timing
    time = {"fix": 30, "feedback": 30, "fast": 0.2, "slow": 2, "iti": 30}

    # block and trial numbers (multiples of 4 for trial numbers)
    num = {"nblks": 2, "nprac": 8, "ntrls": 16}

    # keys
    keys = {"cont": "space", "left": "s", "right": "k"}
    keys["resp"] = [keys["left"], keys["right"], "escape"]

    prms = {"time": time, "num": num, "keys": keys}
    
    return time,num,keys,prms