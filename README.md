## Running with Docker guide 
### First build the image:
```
    sudo docker compose up --build
```
## Download model
RUN git lfs install && \
    git clone https://huggingface.co/ai4bharat/indictrans2-en-indic-1B

### Open a seperate terminal and enter the container:
```
    sudo docker exec -it english_to_urdu_translation-translation-api-1 /bin/bash
```
### run the following commands:
```
    git clone https://github.com/VarunGumma/IndicTransTokenizer /app/IndicTransTokenizer
```
```
    pip install --editable /app/IndicTransTokenizer
```
