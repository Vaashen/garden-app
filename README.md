># Natural language Processing

This is a simple python application that reads from a list that contains 5 garden path sentences. It is using spaCy which is a python NLP library specifically designed with the goal of being a useful library for implementing production-ready systems.

It will Tokenise each sentence in the list and perform entity recognition.

<br>

>## How to run the application

- Download the folder from the repo.
- Open the command windoe, you can use the shortcut "Windows button + R " and type in "cmd" and press enter.
- Next you will need to navegate to the directory that contains the folder, use the `cd` followed by the folder/file name, until you get into the folder
- Next type in the command: `docker build -t garden-app`
- Then: `docker run -i garden-app`

if everything wentwell the application to should run adn you should see a list of each word and their entities.

