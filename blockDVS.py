def blockDVS(blk,fbStim,win,event,prms):
    
    
    blk_num = blk[0]["blk"]
    num_trls = len(blk)
    rts = [x["rt"] for x in blk]
    blk_rt = (sum(rts) / len(rts)) * 1000
    corr = [x["corr"] for x in blk]
    blk_per = (corr.count(1) / num_trls) * 100

    fb_txt = "Block:{0}\nRT:{1:.0f} ms\nCorrect:{2:.0f}%".format(
        blk_num, blk_rt, blk_per
    )
    fb_txt = fb_txt + "\n\nPress the spacebar to continue."
    fbStim.text = fb_txt
    fbStim.draw()
    win.flip()
    event.waitKeys(keyList=[prms["keys"]["cont"]])