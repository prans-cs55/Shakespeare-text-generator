# Shakespeare-text-generator

<img width="2796" height="1438" alt="Screenshot 2025-08-01 215747" src="https://github.com/user-attachments/assets/6944627c-231f-4a65-bbda-9588bbcfdf89" />

📝 Shakespeare Text Generator
A character-level LSTM-based text generation model trained on the works of William Shakespeare, built using TensorFlow and Keras.

📖 Overview
This project demonstrates how deep learning models—specifically LSTM (Long Short-Term Memory) networks—can learn to generate human-like text, character by character. The model is trained on Shakespeare’s complete works and can generate original text in a similar style.

🧠 Model Architecture
Input: Character-level sequences (length = 40)

Model: LSTM layer with 256 units

Output: Dense layer with softmax activation over the vocabulary

Loss: Categorical Crossentropy

Optimizer: RMSprop

🔗 Dataset
The model uses a publicly available dataset:

arduino
https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt
You can download it using:


filepath = tf.keras.utils.get_file(
    'shakespeare.txt',
    'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt'
)
🛠️ Installation
bash
Copy
Edit
git clone https://github.com/yourusername/shakespeare-text-generator.git
cd shakespeare-text-generator
pip install -r requirements.txt
🚀 How to Run
Train the model
Generate text
generate_text(model, char_to_index, index_to_char, seed="to be, or not to be", length=300)
🧪 Example Output
to be, or not to be: that is the que
stion whether 'tis nobler in the mind to suffe
r the slings and arrows of outrageous fortu
ne, or to take arms against a sea of tro
ubles and by opposing end them.
