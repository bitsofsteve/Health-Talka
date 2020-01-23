# Juddie

`Juddie` is Mobicure's Health Assistant, designed to make initial symptom analysis for patients, before passing it on to a doctor

## Stage

`Juddie` is at it's *Proof of concecpt* stage as at *17/1/20*

## What’s inside this codebase?

This codebase contains some training data and the main files needed to run 
`Juddie` on your local machine. The codebase consists of the following files:

- **data/nlu.md** contains training examples for the NLU model  
- **data/stories.md** contains training stories for the Core model
- **actions.py** contains the implementation of a custom `Action`
- **config.yml** contains the model configuration
- **domain.yml** contains the domain of the assistant  
- **endpoints.yml** contains the webhook configuration for the custom actions

## How to use this example?

You can test the example using the following
steps:

1. Install Rasa by running (Skip if you have rasa installed already):

    Visit [Rasa Guide For Installation](https://rasa.com/docs/rasa/user-guide/installation/)
    

1. Train a Rasa model containing the Rasa NLU and Rasa Core models by running:
    ```
    rasa train
    ```
    The model will be stored in the `/models` directory as a zipped file.

  

3. Test the assistant by running:
    ```
    rasa run actions
    ```
    This will run the actions in an ednpoint.

4. Then to use Rasa x to test (rasa x can allow to test the button feel of delivering Payloads)

   ```
   rasa x
   ```
   This will start up Rasa x, then you can talk to the bot

   Note: for some reasons ``` run actions``` and ```rasa shell``` have port conflicts

For more information about the individual commands, please check out our
[documentation](http://rasa.com/docs/rasa/user-guide/command-line-interface/).

## Encountered any issues?
Open up a gist 



## Todos

- This is gonna be updates soon