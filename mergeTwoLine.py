with open('./input122') as f:
    my_lines = f.readlines()
    prevLine = ""
    imps = dict()
    clicks = dict()
    for line in my_lines:
        line = line.strip()
        currLineSplits = line.split()

        currLineid = currLineSplits[0]
        if imps.get(currLineid):
            imps[currLineid] += int(currLineSplits[3])
        else:
            imps[currLineid] = int(currLineSplits[3])
        if clicks.get(currLineid):
            clicks[currLineid] += int(currLineSplits[4])
        else:
            clicks[currLineid] = int(currLineSplits[4])
        if prevLine:
            prevLineSplits = prevLine.split()
            if prevLineSplits[1] == currLineSplits[1]:
                prevLineSplits[3] = str(int(prevLineSplits[3]) + int(currLineSplits[3]))
                prevLineSplits[4] = str(int(prevLineSplits[4]) + int(currLineSplits[4]))
                prevLine = '  '.join(prevLineSplits)
            else:
                print prevLine
                prevLine = line
        else:
            prevLine = line

    for line, impression in imps.iteritems():
        click = clicks.get(line)
        print line, "1", impression, click #, float(click) / float(impression)
