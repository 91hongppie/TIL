import tensorflow as tf
import numpy as np

xData = [1, 2, 3, 4, 5, 6, 7]
yData = [25000, 55000, 75000, 110000, 128000, 155000, 180000]

# tensorflow version 1.x
# W = tf.Variable(tf.random.uniform([1], -100, 100))
# b = tf.Variable(tf.random.uniform([1], -100, 100))
# X = tf.placeholder(tf.float32)
# Y = tf.placeholder(tf.float32)
# H = W * X + b
# cost = tf.reduce_mean(tf.square(H - Y)) # reduce_mean = 평균값을 구하는 것
# a = tf.Variable(0.01) 
# optimizer = tf.train.GradientDescentOptimizer(a) # GradientDescentOPtimizer - tensorflow 에서 제공하는 경사 하강 라이브러리
# train = optimizer.minimize(cost)
# init = tf.global_variables_initializer()
# sess = tf.Session()
# sess.run(init)
# for i in range(5001):
#     sess.run(train, feed_dict={X: xData, Y: yData})
#     if i % 500 == 0:
#         print(i, sess.run(cost, feed_dict={X: xData, Y: yData}), sess.run(W), sess.run(b))
# print(sess.run(H, feed_dict={X: [8]}))


# tensorflow version 2
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(1, input_dim=1))

sgd = tf.keras.optimizers.SGD(lr=0.01)

model.compile(loss='mean_squared_error', optimizer=sgd)

model.fit(xData, yData, epochs=5000)
print(model.predict(np.array([8])))