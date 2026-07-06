import data
import clustering
import numpy as np

print("Part A:  ")
df = data.load_data("london.csv")
df = data.add_new_columns(df)
data.data_analysis(df)

print("\nPart B: ")
features = ['hum', 'wind_speed']
transformed_data = clustering.transform_data(df, features)

for i, k in enumerate([3, 4, 6]):
    labels, centroids = clustering.kmeans(transformed_data, k)

    print(f"k = {k}")
    print(np.array_str(centroids, precision=3, suppress_small=True))
    if i < 2:
        print()


    plot_path = f"plot_{k}.png"
    clustering.visualize_results(transformed_data, labels, centroids, plot_path)