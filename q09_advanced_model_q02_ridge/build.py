from greyatomlib.multivariate_regression_project.q01_load_data.build import load_data

from greyatomlib.multivariate_regression_project.q02_data_split.build import split_dataset

from greyatomlib.multivariate_regression_project.q03_data_encoding.build import label_encode

from greyatomlib.multivariate_regression_project.q07_regression_pred.build import regression_predictor
from sklearn.linear_model import Ridge
import numpy as np
import pandas as pd

from greyatomlib.multivariate_regression_project.q06_cross_validation.build import cross_validation_regressor
np.random.seed(9)

df = load_data('data/student-mat.csv')
 
x_train, x_test, y_train, y_test =  split_dataset(df)

x_train,x_test = label_encode(x_train,x_test)

def ridge(x_train, x_test, y_train, y_test,alpha=0.1):
    ridge = Ridge(alpha=alpha, normalize=True, random_state=9)
    ridge.fit(x_train, y_train)
    c_val = cross_validation_regressor(ridge , x_train, y_train)
    y_pred, mse, mae, r2 = regression_predictor(ridge, x_test, y_test)
    stats = pd.DataFrame({'c_val':c_val,'rmse':np.sqrt(mse),'mae':mae,'r2':r2}, index=[0])
    return ridge,y_pred,stats
