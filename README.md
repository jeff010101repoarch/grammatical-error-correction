# Grammatic Error Corrector

## Instruction to Run 

file structure:

    .
    ├── correct_text.py   
    ├── data_reader.py
    ├── dataset_sep.py        
    ├── preprocessor.py   
    ├── seq2seq.py
    ├── text_corrector_data_readers.py
    ├── text_corrector_models.py             
    └── data
        └── cornell-movie-dialogs-corpus
            └── movie_lines.txt                            


Environment Requirement:  
* GPU: TITAN V (fast for speed) 
* Ubuntu 16.04.6 LTS, Python 3.5.2 (must be this version)
* Library: tensorflow 0.12.0 (must be this version), nltk, pandas, scikit-learn, collections

Train:
```python
python correct_text.py  --train_path PATH OF TRAINING DATA
                        --val_path PATH OF VALIDATING DATA
                        --config DefaultMovieDialogConfig 
                        --data_reader_type MovieDialogReader
                        --model_path PATH OF SAVED MODEL
```
Test:
```ptthon
python correct_text.py --test_path PATH OF TESTING DATA
                       --config DefaultMovieDialogConfig 
                       --data_reader_type MovieDialogReader 
                       --model_path /movie_dialog_model
                       --decode
```
Instead, there is script for training:
```python
python train.py
```
The trained model is saved in 
```python
data\dialog_correcter_model_testnltk
```

Load model:
```python
model = create_model(sess, True, model_path, config=config)
```