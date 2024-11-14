import tensorflow as tf

# Load your Keras model
keras_model = tf.keras.models.load_model('my_model.keras')

# Convert the model to TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_keras_model(keras_model)
tflite_model = converter.convert()

# Save the TensorFlow Lite model
with open('my_model.tflite', 'wb') as f:
    f.write(tflite_model)

#Integrate the TensorFlow Lite model into your Android project:
#Add the TensorFlow Lite dependency to your Android project's build.gradle file:
 
dependencies {
    implementation 'org.tensorflow:tensorflow-lite:2.8.0' // Or latest version
}

#Add the my_model.tflite file to your Android project's assets folder.
#Load the TensorFlow Lite model in your Android code:
 
try (Interpreter tflite = new Interpreter(loadModelFile(this))) {
    // ... (Preprocess input data) ...
    tflite.run(input, output);
    // ... (Postprocess output data) ...
} catch (Exception e) {
    // ... (Handle exceptions) ...
}

private MappedByteBuffer loadModelFile(Activity activity) throws IOException {
    AssetFileDescriptor fileDescriptor = activity.getAssets().openFd("my_model.tflite");
    FileInputStream inputStream = new FileInputStream(fileDescriptor.getFileDescriptor());
    FileChannel fileChannel = inputStream.getChannel();
    long startOffset = fileDescriptor.getStartOffset();
    long declaredLength = fileDescriptor.getDeclaredLength();
    return fileChannel.map(FileChannel.MapMode.READ_ONLY, startOffset, declaredLength);
}
