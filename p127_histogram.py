
def zeichen_im_wort(string):
    dikt = {}
    for zeichen in string:
        dikt[zeichen] = dikt.get(zeichen, 0) + 1
    return dikt


d = zeichen_im_wort('eresputamuyputaputissima')

for item in sorted(d):
    print(item, d[item])
