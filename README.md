# LangChain - Open Source Large Language Models 

This repository is for Learning and Experimenting with Open Source Large Language Models and Embeddings.

### Overview
Groq is a high-performance inference engine for large language models. It is designed to be highly efficient
and scalable, making it suitable for a wide range of applications.

### Open Source Large Language Models
1. Llama
2. Mistral
3. Ollama

### Open Source Embeddings
1. Sentence Transformers
2. Hugging Face Transformers

### Install dependencies :
 Make sure Python is installed, then install the required packages:

   ```bash
    pip install -r requirements.txt
   ```

### Set up Environment Variables :

* **Create an `.env` file in the root directory** :
* **Add the following environment variables to the .env file** :

    ```bash
    GROQ_API_KEY = your_groq_api_key

    HUGGINGFACE_API_KEY = your_huggingface_api_key
    ```


### Getting Started
1. Ensure you have Python and FastAPI installed in your environment.
2. Install the required dependencies.
3. Set up the environment variables.
4. Start the FastAPI server:

    ```bash
    uvicorn server:app --reload
    ```
4. Use a tool like Postman or curl to interact with the /chat endpoint.
5. You can also use the Swagger UI to interact with the API by visiting http://127.0.0.1:8000/docs or use http://127.0.0.1:8000/redoc in your browser.

### FastAPI Endpoints

1. **http://127.0.0.1:8000/chat** : 
    * **Method** : POST
    * **Request Body** : 

        ```json
        {
            "user_input": "What is Generative AI?",
            "language": "France"
        }
        ```
    * **Response** : 

        ```json
        {
            "response": "Les grands modèles de langage"
        }
        ```
