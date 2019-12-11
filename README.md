# Grammatic Error Corrector

The simple project of grammatical error correction by adopting seq2seq model with LSTM.

## Instruction to Run 

1. file structure:

    .
    ├── ...
    ├── docs                    # Documentation files (alternatively `doc`)
    │   ├── TOC.md              # Table of contents
    │   ├── faq.md              # Frequently asked questions
    │   ├── misc.md             # Miscellaneous information
    │   ├── usage.md            # Getting started guide
    │   └── ...                 # etc.
    └── ...

  .   
  ├── correct_text.py   
  ├── data_reader.py  
  ├── dataset_sep.py        
  ├── preprocessor.py   
  ├── seq2seq.py  
  ├── text_corrector_data_readers.py               
  ├── data   
  │     └── cornell-movie-dialogs-corpus  
  │         └── movie_lines.txt  
  └── text_corrector_models.py 


1. Environment Requirement:  
* GPU: TITAN V (fast for speed) 
* Ubuntu 16.04.6 LTS, Python 3.5.2 (must be this version)
* Library: tensorflow 0.12.0 (must be this version), nltk, pandas, scikit-learn, collections

3. Train:
```python
python correct_text.py  -- train_path PATH OF TRAINING DATA
                        -- val_path PATH OF VALIDATING DATA
                        -- config DefaultMovieDialogConfig 
                        -- data_reader_type MovieDialogReader
                        -- model_path PATH OF SAVED MODEL
```
4. Test:
```ptthon
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

5. Load model:
```python
model = create_model(sess, True, model_path, config=config)
```
