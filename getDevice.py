import tensorflow as tf

gpus = tf.config.list_physical_devices('GPU')
if gpus:
  for gpu in gpus:
    print("GPU Name:", gpu.name)
else:
  print("No available GPUs found")