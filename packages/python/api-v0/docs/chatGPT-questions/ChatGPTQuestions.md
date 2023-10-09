ChatGPTQuestions.md


I am build a Chat that can respond exclusively IRS related questions nothing more nothing less. 

How could I build this using the "OpenAI" API and "Fine Tuning". 

Accourding to the documentation, there are 4 steps to follow: 

1. Prepare your data. ```{
  "messages": [
    { "role": "system", "content": "You are an assistant that occasionally misspells words" },
    { "role": "user", "content": "Tell me a story." },
    { "role": "assistant", "content": "One day a student went to schoool." }
  ]
}```

What does each of these roles mean and for this use case(IRS Questions) what could an example?

Could for "user" role be something like this?

```
{ "role": "user", "content": 
"
My client is single, currently employed by Company A
as well as consulting contract for Company C.

Bought X amount of stocks at Company D at price Y and
sold such Company C stock the same year for Z price.

X dollars where collected through saving accounts interest.

Company stock F distributed X dollars in dividends.

Client is shareholder of a s-corporation and c-corporation
that had a net income and distributed dividends.

Client owns a few properties that are currently
rented through a property manager.

Some of the propertities had an amortization and depreciation.

One of the properties is under a mortgage
with around 5% interest rate.

Earlier this year one of the properties suffered damages from a
natural disaster and had to do repairs, purchase new
furnitures and appliances.

What forms do I need to file, receive, attach etc etc?

" }

```

2. Upload files
```
curl https://api.openai.com/v1/files \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F "purpose=fine-tune" \
  -F "file=@path_to_your_file" 
  ```

What if I need to upload 2000k PDF files that will be convert to .txt files though a lot of them exceed the amount of tokens. 

Does it have to one file at the time? 

3. Create a fine-tuning job

curl https://api.openai.com/v1/fine_tuning/jobs \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{
  "training_file": "TRAINING_FILE_ID",
  "model": "gpt-3.5-turbo-0613"
}'

Where do I getn the "training_file": "TRAINING_FILE_ID" ?

4. Use a fine-tuned model.

```curl https://api.openai.com/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{
  "model": "ft:gpt-3.5-turbo:org_id",
  "messages": [
    {
      "role": "system",
      "content": "You are an assistant that occasionally misspells words"
    },
    {
      "role": "user",
      "content": "Hello! What is fine-tuning?"
    }
  ]
}'
```

For our use case what would be an example of the

```    {
      "role": "user",
      "content": "Hello! What is fine-tuning?"
    }
```

