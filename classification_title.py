import torch
from transformers import BertTokenizer, BertForSequenceClassification
import pandas as pd

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def load_csv_tokenizer(input_data):
    # Load the modified CSV file
    df_new = input_data
    
    # Load the saved model and tokenizer
    model_name = "00PJH/klue-bert-tunning-classification-military-news"
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertForSequenceClassification.from_pretrained(model_name)
    model.to(device)
    model.eval()

    return df_new, tokenizer,model

def tokenize_encode(df_new, tokenizer, model):
    # Tokenize and encode the titles from the new CSV
    texts = df_new['title'].tolist()  # Extract the titles
    encoded_data = tokenizer(texts, padding=True, truncation=True, return_tensors='pt', max_length=512)
    input_ids = encoded_data['input_ids'].to(device)
    attention_mask = encoded_data['attention_mask'].to(device)

    
    return model, input_ids, attention_mask, df_new

def perform_inference(model, input_ids, attention_mask, df_new):
    with torch.no_grad():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        preds = torch.argmax(outputs.logits, dim=1)

    # Convert predictions back to labels (0 or 1)
    predictions = preds.cpu().numpy()
    df_new['predictions'] = predictions  # Add predictions to the DataFrame

    return df_new

def run(input_data):
    df_tk_md = load_csv_tokenizer(input_data)
    encode = tokenize_encode(df_tk_md[0], df_tk_md[1], df_tk_md[2])
    result_df = perform_inference(encode[0],encode[1],encode[2],encode[3])

    filtered_df = result_df[result_df['predictions'] == 1]
    return filtered_df
