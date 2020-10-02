if selectF1Lab.get() == 'Sustentation1':
        t = np.arange(float(timeInitF1Entry.get()),float(timeFinalF1Entry.get()),ts)
        tf = float(timeFinalF1Entry.get())
        ti =float(timeInitF1Entry.get())
        a = tf -ti
        conds = [(t <= ti+a/4) & (t>=ti), (t >= ti+a/4) & (t <= ti+2*a/4), (t > ti+2*a/4) & (t < ti+ 3*a/4) , (t >= ti+3*a/4) & (t <= ti+a)]
        funcs = [lambda t: (((t-(ti+a/4))**2)/(1))  ,
        lambda t: (-((t- (ti+2*a/4))**2)/(1)) + (a/4)**2,
        lambda t: (((t-(ti+3*a/4))**2)/(1)),
        lambda t: (-((t- (ti+a))**2)/(1)) + (a/4)**2]
        pieces = np.piecewise(t, conds, funcs)
        sustentGenerator = pieces
        plotF1TimeGeneratorStatus =  t
        plotF1GeneratorStatus = sustentGenerator
        canvasChange()
        print(sustentGenerator)
    if selectF1Lab.get() == 'Sustentation2':
        t = np.arange(float(timeInitF1Entry.get()),float(timeFinalF1Entry.get()),ts)
        tf = float(timeFinalF1Entry.get())
        ti =float(timeInitF1Entry.get())
        a = tf -ti
        conds = [(t <= ti+a/4) & (t>=ti), (t >= ti+a/4) & (t <= ti+2*a/4), (t > ti+2*a/4) & (t < ti+ 3*a/4) , (t >= ti+3*a/4) & (t <= ti+a)]
        funcs = [lambda t: (((t-(ti+a/4))**2)/(1))  ,
        lambda t: (-((t- (ti+2*a/4))**2)/(1)) + (a/4)**2,
        lambda t: (((t-(ti+3*a/4))**2)/(1)),
        lambda t: (-((t- (ti+a))**2)/(1)) + (a/4)**2]
        pieces = np.piecewise(t, conds, funcs)
        sustentGenerator = np.flip(pieces)
        plotF1TimeGeneratorStatus =  t
        plotF1GeneratorStatus = sustentGenerator
        canvasChange()
        print(sustentGenerator)