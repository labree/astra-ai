# astra-ai

Outline on how to create astra ai:

1. Extract wiki pages for QA pairs, and facts
2. Extract discord servers for QA pairs (specifcally the newbie help channels)
3. Organize dataset
4. Finetune gemini through VertexAI
5. launch to an endpoint through VertexAI

Steps not organized:
- Create site for usage
- Create discord bot
- make dataset embeddings for efficient RAG search so that on top of finetuning recent data is availible to the model.
- make a script to regularly get text data from discord and updated wiki pages and make them into embeddings so that retraining is not required as frequently


discord chat export tool:
https://github.com/Tyrrrz/DiscordChatExporter

fandom-wiki download tool:
https://github.com/GOLEM-lab/fandom-wiki
