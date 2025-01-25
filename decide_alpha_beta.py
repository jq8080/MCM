def decide_alpha_beta():
    min=inf;
    for i in range(1,10):
        for j in range(1,10):
            calculate_predicting_scores(i,j);


def calculate_prdicting_score(a,b):
    score=0
    for row_id in range(0,row_num):
        for  coloum_id in range(0,coloum_num):
            score=score+a[row_id][coloum_id]*b[row_id][coloum_id]
    return score

