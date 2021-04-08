# LeafyAI
This project was created by me and my teammate as a part of our 6th sem major project in JIST Jorhat. The project uses machine learning to predict the type of disease from an image of plant leaf. It uses django framework in backend

This repo is not deployable to heroku

There are a  few things you will require to make this project work if you are cloning it:
1. To make the Chatbot work you need Dialogflow credentials from google placed in the root directory and added in 'views.py' as well
2. For the mail system to work you need to place Username and Password in 'settings.py' file.
3. Lastly for the prediction to work you need the trained model placed within a 'Model' folder inside 'potato'. The model name must be added in 'view.py' as well. 
