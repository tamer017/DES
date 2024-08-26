# Sentiment Analysis with BERT on the SST Dataset


This part focuses on sentiment analysis using the BERT model on the Stanford Sentiment Treebank (SST) dataset. Sentiment analysis is a fundamental task in Natural Language Processing (NLP) that involves determining the sentiment expressed in a text. The SST dataset is a widely-used benchmark that provides labeled sentences with sentiment scores across different classes.

Our primary objective is to enhance the performance of BERT-based sentiment classification beyond the current baseline by exploring various techniques and modifications.

The goal of this section is to improve the baseline accuracy of 52.2% achieved by a BERT model on the SST dataset. To achieve this, we explored various techniques such as advanced regularization methods, different loss functions, and architectural modifications. Our aim is to develop a more robust and accurate sentiment classification model that better understands and predicts sentiments expressed in text.

### Key Takeaways

- **BERT Fine-Tuned**: Demonstrated high accuracy on the IMDB dataset but maintained baseline accuracy on SST and the Tweets dataset.
- **Multi-Task Fine-Tuning (SMART + Mnrl)**: Improved performance on the STS dataset but did not enhance SST accuracy.
- **Residual MLP (RIMLP)**: Performance was on par with the baseline.
- **L2 Regularization**: Provided the best improvement in SST accuracy.
- **Autoencoder Backbone**: Resulted in a significant drop in performance.
- **Focal Loss**: Provided a slight improvement in SST accuracy.

## Experiments

### **Comparison of Best Models Across Experiments on development sets**
We conducted several experiments to test different approaches and modifications. Below is a summary of these experiments:

| **Experiment**                  | **Best Model/Technique**           | **Dataset/Task**   | **Evaluation Metric** | **Result** |
|---------------------------------|------------------------------------|--------------------|-----------------------|------------|
| **Experiment 1**                | BERT Fine-Tuned                    | IMDB/SST           | Accuracy               | 93.8%/52.6%      |
| **Experiment 1**                | BERT Fine-Tuned                    | Tweets/SST         | Accuracy               | 61.6%/52.6%      |
| **Experiment 2**                | Multi-Task Fine-Tuning (SMART + Mnrl) | SST           | Accuracy               | 51%        |
| **Experiment 2**                | Multi-Task Fine-Tuning (SMART + Mnrl) | STS           | Pearson’s Correlation | 0.812      |
| **Experiment 3**                | Residual MLP (RIMLP)               | SST                | Accuracy               | 52.2%      |
| **Experiment 4**                | L2 Regularization (Lambda: 0.05)   | SST                | Accuracy               | 52.9%      |
| **Experiment 5**                | Autoencoder Backbone               | SST                | Accuracy               | 18.3%      |
| **Experiment 6**                | Focal Loss                         | SST                | Accuracy               | 53%        |


