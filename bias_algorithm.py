
# REFER TO WEFAT FOR EQUATION 
# https://arxiv.org/pdf/1608.07187
import numpy as np
# Let a and b be vectors from word embedding 
def _cosine_similarity(a,b):
    numerator = a.dot(b)
    return (numerator) / (np.linalg.norm(a)*np.linalg.norm(b))


# Let w be target word 
# a be one set of attributes 
# b be the other set of attributes 
# This will measure 
def SC_WEAT(w,a,b):
    # Determining mean of w and a
    w_a = (sum([_cosine_similarity(w,word) for word in a]))/len(a)
    # Determining mean of w and b 
    w_b = (sum([_cosine_similarity(w,word) for word in b]))/len(b)
    total_list = a + b
    std_to_measure =[_cosine_similarity(w, x) for x in total_list]
    return (w_a - w_b)/np.std(std_to_measure, ddof=1)




    