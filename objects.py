def objects(core,visual,txtInst):


    # create window
    win = visual.Window(size=(640, 480), color=(0, 0, 0), units="pix")

    # create timer
    stopWatch = core.Clock()

    # create stimuli
    instStim = visual.TextStim(win, text=txtInst["inst1"])
    fbStim = visual.TextStim(win)
    fixStim = visual.ShapeStim(
        win,
        lineWidth=2,
        lineColor="white",
        pos=(0, 0),
        vertices=((-10, 0), (10, 0), (0, 0), (0, 10), (0, -10)),
        closeShape=False,
    )
    stroopStim = visual.TextStim(win, height=32)
    
    return win,stopWatch,instStim,fbStim,fixStim,stroopStim