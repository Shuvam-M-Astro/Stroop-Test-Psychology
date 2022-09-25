def instructions(os,files):
    
    txtInst = {}
    for fname in os.listdir(files["insdir"]):
        if fname.endswith(".txt"):
            with open(os.path.join(files["insdir"], fname), "r") as f:
                txtInst[os.path.splitext(fname)[0]] = f.read()
                
    return txtInst            