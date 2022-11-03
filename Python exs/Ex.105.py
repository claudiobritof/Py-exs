#Grades dictionary and analysis:

def grades(* g,sit=False):
    '''
    --> Function to analyze grades and situations of various students.
    :param g: 1 ou more grades from students (may be many).
    :param sit: (optional) indicates if it will show the situation.
    :return: dictionary with many info about class situation.
    '''
    r = {}
    r['total'] = len(g)
    r['biggest'] = max(g)
    r['smallest'] = min(g)
    r['average'] = sum(g) / len(g)
    if sit:
        if r['average'] >= 7:
            r['sit'] = 'GOOD'
        elif r['average'] >= 5:
            r['sit'] = 'OK'
        else:
            r['sit'] = 'BAD'

    return r

r = grades(9,10,5.5,2.5,8.5,sit=True)
print(r)