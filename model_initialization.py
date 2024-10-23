import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from IndicTransTokenizer import IndicProcessor
model_name = "indictrans2-en-indic-1B"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name, trust_remote_code=True)
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
#DEVICE = "cuda"
print(DEVICE)
model.to(DEVICE)
ip = IndicProcessor(inference=True)

def translation(text: str):
    input_sentences = [text]
    src_lang, tgt_lang = "eng_Latn", "urd_Arab"
    
    batch = ip.preprocess_batch(input_sentences, src_lang=src_lang, tgt_lang=tgt_lang)
    inputs = tokenizer(batch, truncation=True, padding="longest", return_tensors="pt", return_attention_mask=True).to(DEVICE)
    
    with torch.no_grad():
        generated_tokens = model.generate(**inputs, use_cache=True, min_length=0, max_length=1024, num_beams=5, num_return_sequences=1, temperature =0)
    
    with tokenizer.as_target_tokenizer():
        generated_tokens = tokenizer.batch_decode(generated_tokens.detach().cpu().tolist(), skip_special_tokens=True, clean_up_tokenization_spaces=True)
    
    translations = ip.postprocess_batch(generated_tokens, lang=tgt_lang)
    
    translated_text = translations[0] if translations else ""
    return translated_text