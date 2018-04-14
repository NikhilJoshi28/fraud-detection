import numpy as np
import math

class parser:
    def do_parsing(self,delimiter):
        filepath = "german.data-numeric"
        data = []
        with open(filepath) as file:
            for row in file:
                list = row.split(' ')
                val =''
                while val in list:
                    list.remove(val)

                list.remove('\n')
                data.append(list)
        return data

    def normalize(self):
        data = self.do_parsing(" ")
        mean_vector = np.linalg.norm(data,axis=0)
        for i in range(len(data)):
            for j in range(len(data[i])):
                data[i][j] = int(data[i][j])/int(mean_vector[j]);
        np_array = np.array(data)
        return np_array

if __name__ == '__main__':
    par = parser()
    par.normalize()