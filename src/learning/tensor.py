import tensorflow as tf


def one():
    a = tf.constant([1.0, 2.0], name="a")
    b = tf.constant([2.0, 3.0], name='b')
    result = a + b
    print(a.graph() is tf.get_default_graph())

def two():
    print(tf.__version__)
    g1 = tf.Graph()
    with g1.as_default():
        v = tf.get_variable("v", [1])

    g2 = tf.Graph()
    with g2.as_default():
        v = tf.get_variable("v", [1])

    with tf.Session(graph=g1) as sess:
        tf.initialize_all_variables().run()
        with tf.variable_scope("", reuse=True):
            print(sess.run(tf.get_variable("v")))
    with tf.Session(graph=g2) as sess:
        tf.initialize_all_variables().run()
        with tf.variable_scope("", reuse=True):
            print(sess.run(tf.get_variable("v")))


two()