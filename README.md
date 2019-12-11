# Grammatic Error Corrector

The simple project of grammatical error correction by adopting seq2seq model with LSTM.

## Instruction to Run 

1. Environment Requirement:  
* GPU: TITAN V (fast for speed) 
* Ubuntu 16.04.6 LTS, Python 3.5.2 (must be this version)
* Library: tensorflow 0.12.0 (must be this version), nltk, pandas, scikit-learn, collections

2. Train:
```python
python correct_text.py  -- train_path PATH OF TRAINING DATA
                        -- val_path PATH OF VALIDATING DATA
                        -- config DefaultMovieDialogConfig 
                        -- data_reader_type MovieDialogReader
                        -- model_path PATH OF SAVED MODEL
```
3. Test:
```python
python correct_text.py -- test_path PATH OF TESTING DATA
                       -- config DefaultMovieDialogConfig 
                       -- data_reader_type MovieDialogReader 
                       -- model_path /movie_dialog_model
                       -- decode
```
Instead, there is script for training:
```python
python train.py
```
The trained model is saved in 
```python
data\dialog_correcter_model_testnltk
```

4. Load model:
```python
model = create_model(sess, True, model_path, config=config)
```
