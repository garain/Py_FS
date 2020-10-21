import numpy as np
from sklearn import datasets
from _utilities import normalize

def PCC(data):
    # function that assigns scores to features according to Pearson's Correlation Coefficient (PCC)
    # the rankings should be done in increasing order of the PCC scores 
    feature_values = np.array(data)
    num_features = feature_values.shape[1]
    PCC_mat = np.zeros((num_features, num_features))
    PCC_values = np.zeros(num_features)

    mean_values = np.mean(feature_values, axis=0)
    for ind_1 in range(num_features):
        for ind_2 in range(num_features):
            numerator = np.sum((feature_values[:, ind_1] - mean_values[ind_1]) * (feature_values[:, ind_2] - mean_values[ind_2]))
            denominator = np.sqrt(np.sum(np.square(feature_values[:, ind_1] - mean_values[ind_1])) * np.sum(np.square(feature_values[:, ind_2] - mean_values[ind_2])))
            PCC_mat[ind_1, ind_2] = PCC_mat[ind_2, ind_1] = numerator/denominator

    for ind in range(num_features):
        PCC_values[ind] = -np.sum(abs(PCC_mat[ind,:]))

    PCC_scores = normalize(PCC_values)
    print(PCC_scores)

if __name__=='__main__':
    iris = datasets.load_iris()
    data = iris.data
    PCC(data)