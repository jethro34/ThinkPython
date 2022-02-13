def invert_dict(d):
    dikt = {}
    for kee in d:
        dikt.setdefault(d[kee], []).append(kee)
    return dikt


d1 = {'Justi': 20,
      'Lulu': 12,
      'Leo': 12,
      'Aly': 10,
      'Ely': 10}

d2 = invert_dict(d1)

for key in d2:
    print(key, d2[key])
