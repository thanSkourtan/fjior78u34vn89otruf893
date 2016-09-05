import matplotlib.pyplot as plt
import numpy as np
    
    
def plot_data(X, centroids, no_of_clusters, centroids_history = None ):
    
    # Initialization
    m = len(X[0])
    np.random.seed(seed = None)
    clusters = np.unique(X[:, m - 1])
    
    # Initialize plots
    f, initDataPlot = plt.subplots(2, sharex=True,  figsize = (12,8))
    f.canvas.set_window_title('Unclustered and Clustered Data')
    #plt.tight_layout()

    initDataPlot[0].set_title('Initial Data')
    initDataPlot[0].set_xlabel('Feature 1')
    initDataPlot[0].set_ylabel('Feature 2')
    
    initDataPlot[1].set_title('Clustered Data')
    initDataPlot[1].set_xlabel('Feature 1')
    initDataPlot[1].set_ylabel('Feature 2')
    
    
    # Plot initial data set without clustering
    initDataPlot[0].scatter(X[:, 0], X[:, 1])
    
    # Plot data after clustering
    for i, cluster in enumerate(clusters):
        initDataPlot[1].scatter(X[ X[:,2] == cluster, 0], X[ X[:, 2] == cluster, 1], c=np.random.rand(3,1), s = 30)
    
    # Plots the centroids history
    if centroids_history != None:
        colors= ['k', 'b', 'g', 'y', 'm', 'c']
        for alpha_counter, i in enumerate(range(0, len(centroids_history),  no_of_clusters)):
            for j in range(i, i + no_of_clusters):
                initDataPlot[1].plot(centroids_history[j, 0], centroids_history[j, 1], c = colors[j % len(colors)], marker = 'x', mew =  1, ms = 15, alpha = 0.2 + alpha_counter * 0.8/(len(centroids_history)/no_of_clusters))
            
    # Plots the centroids
    for i, c in enumerate(centroids):
            initDataPlot[1].plot(centroids[i, 0], centroids[i, 1], c = 'r', marker = 'x', mew=2, ms = 10)
    
    
   

def hist_internal_criteria(initial_gamma, list_of_gammas, result):
    f, ax = plt.subplots(figsize = (12,8))
    f.canvas.set_window_title('Internal Criteria')
    n, bins, patches = plt.hist(list_of_gammas, bins = 50, color = 'g')
    ax.hist(initial_gamma, bins = 50, color = 'r')
    
    #bincenters = 0.5*(bins[1:]+bins[:-1])
    #y = norm.pdf(bincenters, np.mean(list_of_gammas), np.std(list_of_gammas))
    #ax.plot(bincenters, y, 'r--', linewidth=1)
    
    ax.set_title(result)
    #f.suptitle(result)
    ax.set_xlabel('Hubert\'s Gamma Values')
    ax.set_ylabel('Probability')
    
    plt.tight_layout()



def hist_external_criteria(initial_indices, list_of_indices, result_list):
    
    f1,  ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2,  figsize = (12,8))
    f1.canvas.set_window_title('External Criteria')

    figure_subplots = (ax1, ax2, ax3, ax4)
    names_of_indices = ['Rand statistic', 'Jaccard coefficient', 'Fowlkes and Mallows', 'Hubert\'s Gamma']
    for i in range(len(result_list)):
        n, bins, patches = figure_subplots[i].hist(list_of_indices[i, :], bins = 50, color = 'g',histtype='stepfilled')
        figure_subplots[i].hist(initial_indices[i], bins = [initial_indices[i], initial_indices[i] + 5*(bins[1] - bins[0])], color = 'r')
        # in case we need the initial_indice histogram to have the same length. Not visible enough though
        #figure_subplots[i].hist(initial_indices[i], bins = [initial_indices[i], initial_indices[i] + bins[1] - bins[0]], color = 'r')
        figure_subplots[i].set_title(result_list[i], fontsize=8, wrap = True, ha = 'center')
        figure_subplots[i].set_xlabel(names_of_indices[i])
        figure_subplots[i].set_ylabel('Probability')
        # important addition for good visualization
        figure_subplots[i].set_xlim(min(np.min(list_of_indices[i]), initial_indices[i]) - 0.05, 
                                    max(np.max(list_of_indices[i]), initial_indices[i]) + 0.05) 
        # Fit the normal distribution to the data
        #bincenters = 0.5*(bins[1:]+bins[:-1])
        #y = norm.pdf(bincenters, np.mean(list_of_indices[i, :]), np.std(list_of_indices[i, :]))
        #figure_subplots[i].plot(bincenters, y, 'r--', linewidth=1)
    
    #ax1.set_title('External indices')
    plt.tight_layout()
    

def plot_relative_criteria_fuzzy(no_of_clusters_list, values_of_q, PC, PE, XB, FS):
    
    # row and column sharing
    figure, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize = (12,9))
    
    subplots_list = (ax1, ax2, ax3, ax4)
    
    
    
    # Plot PC
    for j, q_value in enumerate(values_of_q):
        ax1.plot(no_of_clusters_list, PC[:, j], label =  q_value)
        
    # Plot PE
    for j, q_value in enumerate(values_of_q):
        ax2.plot(no_of_clusters_list, PE[:, j], label = q_value)
        
    # Plot XB
    for j, q_value in enumerate(values_of_q):
        ax3.plot(no_of_clusters_list, XB[:, j], label = q_value)
        
    # Plot FS
    for j, q_value in enumerate(values_of_q):
        ax4.plot(no_of_clusters_list, FS[:, j], label = q_value)
        
    #plt.tight_layout()
    
    ax1.set_title('Partition Coefficient')
    ax2.set_title('Partition Entropy Coefficient')
    ax3.set_title('Xien Ben index')
    ax4.set_title('Fukuyama Sugeno index')
    figure.canvas.set_window_title('Relative Indices')
    
    for subplot in subplots_list:
        subplot.set_xlabel('Number of clusters')
        subplot.set_ylabel('Index value')
        subplot.legend(title = 'q values',framealpha= 0.7)

def plot_relative_criteria_hard(no_of_clusters_list, DI):
    # row and column sharing
    figure, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize = (12,9))
    
    subplots_list = (ax1, ax2, ax3, ax4)
    
    # Plot DI
    ax1.plot(no_of_clusters_list, DI)
    '''  
    # Plot PE
    for j, q_value in enumerate(values_of_q):
        ax2.plot(no_of_clusters_list, PE[:, j], label = q_value)
        
    # Plot XB
    for j, q_value in enumerate(values_of_q):
        ax3.plot(no_of_clusters_list, XB[:, j], label = q_value)
        
    # Plot FS
    for j, q_value in enumerate(values_of_q):
        ax4.plot(no_of_clusters_list, FS[:, j], label = q_value)
    '''
    #plt.tight_layout()
    
    ax1.set_title('Dunn Index')
    ax2.set_title('Partition Entropy Coefficient')
    ax3.set_title('Xien Ben index')
    ax4.set_title('Fukuyama Sugeno index')
    figure.canvas.set_window_title('Relative Indices')
    
    for subplot in subplots_list:
        subplot.set_xlabel('Number of clusters')
        subplot.set_ylabel('Index value')
        
 