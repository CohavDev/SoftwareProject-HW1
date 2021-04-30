class Vector:
    def __init__(self):
        self.coordinates = (0, 0)  # the vector itself
        self.clust = Cluster()  # the cluster who's the vector belong to

    def getCluster(self):
        return self.clust

    def getcoordinates(self):
        return self.coordinates


class Cluster:
    def __init__(self, d):
        self.sum = [0] * d  # total sum of all vectors in cluster, init to 0
        self.count = 0  # number of vectors in cluster
        self.mean = [0] * d
        self.d = d

    def addVector(self, vector):
        for i in range(0, self.d):
            self.sum[i] += vector.getCoordinates[i]
        self.count += 1

    def deleteVector(self, vector):
        for i in range(0, self.d):
            self.sum[i] -= vector.getCoordinates[i]
        self.count -= 1

    def getMean(self):
        return self.mean

    def calcMean(self):
        for i in range(0, self.d):
            self.mean[i] = self.sum[i] / self.count


# main
vectorsArr = []
clustersArr = []


# calculate distance^2 between 2 vectors coordinates
def distance(x, y):
    if len(x) != len(y):
        return None
    sum = 0
    for i in range(0, len(x)):
        sum += (x[i]-y[i])**2
    return sum


# calc means of each cluster in the array of clusters
def reCalcMeans():
    for clust in clustersArr:
        clust.calcMean()


# insert vector to its closest cluster and removes it from the previous
def findCluster(vector):
    mean = clustersArr[0].getMean()
    minDistance = distance(vector, mean)
    tempDistance = 0
    minCluster = clustersArr[0]  #default
    for clust in clustersArr:
        mean = clust.getMean()
        tempDistance = distance(vector.getCoordinates(), mean)
        if tempDistance < minDistance:
            minDistance = tempDistance
            minCluster = clust

    vector.getCluster().deleteVector(vector)
    minCluster.addVector(vector)
