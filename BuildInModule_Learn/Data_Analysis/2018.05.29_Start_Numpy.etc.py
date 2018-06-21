# Chapter2

# page34
# import numpy as np
#
# b = np.arange(24).reshape(2,12)
# print('b:',b)
# b1 = b.T
# print('b1:',b1)
# print(b.ndim)
# print(b1.ndim)


# # page43
# import scipy.misc
# import matplotlib.pyplot as plt
# import numpy as np
#
# # lena = scipy.misc.lena()
# xmax = lena.shape[0]
# ymax = lena.shape[1]
#
# def shuffle_indices(size):
#     arr = np.arange(size)
#     np.random.shuffle(arr)
#     return arr
#
# xindices = shuffle_indices(xmax)
# np.testing.assert_equal(len(xindices),xmax)
# yindices = shuffle_indices(ymax)
# np.testing.assert_equal(len(yindices),ymax)
# plt.imshow(lena[np.ix_(xindices,yindices)])
# plt.show()