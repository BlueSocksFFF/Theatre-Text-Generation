# Theatre-Text-Generation

## General Languages and Packages Required
Python == 3.10+


## Language Model

We are invoking the GPT3 "text-davinci-003" model for generation of monologues.

We are now also invoking GPT3.5 Turbo model for generation

Our goal is to simultaneously compute monologues and pick the one that generates faster to pass back to the Avatar

#### Files

Main.py

 We are switching to a more modular based approach where main.py is less important. 

 At this point, main.py demonstrates the ability to take raw text and extract sentiment and key phrases from that text. 

 It then passes those key phrases into a prompt format and through to our GPT3 monologue generator. 



api_client.py  

    write_to_api(content, file)
    Writes to the Avatar API. Write will rewrite the file, not append to it. Write will create a file if one does not exist.
    
    append_to_api(content, file)
       

    read_from_api(file)
        

    read_latest_from_api(file)




#### Installation
We recommend that you download the packages in a virtual environment.
In Windows:
```
py -m venv env
```
To activate: 
```
env\Scripts\activate
```
After you have your virtual environment set up, run the command below to install all of the packages relevant to this project.

```
pip install -r requirements.txt

```
If the above command does not work, refer to requirements.txt and download the individual packages.

#### Environment Variables
To run our generator, you would need to obtain your own API keys. Please refer to the .env.example file, which is a template for your .env file, and create your own .env file and put down your API keys there. Make sure to keep them to yourself, hence we did not include any API keys in this repo.