1. **Experiment 1: Fine-Tuning BERT with New Datasets**
   - **Description**: This experiment involved fine-tuning the BERT model using three datasets:
     - **IMDB Dataset**: A dataset of 50,000 movie reviews for binary sentiment classification.
       - **Description**: The IMDB dataset consists of 25,000 positive and 25,000 negative movie reviews. Due to limited resources, only 17,500 samples were used for training.
       - **Link**: [IMDB Dataset of 50K Movie Reviews](http://ai.stanford.edu/~amaas/data/sentiment/)
       - **Branch**: [sentiment-imdb-binary](https://github.com/thisHermit/nlp_project/tree/sentiment-imdb-binary)
     - **Tweets Dataset**: A dataset for multi-class sentiment classification with 5 sentiment classes.
       - **Description**: The dataset contains tweets labeled with five sentiment categories: anger, fear, happy, love, and sadness. For training, 3,521 samples were used.
       - **Link**: [Tweets Dataset](https://raw.githubusercontent.com/IndoNLP/indonlu/master/dataset/emot_emotion-twitter)
       - **Branch**: [sentiment-tweets](https://github.com/thisHermit/nlp_project/tree/sentiment-tweets)
     - **SST Dataset**: Used together with the IMDB and Tweets datasets for training.
       - **Description**: The Stanford Sentiment Treebank (SST) dataset was used to evaluate the model’s performance.
   - **Training Procedure**:
     - **Model**: BERT model was fine-tuned using IMDB, Tweets, and SST datasets together.
     - **Loss Function**: Used CrossEntropyLoss for updating the weights of the BERT model.
     - **Evaluation**: Performance was measured on the SST development set.
     - **Data Handling**:
       - **Data Loaders**: New data loaders were implemented to handle the separate datasets for Tweets and IMDB.
       - **Validation Functions**: Separate validation functions were added to evaluate performance for each task independently.
   - **Objective**: To evaluate the performance of the BERT model when trained with multiple datasets and assessed on the SST development set.
   - **Results**:
     - **IMDB Dataset**: Achieved 93.8% accuracy on the IMDB development set.
     - **Tweets Dataset**: Achieved 61.6% accuracy on the Tweets development set.
     - **SST Dataset**: Achieved 52.6% accuracy on the SST development set.
     
| **Dataset**      | **Training Samples** | **Evaluation Metric** | **Result** |
|------------------|----------------------|-----------------------|------------|
| IMDB/SST            | 17,500               | Accuracy               | 93.8%/52.6%      |
| Tweets/SST          | 3,521                | Accuracy               | 61.6%/52.6%      |

#### How to run
```bash
   # load IMDB Dataset
   python load_binary_data.py

   # load IMDB Dataset
   python load_tweets_data.py
   ```
   edit **run_train.py** 
```bash
   python -u multitask_classifier.py --use_gpu --epochs 15 --local_files_only --option finetune --task multi-sentiment --hidden_dropout_prob 0.1 --lr 1e-5 --batch_size 64
   ```
   run **run_train.py**
   ```bash
      ./run_train.py
   ```



2. **Experiment 2: Multi-Task Fine-Tuning with Sentiment Analysis and Semantic Similarity**
   - **Description**: This experiment involved fine-tuning the BERT model to perform two distinct tasks simultaneously:
     - **Sentiment Analysis Task**: Utilized the SST dataset for sentiment classification.
       - **Description**: The sentiment analysis task involved classifying sentences into different sentiment categories using a dropout layer and a classification layer.
     - **Semantic Textual Similarity (STS) Task**: Used the STS dataset to evaluate the semantic similarity between sentence pairs.
       - **Technique**: Employed SMART + Mnrl:
         - **SMART**: Provides regularization benefits to improve model robustness.
         - **Mnrl**: Enhances ranking optimization to boost accuracy in semantic similarity measurements.
       - **Explanation**: SMART's regularization and Mnrl's ranking optimization are combined to enhance both the robustness and ranking accuracy for the STS task.
   - **Training Procedure**:
     - **Model**: BERT model was fine-tuned for both sentiment analysis and semantic similarity tasks.
     - **Loss Functions**: Utilized appropriate loss functions for each task to ensure proper training and evaluation.
   - **Results**:
     - **SST Dataset**: Achieved 51% accuracy on the SST development set.
     - **STS Dataset**: Achieved a Pearson’s correlation of 0.812 on the STS development set.
   - **Branch**: [sentiment-semantic](https://github.com/thisHermit/nlp_project/tree/sentiment-semantic)

| **Task**                  | **Dataset**      | **Evaluation Metric** | **Result** |
|---------------------------|------------------|-----------------------|------------|
| Sentiment Analysis        | SST              | Accuracy               | 51%        |
| Semantic Textual Similarity (STS) | STS              | Pearson’s Correlation | 0.812      |

#### How to run
change the following constants in **multitask_calssifier.py**
```bash
   AUTOENCODER = True # to use the AOE
   AOE = False # to train the AOE
   ```

   edit **run_train.py** 
```bash
   # at auto-encoder training
   python -u multitask_classifier.py --use_gpu --epochs 10 --local_files_only --option pretrain --task sst --hidden_dropout_prob 0.1 --lr 1e-5 --batch_size 64
   # at classification
   python -u multitask_classifier.py --use_gpu --epochs 10 --local_files_only --option finetune --task sst --hidden_dropout_prob 0.1 --lr 1e-5 --batch_size 64
   ```
   run **run_train.py**
   ```bash
      ./run_train.py
   ```

3. **Experiment 3: Changing the Classification Head**
   - **Description**: This experiment explored a more complex classification head by integrating residual connections and a multi-layer perceptron with a bidirectional LSTM (bLSTM):
     - **Architecture**:
       - **Bidirectional LSTM (bLSTM)**: Added to model the sequence of sentences or words, capturing the overall sentiment flow.
       - **Residual MLP (RIMLP)**: Incorporated with residual connections to add depth and non-linearity, aiming to enhance the model's ability to learn complex patterns.
       - **Residual Connections**: Used within the MLP to improve gradient flow and training stability.
   - **Objective**: To determine if combining bLSTM with a Residual MLP architecture improves performance over a simpler classifier layer.
   - **Results**:
     - **Residual MLP**: Achieved 52% accuracy on the SST development set.
     - **Bidirectional LSTM (bLSTM)**: Achieved 51.9% accuracy on the SST development set.
     - **Simple Classification Layer (Baseline)**: Achieved 52.2% accuracy on the SST development set.
   - **Analysis**: The accuracy did not improve significantly due to the overhead of training additional layers with the small dataset. The complexity introduced by the new layers may have led to overfitting or inefficiencies in learning from the limited data.
   - **Branch**: [sentiment-architectures](https://github.com/thisHermit/nlp_project/tree/sentiment-architectures)

| **Architecture**           | **Evaluation Metric** | **Result** |
|----------------------------|-----------------------|------------|
| Residual MLP (RIMLP)        | Accuracy               | 52%      |
| Bidirectional LSTM (bLSTM)  | Accuracy               | 51.9%      |
| Simple Classification Layer (Baseline) | Accuracy   | 52.2%      |

4. **Experiment 4: Addressing Overfitting with Regularization Techniques**
   - **Description**: This experiment aimed to tackle the overfitting issue by applying various regularization techniques to the model. The following techniques were tested:
     - **Dropout**: Applied with a dropout rate of 0.4.
       - **Justification**: Dropout helps prevent overfitting by randomly dropping units during training, which encourages the model to learn more robust features.
       - **Result**: Achieved 52.7% accuracy.
     - **L2 Regularization (Weight Decay)**: Applied with a lambda of 0.05.
       - **Justification**: L2 regularization penalizes large weights, helping to reduce model complexity and overfitting.
       - **Result**: Achieved 52.9% accuracy.
     - **Batch Normalization**: Incorporated into the model.
       - **Justification**: Batch normalization helps stabilize and accelerate training by normalizing the inputs of each layer, but did not show significant improvement.
       - **Result**: Achieved 52% accuracy.
     - **L1 Regularization**: Applied with a lambda of 1e-5.
       - **Justification**: L1 regularization encourages sparsity in the model weights, which can be useful for feature selection, though its impact was limited in this case.
       - **Result**: Achieved 52.1% accuracy.
     - **Gradient Clipping**: Applied with a clipping value of 1.
       - **Justification**: Gradient clipping prevents exploding gradients by setting a maximum threshold, helping to stabilize training, but did not significantly improve accuracy.
       - **Result**: Achieved 52.1% accuracy.
     - **Label Smoothing**: Applied with a smoothing factor of 0.1.
       - **Justification**: Label smoothing helps to reduce the model’s confidence on training examples, which can improve generalization.
       - **Result**: Achieved 52.3% accuracy.
   - **Best Results**:
     - **Dropout and L2 Regularization**: Both achieved the highest accuracy of 52.7%. These methods showed the best performance in reducing overfitting and improving the model’s robustness.
   - **Branch**: [sentiment-regularization](https://github.com/thisHermit/nlp_project/tree/sentiment-regularization)

| **Regularization Technique** | **Evaluation Metric** | **Result** |
|------------------------------|-----------------------|------------|
| Dropout (Rate: 0.4)           | Accuracy               | 52.7%      |
| L2 Regularization (Lambda: 0.05) | Accuracy           | 52.9%      |
| Batch Normalization          | Accuracy               | 52%        |
| L1 Regularization (Lambda: 1e-5) | Accuracy           | 52.1%      |
| Gradient Clipping (Value: 1) | Accuracy               | 52.1%      |
| Label Smoothing (Factor: 0.1) | Accuracy              | 52.3%      |


5. **Experiment 5: Using Autoencoder as a Backbone After BERT**
   - **Description**: In this experiment, I utilized an autoencoder as a backbone after the BERT model to reconstruct the embeddings produced by BERT. The goal was to improve the quality of embeddings and subsequently enhance sentiment classification performance.
   - **Autoencoder Architecture**:
     - **Encoder**:
       - The encoder consists of multiple linear layers with decreasing dimensions: `[512, 256, 128, 64]`.
       - Each layer is followed by LayerNorm, LeakyReLU activation, and Dropout for regularization.
     - **Decoder**:
       - The decoder mirrors the encoder with linear layers in reverse order, reconstructing the input embedding.
       - The final layer applies a Sigmoid activation function to produce the reconstructed embeddings.
     - **Skip Connections**:
       - Added skip connections to the decoder, allowing the model to better capture the input information.
   - **Training**:
     - **Dataset**: Quora Paraphrase dataset was used for training the autoencoder since it is larger than the SST dataset.
     - **Objective**: The autoencoder was trained to reconstruct the embeddings generated by the BERT model using the first sentence in each example.
     - **Results**: Achieved a very low reconstruction loss of 0.00001, indicating that the autoencoder learned to effectively reconstruct the BERT embeddings.
   - **Using the Autoencoder as a Backbone**:
     - **Approach**: The encoder part of the autoencoder was used as a backbone after the BERT model. An additional classification layer was added at the end.
     - **Performance**: The model performed poorly on the SST development set, achieving only 18.3% accuracy.
     - **Analysis**: The poor performance was likely due to the suboptimal embeddings generated by the BERT model when used without fine-tuning for this specific task. However, after tuning BERT with other tasks, the encoder backbone is expected to perform better when frozen and used with tuned embeddings.
   - **Branch**: [sentiment-autoencoder](https://github.com/thisHermit/nlp_project/tree/sentiment-autoencoder)

| **Training Dataset** | **Evaluation Metric** | **Result** |
|----------------------|-----------------------|------------|
| Quora Paraphrase      | Reconstruction Loss   | 0.00001    |
| SST                   | Accuracy               | 18.3%      |

### Experiment 6: Exploring Multiple Loss Functions to Improve Model Performance

**Description**: In this experiment, I explored different loss functions to improve the accuracy of the BERT-based sentiment analysis model. The goal was to determine which loss function yields the best performance on the SST development set.

**Loss Functions Tested**:
1. **CrossEntropyLoss** (Baseline): 
   - **Explanation**: CrossEntropyLoss is the standard loss function used for classification tasks. It measures the difference between the predicted probability distribution and the true distribution, encouraging the model to increase the probability of the correct class.
   - **Result**: Achieved 52.2% accuracy on the SST development set.
   
2. **Mean Squared Error (MSE)**:
   - **Explanation**: MSE is typically used for regression tasks but can be applied to classification by treating class probabilities as continuous values. It penalizes the squared differences between predicted and true values, promoting small errors.
   - **Result**: Achieved 52.6% accuracy on the SST development set, slightly outperforming CrossEntropyLoss.

3. **Hinge Loss**:
   - **Explanation**: Hinge Loss is commonly used in support vector machines (SVMs). It penalizes misclassifications and encourages the model to push the decision boundary further from the training examples, improving margin.
   - **Result**: Achieved 52.4% accuracy on the SST development set.

4. **Dice Loss**:
   - **Explanation**: Dice Loss is often used in segmentation tasks and measures the overlap between the predicted and true labels. It is particularly useful for handling class imbalances by focusing on maximizing overlap.
   - **Result**: Achieved 46.6% accuracy on the SST development set, indicating that it might not be well-suited for this task.

5. **Focal Loss**:
   - **Explanation**: Focal Loss is designed to address class imbalance by down-weighting the loss for well-classified examples, allowing the model to focus more on hard-to-classify examples. This can lead to better performance on tasks where some classes are underrepresented.
   - **Result**: Achieved 53% accuracy on the SST development set, outperforming all other loss functions.
   - **Justification**: Focal Loss proved to be the most effective, likely due to its ability to focus on harder examples, making it more suitable for this task.

**Conclusion**: The use of Focal Loss resulted in the highest accuracy, making it the best choice among the tested loss functions. It effectively handles class imbalance and improves model robustness, leading to better generalization on the SST dataset.

**Branch**: [sentiment-loss-function](https://github.com/thisHermit/nlp_project/tree/sentiment-loss-function)

| **Loss Function**        | **Evaluation Metric** | **Result** |
|--------------------------|-----------------------|------------|
| CrossEntropyLoss (Baseline) | Accuracy          | 52.2%      |
| Mean Squared Error (MSE) | Accuracy               | 52.6%      |
| Hinge Loss               | Accuracy               | 52.4%      |
| Dice Loss                | Accuracy               | 46.6%      |
| Focal Loss               | Accuracy               | 53%        |

# HOW TO RUN The Best Model
   edit **run_train.py** 
```bash
   python -u multitask_classifier.py --use_gpu --epochs 10 --local_files_only --option finetune --task sst --hidden_dropout_prob 0.1 --lr 1e-5 --batch_size 64
   ```
   run **run_train.py**
   ```bash
      ./run_train.py


