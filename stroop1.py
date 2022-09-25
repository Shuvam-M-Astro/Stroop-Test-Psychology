"""
Basic stroop Task: VP responds to font color of congruent and
incongruent colored color words with keypresses.
Programming exercise: improve the code below!

Left = red
Center = green
Right = blue

Reaction time and error rate as dependent variables.
"""
import os
import sys
import datetime as dt
import random
import pandas as pd
from instructions import instructions
from objects import objects
from shuffle import shuffle
from response import response
from blockDVS import blockDVS
from expprms import expprms

from psychopy import visual, event, core

# #################### Experimental Parameters ################################
time,num,keys,prms = expprms()

# ######################### Files #############################################
# files = {"dirname": os.getcwd(), "filename": __file__}
files = {"dirname": os.getcwd(), "filename": "stroopTask1.py"}
files["expname"] = os.path.basename(files["filename"])[:-3]
files["date"] = dt.datetime.today().strftime("%d/%m/%Y")
files["insdir"] = files["dirname"] + os.sep + "Instructions"
files["resdir"] = files["dirname"] + os.sep + "Results"

# create results directory if required
if not os.path.isdir(files["resdir"]):
    os.makedirs(files["resdir"])

tmpName = files["resdir"] + os.sep + files["expname"]
files["resfile"] = tmpName + "_" + str(1) + ".res"


# ######################### Stimulus Sequence #################################
# Genrate stimulus sequence for the experiment. Trial information
# is contained within a 2D (blocks * trials) list of dicts.
words = ["red", "green", "green", "red"]
cols = ["red", "green"] * 2

stim = list(zip(words, cols))

# 2D list of dicts for blocks*trials
expSeq = [
    [{} for _ in range(prms["num"]["ntrls"])] for _ in range(prms["num"]["nblks"])
]

for iblk, blk in enumerate(expSeq):

    if iblk == 0:  # different number of trials in practise block
        stim_blk = stim * int((prms["num"]["nprac"] / len(stim)))
        practice = True
    else:
        stim_blk = stim * int((prms["num"]["ntrls"] / len(stim)))
        practice = False

    # shuffle stimuli in each block
    shuffle(random,stim_blk,blk,files,iblk,practice,prms)

# ######################### Read Instructions #################################

txtInst = instructions(os,files)

# ######################### PsychoPy Objects ##################################
win,stopWatch,instStim,fbStim,fixStim,stroopStim = objects(core,visual,txtInst)

# ######################### Block/Trial loop ##################################
for blk in expSeq:  # block loop

    blk = [x for x in blk if x]

    # show some instructions before first block and wait for key press
    if blk[0]["blk"] == 1:
        instStim.draw()
        win.flip()
        event.waitKeys(keyList=[prms["keys"]["cont"]])

    for trl in blk:  # trial loop

        # present fixation cross
        for _ in range(prms["time"]["fix"]):
            fixStim.draw()
            win.flip()

        # present stroop stimulus and reset stop watch
        stroopStim.text = trl["word"]
        stroopStim.color = trl["color"]
        stroopStim.draw()

        win.callOnFlip(stopWatch.reset)
        win.flip()

        # get response
        keysRT = event.waitKeys(
            maxWait=prms["time"]["slow"],
            keyList=prms["keys"]["resp"],
            timeStamped=stopWatch,
        )

        if keysRT:
            key, rt = keysRT[0]  # unpack first keypress/rt
        else:
            key, rt = "na", prms["time"]["slow"]

        # code response
        corr = response(prms,key,trl,rt,fbStim)

        # show feedback
        for _ in range(prms["time"]["feedback"]):
            fbStim.draw()
            win.flip()

        # update data dict
        trl["date"] = dt.datetime.now().strftime("%d-%m-%Y-%H:%M:%S")
        trl["key"] = key
        trl["rt"] = rt
        trl["corr"] = corr

        if key == "escape":
            win.close()
            core.quit()

        # blank screen for inter-trial-interval
        for _ in range(prms["time"]["iti"]):
            win.flip()

    # show block feedback and wait for keypress
    # calculate some block DVs
    blockDVS(blk,fbStim,win,event,prms)

    # blank screen for inter-trial-interval
    for _ in range(prms["time"]["iti"]):
        win.flip()

# ############################## Save Results #################################
# flatted 2D list of dicts
tmpData = [trial for data in expSeq for trial in data if trial]

# create pandas data frame
dataDF = pd.DataFrame()
dataDF = dataDF.from_dict(tmpData)

# make nice order
order = [
    "expname",
    "date",
    "blk",
    "trl",
    "practice",
    "word",
    "color",
    "comp",
    "corr_key",
    "key",
    "corr",
    "rt",
]
dataDF = dataDF[order]

# write to * .txt
dataDF.to_csv(files["resfile"], header=True, index=False, sep="\t", mode="w")

# close window and quit
win.close()
core.quit()
