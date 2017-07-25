#In this case study, we will analyze a dataset consisting of an assortment of wines classified as "high quality" and "low quality" and will use the k-Nearest Neighbors classifier to determine whether or not other information about the wine helps us correctly predict whether a new wine will be of high quality.

#Part 1
#Read in the data as a pandas dataframe using pd.read_csv. The data can be found at https://s3.amazonaws.com/demo-datasets/wine.csv.
import pandas as pd
data = pd.read_csv('https://s3.amazonaws.com/demo-datasets/wine.csv')

#Part 2
#The dataset remains stored as data. Two columns in data are is_red and color, which are redundant. Drop color from the dataset, and save the new dataset as numeric_data.
numeric_data = data.drop('color',axis=1)
print(numeric_data)

#part 3
#To ensure that each variable contributes equally to the kNN classifier, we need to standardize the data. 
#First, from each variable in numeric_data, subtract its mean. Second, for each variable in numeric_data, divide by its standard deviation. Store your standardized result as numeric_data.
#Principal component analysis is a way to take a linear snapshot of the data from several different angles, with each snapshot ordered by how well it aligns with variation in the data. The sklearn.decomposition module contains the PCA class, which determines the most informative principal components of the data (a matrix with columns corresponding to the principal components). Use pca.fit(numeric_data).transform(numeric_data) to extract the first two principal components from the data. Store this as principal_components.

numeric_data = (numeric_data - np.mean(numeric_data)) / np.std(numeric_data) # Enter your code here!
print(numeric_data)

import sklearn.decomposition
pca = sklearn.decomposition.PCA(n_components=2)
principal_components = pca.fit(numeric_data).transform(numeric_data)

#part 4
#The first two principal components can be accessed using principal_components[:,0] and principal_components[:,1]. 
#Store these as x and y respectively, and plot the first two principal components. The high and low quality wines will be colored using red and blue. How well are the two groups of wines separated by the first two principal components?

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.backends.backend_pdf import PdfPages
observation_colormap = ListedColormap(['red', 'blue'])
x = principal_components[:,0]# Enter your code here!
y = principal_components[:,1]# Enter your code here!

plt.title("Principal Components of Wine")
plt.scatter(x, y, alpha = 0.2,
    c = data['high_quality'], cmap = observation_colormap, edgecolors = 'none')
plt.xlim(-8, 8); plt.ylim(-8, 8)
plt.xlabel("Principal Component 1"); plt.ylabel("Principal Component 2")
plt.show()

#part 5
#We are now ready to fit the wine data to our kNN classifier. Create a function accuracy(predictions, outcomes) that takes two lists of the same size as arguments and returns a single number, which is the percentage of elements that are equal for the two lists.
Use accuracy to compare the percentage of similar elements in x = np.array([1,2,3]) and y = np.array([1,2,4]).
Print your answer.#

def accuracy(predictions, outcomes):
    for i in predictions:
        for j in outcomes:
            if i == j:
                percentage = 100 * np.mean(predictions == outcomes)
    return percentage
    # Enter your code here!
x = np.array([1,2,3])
y = np.array([1,2,4])

print(accuracy(x,y))

#part 6
#The dataset remains stored as data. Because most wines in the dataset are classified as low quality, one very simple classification rule is to predict that all wines are of low quality. Use the accuracy function (preloaded into memory as defined in Exercise 5) to calculate how many wines in the dataset are of low quality. Accomplish this by calling accuracy with 0 as the first argument, and data["high_quality"] as the second argument.
#Print your result.

# Enter code here!
low = accuracy(0,data["high_quality"])
print(low)


#part 7
#Use knn.predict(numeric_data) to predict which wines are high and low quality and store the result as library_predictions.
#Use accuracy to find the accuracy of your predictions, using library_predictions as the first argument and data["high_quality"] as the second argument.
#Print your answer. Is this prediction better than the simple classifier in Exercise 6? - yes

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(numeric_data, data['high_quality'])
# Enter your code here!
library_predictions = knn.predict(numeric_data)
print(accuracy(library_predictions, data["high_quality"]))

#part 8
#Unlike the scikit-learn function, our homemade kNN classifier does not take any shortcuts in calculating which neighbors are closest to each observation, so it is likely too slow to carry out on the whole dataset. To circumvent this, fix the random generator using random.seed(123), and select 10 rows from the dataset using random.sample(range(n_rows), 10). Store this selection as selection.
import random
n_rows = data.shape[0]
# Enter your code here.

random.seed(123)
selection = random.sample(range(n_rows),10)


#part 9
#The sample of 10 row indices are stored as selection from the previous exercise. For each predictor p in predictors[selection], use knn_predict(p, predictors[training_indices,:], outcomes, k=5) to predict the quality of each wine in the prediction set, and store these predictions as a np.array called my_predictions. Note that knn_predict is already defined as in the Case 3 videos.
#Using the accuracy function, compare these results to the selected rows from the high_quality variable in data using my_predictions as the first argument and data.high_quality[selection] as the second argument. Store these results as percentage.
#Print your answer.

predictors = np.array(numeric_data)
training_indices = [i for i in range(len(predictors)) if i not in selection]
outcomes = np.array(data["high_quality"])

my_predictions = np.array([knn_predict(p, predictors, outcomes, 5) for p in predictors[selection]]) # Enter your code here!

percentage = accuracy(my_predictions, data.high_quality[selection])

# Enter your code here!

print(percentage)

#Great work! Our accuracy is comparable to the library's function! This concludes the case study. 
