import numpy
import pickle
from data_preprocessing import parser
import math

class distance_calculation:
    def get_cos_Distance(self,pt1,pt2):
        sum1=0
        sum2=0
        sum3=0
        for i in range(len(pt1)):
            sum1+=pt1[i]*pt2[i]
            sum2+=pt1[i]*pt1[i]
            sum3+=pt2[i]*pt2[i]

        return (sum1/((math.sqrt(sum2))*(math.sqrt(sum3))))

    def get_euclidian_dis(self,pt1,pt2):
        sum=0
        for i in range(len(pt1)-1):
            sum+=(pt1[i]-pt2[i])*(pt1[i]-pt2[i])

        return math.sqrt(sum)

    def dis(self):
        par = parser()
        data = par.normalize()
        N = len(data)
        distance_matrix = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                print(i,j)
                if i<j:
                    distance_matrix[i][j]= self.get_euclidian_dis(data[i],data[j])
                elif i == j:
                    distance_matrix[i][j] = 0
                else:
                    distance_matrix[i][j]=distance_matrix[j][i]

        pickle.dump(distance_matrix, open("distance_matrix.pkl", "wb"), pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    dc = distance_calculation()
    dc.dis()