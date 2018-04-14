import pickle
from data_preprocessing import parser

class clustering:
    def point_classification(self,min_points,epsilon):
        dis_mat = pickle.load(open("distance_matrix.pkl","rb"))
        #print(min(dis_mat))
        N = len(dis_mat)
        point_classification = {}
        point_classification["CP"] = []
        point_classification["BP"] = []
        point_classification["NP"] = []
        for i in range(N):
            point_count=0
            for j in range(0,N):
                if i==j:
                    pass
                if dis_mat[i][j]<epsilon:
                    point_count+=1

            if point_count>=min_points:
                point_classification["CP"].append(i)

        for i in range(N):
            if i not in point_classification["CP"]:
                for j in range(N):
                    if i!=j and j in point_classification["CP"] and dis_mat[i][j]>epsilon:
                        point_classification["BP"].append(i)
                        break

        for i in range(N):
            if i not in point_classification["CP"] and i not in point_classification["BP"]:
                point_classification["NP"].append(i)

        return point_classification,N

    def dbscan(self,min_points,epsilon):
        classification,N = self.point_classification((min_points),epsilon)
        cluster = [[],[]]
        for i in range(N):
            if i in classification["CP"]:
                cluster[0].append(i)
            elif i in classification["BP"]:
                cluster[0].append(i)
            else:
                cluster[1].append(i)

        sum=0;
        pa = parser()
        data = pa.do_parsing(" ")

        for i in range(N):
            if (i in cluster[0] and int(data[i][24])==1):
                sum+=1
            elif (i in cluster[1] and int(data[i][24])==2):
                sum+=1

        print("Accuracy = "+str(sum/10))


if __name__ == '__main__':
    cls = clustering()
    cls.dbscan(3,0.1081072053651570)