class Vector:
    def __init__(self, arr):
        self.coordinates = arr  # the vector itself
        self.clust = None  # the cluster who's the vector belong to

    def getCluster(self):
        return self.clust

    def getCoordinates(self):
        return self.coordinates


class Cluster:
    def __init__(self, d):
        self.sum = [0] * d  # total sum of all vectors in cluster, init to 0
        self.count = 0  # number of vectors in cluster
        self.mean = [0] * d
        self.d = d

    def addVector(self, vector):
        for i in range(0, self.d):
            self.sum[i] += vector.getCoordinates()[i]
        self.count += 1
        vector.clust = self

    def deleteVector(self, vector):
        for i in range(0, self.d):
            self.sum[i] -= vector.getCoordinates()[i]
        self.count -= 1
        vector.clust = None

    def getMean(self):
        return self.mean

    def calcMean(self):
        changed = False  # indicates if mean have changed
        for i in range(0, self.d):
            if self.mean[i] != self.sum[i] / self.count:
                changed = True
            self.mean[i] = self.sum[i] / self.count
        return changed


# main
vectorsArr = []
clustersArr = []


# calculate distance^2 between 2 vectors coordinates
def distance(x, y):
    if len(x) != len(y):
        return None
    sum = 0
    for i in range(0, len(x)):
        sum += (x[i] - y[i]) ** 2
    return sum


# calc means of each cluster in the array of clusters.
# returns True if means have changed, False otherwise.
def reCalcMeans():
    changed = False
    for clust in clustersArr:
        if clust.calcMean():
            changed = True
    return changed


# insert vector to its closest cluster and removes it from the previous
def findCluster(vector):
    mean = clustersArr[0].getMean()
    minDistance = distance(vector, mean)
    tempDistance = 0
    minCluster = clustersArr[0]  # default
    for clust in clustersArr:
        mean = clust.getMean()
        tempDistance = distance(vector.getCoordinates(), mean)
        if tempDistance < minDistance:
            minDistance = tempDistance
            minCluster = clust

    vector.getCluster().deleteVector(vector)
    minCluster.addVector(vector)


# test
# c1 = [2, 2]
# c2 = [2, 8]
# print(36 == distance(c1, c2))
#
# vec1 = Vector(c1)
# vec2 = Vector(c2)
# clust = Cluster(2)
# clust.addVector(vec1)
# clust.addVector(vec2)
# clust.deleteVector(vec1)

def initFromFile(fileName, k, d):
    # TODO: read vectors from file and init arrays
    f = open(fileName, "rt")
    for line in f:
        vec = Vector(line.split(","))
        vectorsArr.append(vec)
    f.close()
    # set first k vectors as centroids
    for i in range(0, k):
        vec = vectorsArr[i]
        clust = Cluster(d)
        clust.addVector(vec)
        clustersArr.append(clust)


def printMeans(lst):
    for clust in lst:
        arr = clust.getMean()
        for x in arr:
            print(x + ",")
        print("\n")


# TODO: didnt check this function
def kMeans(k, maxIter, fileName):
    initFromFile(fileName)
    changed = True  # false if cluster's mean have converged
    iterCount = 0  # counts number of iterations
    while (iterCount < maxIter) and changed:
        iterCount += 1
        for vec in vectorsArr:
            findCluster(vec)
        # recalcs means of clusters, and determines if changed
        changed = reCalcMeans()
    printMeans(clustersArr)
