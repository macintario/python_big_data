from sklearn.neighbors import KNeighborsClassifier

features, labels = load_dataset('iris-dataset')
sklearn_knn = KNeighborsClassifier(n_neighbors=3)
sklearn_knn.fit(features, labels)

for test in testing_set:
    if sklearn_knn.predict(test) == your_knn(test, features, labels, k = 1):
        print("Error in " + str(test))