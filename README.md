# Grammatic Error Corrector

## Instruction to Run

Environment Requirement:   
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
## News
~~2019.08.10: Code test passes~~