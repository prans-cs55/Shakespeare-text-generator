filepath=tf.keras.utils.get_file('shake.txt','https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text=open(filepath,'rb').read().decode(encoding='utf-8')
text=text[300000:800000]
characters=sorted(set(text))
