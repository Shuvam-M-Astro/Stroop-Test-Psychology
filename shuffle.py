def shuffle(random,stim_blk,blk,files,iblk,practice,prms):

    random.shuffle(stim_blk)

    for itrl, trl in enumerate(blk):

        if itrl >= len(stim_blk):  # empty dict positions
            break


        trl["expname"] = files["expname"]
        trl["blk"] = iblk + 1  # python 0 index!
        trl["trl"] = itrl + 1
        trl["practice"] = practice

        # code stimulus
        trl["word"] = stim_blk[itrl][0]
        trl["color"] = stim_blk[itrl][1]

        if trl["word"] == trl["color"]:
            trl["comp"] = "comp"
        else:
            trl["comp"] = "incomp"

        # code response
        if trl["color"] == "red":
            trl["corr_key"] = prms["keys"]["left"]
        elif trl["color"] == "green":
            trl["corr_key"] = prms["keys"]["right"]