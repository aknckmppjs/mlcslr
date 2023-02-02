import numpy as np
# from simple_linear_regr_utils import generate_data, evaluate


class SimpleLinearRegression:
    def __init__(self, iterations=15000, lr=0.1):
        self.iterations = iterations # number of iterations the fit method will be called
        self.lr = lr # The learning rate
        self.losses = [] # A list to hold the history of the calculated losses
        self.W, self.b = None, None # the slope and the intercept of the model

    def __loss(self, y, y_hat):
        """

        :param y: the actual output on the training set
        :param y_hat: the predicted output on the training set
        :return:
            loss: the sum of squared error

        """
        #ToDO calculate the loss. use the sum of squared error formula for simplicity
        loss = None
        loss = 0
        for k in range (y.shape[0]):
          loss += ((y[k]-y_hat[k])**2)
        loss = loss/(y.shape[0])
        self.losses.append(loss)
        return loss

    def __init_weights(self, X):
        """

        :param X: The training set
        """
        weights = np.random.normal(size=X.shape[1] + 1)
        self.W = weights[:X.shape[1]].reshape(-1, X.shape[1])
        self.b = weights[-1]

    def __sgd(self, X, y, y_hat):
        """

        :param X: The training set
        :param y: The actual output on the training set
        :param y_hat: The predicted output on the training set
        :return:
            sets updated W and b to the instance Object (self)
        """
        # ToDo calculate dW & db.
        n = X.shape[0]
        sumW = 0.0
        sumb = 0.0
        for k in range(n):
          sumW += X[k]*(y_hat[k]-y[k])
        dW = (sumW*2)/n
        # print("dW ", dW)
        # db = None
        for k in range(n):
          sumb += (y_hat[k]-y[k])
        db = (sumb*2)/n
        #  ToDO update the self.W and self.b using the learning rate and the values for dW and db
        self.W = self.W-self.lr*dW
        self.b = self.b-self.lr*db


    def fit(self, X, y):
        """

        :param X: The training set
        :param y: The true output of the training set
        :return:
        """
        self.__init_weights(X)
        y_hat = self.predict(X)
        loss = self.__loss(y, y_hat)
        print(f"Initial Loss: {loss}")
        for i in range(self.iterations + 1):
            self.__sgd(X, y, y_hat)
            y_hat = self.predict(X)
            loss = self.__loss(y, y_hat)
            if not i % 1000:
                print(f"Iteration {i}, Loss: {loss}")

    def predict(self, X):
        """

        :param X: The training dataset
        :return:
            y_hat: the predicted output
        """
        #ToDO calculate the predicted output y_hat. remember the function of a line is defined as y = WX + b
        # import numpy as np
        y_ht = []
        for k in range(X.shape[0]):
          y_ht.append(self.W*X[k] + self.b)
        y_hat = np.array(y_ht).reshape((-1,1))
        return y_hat


# if __name__ == "__main__":
#     X_train, y_train, X_test, y_test = generate_data()
#     model = SimpleLinearRegression()
#     model.fit(X_train,y_train)
#     predicted = model.predict(X_test)
#     evaluate(model, X_test, y_test, predicted)