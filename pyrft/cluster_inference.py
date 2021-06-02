import numpy as np
import pyrft as pr
import math
from skimage import measure

def find_clusters(test_statistic, CDT, below = bool(0), mask = math.nan, connectivity = 1, two_sample = bool(0)):
  """ find_clusters
  Parameters  
  ---------------------
  test_statistic:   a numpy.nd array,
          

  Returns
  ---------------------
  cluster_image:    a numpy.nd array,
              with the same size as the test-statistic in which the clusters 
              above the CDT are labelled each with a different number. 
  
  Examples
  ---------------------
# Clusters above 0.5
cluster_image, cluster_sizes = pr.find_clusters(np.array([[1,0,1],[1,1,0]]), 0.5)
# Clusters below 0.5
cluster_image, cluster_sizes = pr.find_clusters(np.array([[1,0,1],[1,1,0]]), 0.5, below = 1)
  """
  
  # Mask the data if that is possible
  if np.sum(np.ravel(mask)) > 0:
      test_statistic = test_statistic*mask
      
  if two_sample:
      raise Exception("two sample hasn't been implemented yet!")
      
  if below:
     cluster_image = measure.label((test_statistic < CDT)*(test_statistic > 0), connectivity = connectivity)
  else:
     cluster_image = measure.label(test_statistic > CDT, connectivity = connectivity)
  
  n_clusters = np.max(cluster_image)
  cluster_sizes = np.zeros(n_clusters)
  
  for I in np.arange(n_clusters):
      cluster_sizes[I] = np.sum(cluster_image == (I+1))
      
  return cluster_image, cluster_sizes
  