use tensorflow::Tensor;


fn main() {
//Sigmatures declared when we saved the model
    let train_input_parameter_input_name = "training_input";
    let train_input_parameter_target_name = "training_target";
    let pred_input_parameter_name = "inputs";

    //Names of output nodes of the graph, retrieved with the saved_model_cli command
    let train_output_parameter_name = "output_0";
    let pred_output_parameter_name = "output_0";

    //Create some tensors to feed to the model for training, one as input and one as the target value
    //Note: All tensors must be declared before args!
    let input_tensor: Tensor<f32> = Tensor::new(&[1,2]).with_values(&[1.0, 1.0]).unwrap();
    let target_tensor: Tensor<f32> = Tensor::new(&[1,1]).with_values(&[2.0]).unwrap();
}
