import torch
from transformers import BertTokenizer, BertForSequenceClassification
import pandas as pd

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def load_csv_tokenizer(input_data_path):
    # Load the modified CSV file
    file_path = input_data_path
    df_new = pd.read_csv(file_path)

    
    # Load the saved model and tokenizer
    model_name = "00PJH/klue-bert-tunning-classification-military-news"
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertForSequenceClassification.from_pretrained(model_name)
    model.to(device)
    model.eval()

    tokenize_encode(df_new, tokenizer,model)

def tokenize_encode(df_new, tokenizer, model):
    # Tokenize and encode the titles from the new CSV
    texts = df_new['title'].tolist()  # Extract the titles
    encoded_data = tokenizer(texts, padding=True, truncation=True, return_tensors='pt', max_length=512)
    input_ids = encoded_data['input_ids'].to(device)
    attention_mask = encoded_data['attention_mask'].to(device)

    
    perform_inference(model, input_ids, attention_mask, df_new)

def perform_inference(model, input_ids, attention_mask, df_new):
    with torch.no_grad():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        preds = torch.argmax(outputs.logits, dim=1)

    # Convert predictions back to labels (0 or 1)
    predictions = preds.cpu().numpy()
    df_new['predictions'] = predictions  # Add predictions to the DataFrame

    return df_new