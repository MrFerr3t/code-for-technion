import data
import numpy as np
import evaluation
import knn
from cross_validation import cross_validation_scores



df = data.load_data("london_sample_2500.csv")
folds = data.get_folds()



y = df['season'].values
y = data.adjust_labels(y)

X = df.drop(columns=['season']).values
X = data.add_noise(X)

k_list = [3, 5, 11, 25, 51, 75, 101]

print("Part1 - Classification")

mean_scores_class = []

for k in k_list:
    model = knn.ClassificationKNN(k)
    scores = cross_validation_scores(model, X, y, folds, evaluation.f1_score)


    mean_score = np.mean(scores)
    std_score = np.std(scores, ddof=1)
    mean_scores_class.append(mean_score)

    print(f"k={k}, mean score: {mean_score:.4f}, std of scores: {std_score:.4f}")

evaluation.visualize_results(k_list, mean_scores_class, "f1 score", "Classification", "classification_plot.pdf")


y = df['hum'].values


X = df.drop(columns=['season','hum']).values
X = data.add_noise(X)

k_list = [3, 5, 11, 25, 51, 75, 101]

print("Part2 - Regression")

mean_scores_class = []

for k in k_list:
    model = knn.RegressionKNN(k)
    scores = cross_validation_scores(model, X, y, folds, evaluation.rmse)


    mean_score = np.mean(scores)
    std_score = np.std(scores, ddof=1)
    mean_scores_class.append(mean_score)

    print(f"k={k}, mean score: {mean_score:.4f}, std of scores: {std_score:.4f}")

evaluation.visualize_results(k_list, mean_scores_class, "rmse", "Regression", "regression_plot.pdf")