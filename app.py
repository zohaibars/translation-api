from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model_initialization import translation

class TranslationRequest(BaseModel):
    text: str

class TranslationResponse(BaseModel):
    source_language: str
    target_language: str
    input_text: str
    translated_text: str


app = FastAPI()

@app.post("/translate", response_model=TranslationResponse)
def translate(request: TranslationRequest):
    input_sentences = [request.text]
    src_lang, tgt_lang = "eng_Latn", "urd_Arab"
    translated_text = translation(text=input_sentences)
    return TranslationResponse(
        source_language=src_lang,
        target_language=tgt_lang,
        input_text=request.text,
        translated_text=translated_text
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8091, reload = True)
