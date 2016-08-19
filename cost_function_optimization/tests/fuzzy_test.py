from sklearn.datasets import *
import numpy as np
import matplotlib.pyplot as plt
from cost_function_optimization import fuzzy_clustering


import unittest


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    #@unittest.skip("no")
    def testBlobs(self):
        X, y = make_blobs(n_samples=1000, centers=3, n_features=2,random_state=10)
        X = fuzzy_clustering.fuzzy(X, 3)
        plot_data_util(X)
        
    #@unittest.skip("no")
    def testCircles(self):
        X, y = make_circles(n_samples=1000, shuffle = True, noise = 0.05, factor = 0.5, random_state = 10)
        X = X = fuzzy_clustering.fuzzy(X, 3)
        plot_data_util(X)
        
    #@unittest.skip("no")
    def testMoons(self):
        X, y = make_moons(n_samples=1000, shuffle = True, noise = 0.1, random_state = 10)
        X = X = fuzzy_clustering.fuzzy(X, 3)
        X = plot_data_util(X)
        
    
    
def plot_data_util(X):
    np.random.seed(seed = 10)
    clusters = np.unique(X[:, 2])
    #colors = ['r', 'b','g', 'm', 'y', 'c', 'k','w']
    for i, cluster in enumerate(clusters):
        plt.scatter(X[ X[:,2] == cluster, 0], X[ X[:, 2] == cluster, 1], c=np.random.rand(3,1), s = 30)
    plt.show()



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()