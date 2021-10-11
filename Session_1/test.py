import pytest
import os
import pandas as pd

def test_datazip_exists():
    assert not os.path.isfile("data.zip"), "Data.zip is present!"

def test_model_file_exists():
    assert not os.path.isfile("model.h5"), "Model.h5 is present!"

def test_model_file_exists():
    assert os.path.isfile("metrics.csv"), "metrics.csv file missing!"

def test_accuracy():
    accuracy_data=pd.read_csv("metrics.csv")
    acc=accuracy_data["overall_accuracy"][-1]
    assert acc>0.7,"Your accuracy is less than 70%"

def test_accuracy_categorywise():
    accuracy_data=pd.read_csv("metrics.csv")
    cat_acc=accuracy_data["cat_accuracy"][-1]
    assert cat_acc>0.7,"Your cat accuracy is less than 70%"

def test_accuracy_categorywise():
    accuracy_data=pd.read_csv("metrics.csv")
    dog_acc=accuracy_data["dog_accuracy"][-1]
    assert dog_acc>0.7,"Your dog accuracy is less than 70%"
