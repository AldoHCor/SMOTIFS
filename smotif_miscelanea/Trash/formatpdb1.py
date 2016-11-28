import sys, os, pickle, numpy


list_ = [[['ATOM', 1, 'N', 'A', 89, -7.322, -8.434, 1.263]], [['ATOM', 2, 'H', 'A', 89, -6.748, -8.382, 2.08]], [['ATOM', 3, 'CA', 'A', 89, -6.754, -8.069, -0.027]], [['ATOM', 4, 'C', 'A', 89, -6.676, -9.265, -0.982]], [['ATOM', 5, 'O', 'A', 89, -6.924, -9.12, -2.185]], [['ATOM', 6, 'N', 'A', 90, -6.331, -10.442, -0.466]], [['ATOM', 7, 'H', 'A', 90, -6.171, -10.529, 0.517]], [['ATOM', 8, 'CA', 'A', 90, -6.186, -11.611, -1.337]], [['ATOM', 9, 'C', 'A', 90, -7.484, -11.922, -2.067]], [['ATOM', 10, 'O', 'A', 90, -7.504, -12.119, -3.291]], [['ATOM', 11, 'N', 'A', 91, -8.57, -11.967, -1.304]], [['ATOM', 12, 'H', 'A', 91, -8.473, -11.805, -0.322]], [['ATOM', 13, 'CA', 'A', 91, -9.896, -12.242, -1.837]], [['ATOM', 14, 'C', 'A', 91, -10.355, -11.124, -2.782]], [['ATOM', 15, 'O', 'A', 91, -10.932, -11.366, -3.853]], [['ATOM', 16, 'N', 'A', 92, -10.104, -9.888, -2.364]], [['ATOM', 17, 'H', 'A', 92, -9.596, -9.763, -1.512]], [['ATOM', 18, 'CA', 'A', 92, -10.542, -8.701, -3.101]], [['ATOM', 19, 'C', 'A', 92, -9.959, -8.708, -4.506]], [['ATOM', 20, 'O', 'A', 92, -10.685, -8.542, -5.489]], [['ATOM', 21, 'N', 'A', 93, -8.651, -8.917, -4.611]], [['ATOM', 22, 'H', 'A', 93, -8.109, -9.137, -3.8]], [['ATOM', 23, 'CA', 'A', 93, -8.013, -8.822, -5.921]], [['ATOM', 24, 'C', 'A', 93, -7.827, -10.159, -6.642]], [['ATOM', 25, 'O', 'A', 93, -7.458, -10.184, -7.816]], [['ATOM', 38, 'N', 'A', 105, 6.255, 4.191, 5.071]], [['ATOM', 39, 'H', 'A', 105, 6.322, 3.232, 5.345]], [['ATOM', 40, 'CA', 'A', 105, 7.353, 5.106, 5.373]], [['ATOM', 41, 'C', 'A', 105, 7.885, 5.844, 4.152]], [['ATOM', 42, 'O', 'A', 105, 8.231, 7.03, 4.212]], [['ATOM', 43, 'N', 'A', 106, 7.927, 5.157, 3.018]], [['ATOM', 44, 'H', 'A', 106, 7.585, 4.218, 2.989]], [['ATOM', 45, 'CA', 'A', 106, 8.472, 5.772, 1.814]], [['ATOM', 46, 'C', 'A', 106, 7.559, 6.828, 1.206]], [['ATOM', 47, 'O', 'A', 106, 8.017, 7.889, 0.788]], [['ATOM', 48, 'N', 'A', 107, 6.27, 6.525, 1.139]], [['ATOM', 49, 'H', 'A', 107, 5.95, 5.656, 1.517]], [['ATOM', 50, 'CA', 'A', 107, 5.314, 7.43, 0.528]], [['ATOM', 51, 'C', 'A', 107, 5.122, 8.675, 1.389]], [['ATOM', 52, 'O', 'A', 107, 4.824, 9.755, 0.874]], [['ATOM', 53, 'N', 'A', 108, 5.31, 8.526, 2.699]], [['ATOM', 54, 'H', 'A', 108, 5.48, 7.612, 3.068]], [['ATOM', 55, 'CA', 'A', 108, 5.274, 9.67, 3.611]], [['ATOM', 56, 'C', 'A', 108, 6.388, 10.656, 3.257]], [['ATOM', 57, 'O', 'A', 108, 6.185, 11.87, 3.276]], [['ATOM', 58, 'N', 'A', 109, 7.562, 10.132, 2.922]], [['ATOM', 59, 'H', 'A', 109, 7.683, 9.14, 2.961]], [['ATOM', 60, 'CA', 'A', 109, 8.679, 10.971, 2.498]], [['ATOM', 61, 'C', 'A', 109, 8.416, 11.536, 1.106]], [['ATOM', 62, 'O', 'A', 109, 8.732, 12.692, 0.824]], [['ATOM', 63, 'N', 'A', 110, 7.836, 10.71, 0.24]], [['ATOM', 64, 'H', 'A', 110, 7.608, 9.782, 0.534]], [['ATOM', 65, 'CA', 'A', 110, 7.522, 11.116, -1.128]], [['ATOM', 66, 'C', 'A', 110, 6.242, 11.943, -1.179]], [['ATOM', 67, 'O', 'A', 110, 5.247, 11.527, -1.776]]]

first_line = list_[0]
print first_line[0]


test =  "%-6s%5d  %-2s%5s%2s%4d%1s   %8.3f%8.3f%8.3f%6.2f%6.2f          %2s%2s"\%('ATOM', atom number,'A', aa_number,' ', x, y, z,1.0,30.0, '')
print test


pdb_line = "%-6s%5d  %-2s%5s%2s%4d%1s   %8.3f%8.3f%8.3f%6.2f%6.2f          %2s%2s"\
                   %('ATOM',i+1,atom,res,'A',res_num," ",x, y, z,1.0,30.0,' ',' \n')
                outfile.write(pdb_line)
