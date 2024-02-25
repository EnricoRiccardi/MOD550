from mse_vanilla import mean_squared_error as vanilla_mse
from mse_numpy import mean_squared_error as numpy_mse
import sklearn.metrics as sk

observed = [2, 4, 6, 8]
predicted = [2.5, 3.5, 5.5, 7.5]


mse_vanilla = vanilla_mse(observed, predicted)
print("Mean Squared Error, vanilla :", mse_vanilla) 

mse_numpy = numpy_mse(observed, predicted)
print("Mean Squared Error, numpy :  ", mse_numpy) 

sk_mse = sk.mean_squared_error(observed, predicted)
print("Mean Squared Error, sklearn :", sk_mse) 

assert(mse_vanilla == mse_numpy == sk_mse)

