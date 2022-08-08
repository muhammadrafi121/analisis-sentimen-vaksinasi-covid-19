# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 05:18:19 2022

@author: Acer
"""

import os
import re
import torch
import pandas as pd
from torch.utils.data import Dataset
from transformers import (XLNetConfig, 
                          XLNetForSequenceClassification, 
                          XLNetTokenizer,
                          )

class Model:
    def __init__(self):
        pass
    
    def clean_text(self, line):
        # cleaning wild char except maybe a repetition word
        cleanline = re.sub(r"[^\w\s\-]", " ", line).lower()
    
        # cleaning number
        cleanline = re.sub('[0-9]', ' ', cleanline)
    
        # cleaning non indonesian character
        cleanline = re.sub(r"[^(a-z)+\s{1}]", "", cleanline)
    
        # cleaning whitespaces
        cleanline = re.sub(r"\s+", " ", cleanline)
        return cleanline
    
    def load_xlnet_model(self, model_type, n_labels):
        model_path = f"./xlnetmodel/model-{model_type}"
        
        config = XLNetConfig.from_pretrained(
            pretrained_model_name_or_path=model_path, 
            num_labels=n_labels
            )
        
        xlnetmodel = XLNetForSequenceClassification.from_pretrained(
            pretrained_model_name_or_path=model_path, 
            config=config
            )
        
        return config, xlnetmodel
    
    def load_tokenizer(self, model_type):
        model_path = f"./xlnetmodel/model-{model_type}"
        
        tokenizer = XLNetTokenizer.from_pretrained(
            pretrained_model_name_or_path=model_path
            )
        return tokenizer
    
    def load_dataset(self, path, tokenizer, labels_ids, max_sequence_len=None):
        return CommentsDataset(
            path=path, 
            use_tokenizer=tokenizer, 
            labels_ids=labels_ids, 
            max_sequence_len=max_sequence_len
            )
    
class CommentsDataset(Dataset):
    def __init__(self, path, use_tokenizer, labels_ids, max_sequence_len=None):
        # load model object
        self.model = Model()
        self.text_data = []
        
        # Check if file exists.
        """
        if not os.path.exists(path):
            # Raise error if path is invalid.
            raise ValueError('Invalid `path` variable! Needs to be a .csv file')
        """  
        # Check max sequence length.
        max_sequence_len = use_tokenizer.max_len if max_sequence_len is None else max_sequence_len
        texts = []
        labels = []
        print('Reading file...')
        df = pd.read_csv(path, on_bad_lines='error')
        df = df.reset_index()  # make sure indexes pair with number of rows
        for index, row in df.iterrows():
            text = self.model.clean_text(row['text'])
            texts.append(text)
            labels.append(labels_ids[row['label']])
            
        for i in range(len(texts)):
            tmplabel = 'Positif' if labels[i] == 1 else 'Negatif'
            self.text_data.append([
                texts[i], tmplabel
                ])

        # Number of exmaples.
        self.n_examples = len(labels)
        # Use tokenizer on texts. This can take a while.
        print('Using tokenizer on all texts. This can take a while...')
        self.inputs = use_tokenizer(
            texts, 
            add_special_tokens=True, 
            truncation=True, 
            padding=True, 
            return_tensors='pt', 
            max_length=max_sequence_len
        )
        # Get maximum sequence length.
        self.sequence_len = self.inputs['input_ids'].shape[-1]
        print('Texts padded or truncated to %d length!' % self.sequence_len)
        # Add labels.
        # self.inputs.update({'texts': texts})
        self.inputs.update({'labels':torch.tensor(labels)})
        print('Finished!\n')

        return

    def __len__(self):
        return self.n_examples

    def __getitem__(self, item):
        return {key: self.inputs[key][item] for key in self.inputs.keys()}