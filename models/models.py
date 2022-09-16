"""this module creates a model"""
import tensorflow as tf

class CustomModel(tf.keras.Model):
    """CustomModel is for creating models that can be exported"""
    def __init__(self, *args, **kwargs):
        super(CustomModel, self).__init__(*args, **kwargs)
        self.dense_1 = tf.keras.layers.Dense(2, name="test_in", input_dim=2)
        self.dense_2 = tf.keras.layers.Dense(1, name="test_out")

    #Call function used to make predictions from Rust
    #pylint: disable=arguments-differ
    @tf.function
    def call(self, inputs):
        """predict some stuff"""
        return self.dense_2(self.dense_1(inputs))

    #Train function called from Rust which uses the keras model innate train_step function
    @tf.function
    def training(self, train_data):
        """train the model"""
        return self.train_step(train_data)['loss']

#Create model
test_model = CustomModel()

#Compile model
test_model.compile(optimizer ='sgd', loss='mse', metrics = ['mae'])

#Get concrete function for the call method
pred_output = test_model.call.get_concrete_function(
    tf.TensorSpec(
        shape=[1, 2],
        dtype=tf.float32,
        name='inputs'))

#Get concrete function for the training method
train_output = test_model.training.get_concrete_function((
    tf.TensorSpec(
        shape=[1,2],
        dtype=tf.float32,
        name="training_input"
    ),
    tf.TensorSpec(
        shape=[1,1],
        dtype=tf.float32,
        name="training_target")))

#Saving the model, explictly adding the concrete functions as signatures
test_model.save(
    'custom_model',
    save_format='tf',
    signatures={'train': train_output, 'pred': pred_output})
