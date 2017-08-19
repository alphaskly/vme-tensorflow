#coding: utf-8
import tensorflow as tf

class Tensor:

    '''
        TensorFlow Two stage:
            1、定义计算图中的计算
            2、执行计算
        每个TensorFlow程序都有一个默认的计算图
    '''

    def one(self):
        #定义计算
        a = tf.constant([1.0, 2.0], name="a")
        b = tf.constant([2.0, 3.0], name='b')
        result = a + b
        print(result)

    def two(self):
        print(tf.__version__)
        #生成计算图(不同计算图上的张量和运算不会共享)
        g1 = tf.Graph()
        with g1.as_default():
            #在计算图中添加变量,并初始化
            v = tf.get_variable("v", [1])

        g2 = tf.Graph()
        with g2.as_default():
            v = tf.get_variable("v", [1])

        #读取变量
        with tf.Session(graph=g1) as sess:
            tf.initialize_all_variables().run()
            with tf.variable_scope("", reuse=True):
                print(sess.run(tf.get_variable("v")))
        with tf.Session(graph=g2) as sess:
            tf.initialize_all_variables().run()
            with tf.variable_scope("", reuse=True):
                print(sess.run(tf.get_variable("v")))


tensor = Tensor()
tensor.one()
tensor.two()
print(Tensor.__doc__)