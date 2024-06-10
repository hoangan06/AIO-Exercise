def calc_classification_scores(tp, fp, fn):
    if type(tp) != int:
        return print('tp must be int')
    if type(fp) != int:
        return print('fp must be int')
    if type(fn) != int:
        return print('fn must be int')
    if (tp <= 0) or (fp <= 0) or (fn <= 0):
        return print('tp and fp and fn must be greater than zero')
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1_score = 2*(precision*recall)/(precision+recall)
    print(f'precision is {precision}')
    print(f'recall is {recall}')
    print(f'f1-score is {f1_score}')

calc_classification_scores(tp=2, fp=4, fn=5)