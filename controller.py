# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 05:18:28 2022

@author: Acer
"""

import time
import torch
from tqdm.notebook import tqdm
from torch.utils.data import DataLoader

from model import Model
from view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)
        
        self.history = []
        
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    def evaluate(self, dataloader):
        # Tracking variables
        predictions_labels = []
        true_labels = []
        #total loss for this epoch.
        total_loss = 0
    
        # Put the model in evaluation mode--the dropout layers behave differently
        # during evaluation.
        self.xlnetmodel.eval()
    
        # Evaluate data for one epoch
        for batch in tqdm(dataloader, total=len(dataloader)):
    
            # add original labels
            true_labels += batch['labels'].numpy().flatten().tolist()
    
            # move batch to device
            batch = {k:v.type(torch.long).to(self.device) for k,v in batch.items()}
    
            with torch.no_grad():        
    
                outputs = self.xlnetmodel(**batch)
    
                loss, logits = outputs[:2]
    
                logits = logits.detach().cpu().numpy()
    
                total_loss += loss.item()
    
                predict_content = logits.argmax(axis=-1).flatten().tolist()
    
                predictions_labels += predict_content
    
        avg_epoch_loss = total_loss / len(dataloader)
    
        return true_labels, predictions_labels, avg_epoch_loss
    
    def getdataset(self, file_path):
        if not file_path.endswith('.csv'):
            # Raise error if path is invalid.
            self.view.showerror()
        else:
            labels_ids = {'negatif': 0, 'positif': 1}
            max_length = 512
            
            self.tokenizer = self.model.load_tokenizer(1)
            
            self.test_dataset = self.model.load_dataset(
                path=file_path, 
                tokenizer=self.tokenizer, 
                labels_ids=labels_ids, 
                max_sequence_len=max_length
                )
            
            data = self.test_dataset.text_data
            self.view.showresult(data)
    
    def run_test(self, config_type, file_path):
        
        if not file_path.endswith('.csv'):
            # Raise error if path is invalid.
            self.view.showerror()
        else:
            labels_ids = {'negatif': 0, 'positif': 1}
            n_labels = len(labels_ids)
            
            config_dict = {
                "Epochs 3 & Batch Size 16": 1,
                "Epochs 4 & Batch Size 16": 2,
                "Epochs 3 & Batch Size 32": 3,
                "Epochs 4 & Batch Size 32": 4,
                "Epochs 3 & Batch Size 50": 5,
                "Epochs 4 & Batch Size 50": 6
                }
            
            self.config, self.xlnetmodel = self.model.load_xlnet_model(
                config_dict[config_type], n_labels)
            
            self.xlnetmodel.to(self.device)
            
            if "Batch Size 16" in config_type:
                batch_size = 16
            elif "Batch Size 32" in config_type:
                batch_size = 32
            elif "Batch Size 50" in config_type:
                batch_size = 50
            
            test_dataloader = DataLoader(
                self.test_dataset, 
                batch_size=batch_size, 
                shuffle=False
                )
            
            data = self.test_dataset.text_data
            
            start = time.time()
            
            true_labels, predictions_labels, avg_epoch_loss = self.evaluate(test_dataloader)
            
            for i in range(len(predictions_labels)):
                tmplabel = 'Positif' if predictions_labels[i] == 1 else 'Negatif'
                if len(data[i]) == 2:
                    data[i].append(tmplabel)
                else:
                    data[i][2] = tmplabel
                
            self.view.showresult(data)
            
            tn = tp = fn = fp = 0
            
            for i in range(len(true_labels)):
                if true_labels[i] == 0:
                    if predictions_labels[i] == 0:
                        tn += 1
                    else:
                        fp += 1
                else:
                    if predictions_labels[i] == 1:
                        tp += 1
                    else:
                        fn += 1
            
            acc = (tp + tn) / (tp + fp + tn + fn)
            prec = tp / (tp + fp)
            rec = tp / (tp + fn)
            fscore = (2 * prec * rec) / (prec + rec)
            
            self.history.append(
                [
                    config_type, 
                    tp, 
                    fp, 
                    tn, 
                    fn, 
                    acc,
                    prec,
                    rec,
                    fscore,
                    (time.time() - start)
                    ]
                )
            
            self.view.showhistory(self.history)
    
    def main(self):
        self.view.main()
    
if __name__ == '__main__':
    controller = Controller()
    controller.main()