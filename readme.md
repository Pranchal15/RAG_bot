Want to give it a try?
Go to : https://pranchal15-rag-bot-streamlit-app-5kqfex.streamlit.app/
It is a work in progress. Feel free to submit issues! 

How to set it up on your own and play around?
1. create and activate a conda env
2. Install all the requirements - pip install -r requirements.txt
3. download model weights - python download_mistral.py
4. start vllm server - python -m vllm.entrypoints.openai.api_server   --model ./models/mistral   --gpu-memory-utilization 0.90   --max-model-len 8192
5. Test 
5. run your streamlit app - streamlit run app.py
