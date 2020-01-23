## symptom_checker happy path
* greet
  - utter_juddie_greet
* headache_symptom_match{"symptom": "headache"}
  - headache_form
  - form{"name": "headache_form"}
  - form{"name": null}
  - utter_slots_values
* thank_you
  - utter_goodbye

## Very Happy Path

* greet
    - utter_juddie_greet
* headache_symptom_match{"headache_symptom":"headache"}
    - headache_form
    - form{"name":"headache_form"}
    - slot{"requested_slot":"patient_sex"}     
* inform{"patient_sex":"Male"}
    - headache_form
    - slot{"patient_sex":"Male"}
    - slot{"requested_slot":"patient_age"}
* inform{"patient_age":"20"}
    - headache_form
    - slot{"patient_age":"20"}
    - slot{"requested_slot":"symptom_duration"}

    """
    Form actions tend to create
    a repetitive call to the form methods, it says, 
    1- select the form action
    2- request_slot to be filled
    3- user will give an input (This input is mapped to intent{entity:value})
    4- Once the entity is predicted , call the headache-form again and set the slot to the value
    5- start from 1
    """

## Headache Very Happy Path

* greet
    - utter_juddie_greet
* headache_symptom_match{"headache_symptom":"Headache"}
    - headache_form
    - form{"name":"headache_form"}
    - slot{"requested_slot":"patient_sex"}
* inform{"patient_sex":"Male"}
    - headache_form
    - slot{"patient_sex":"Male"}
    - slot{"requested_slot":"patient_age"}
* inform{"patient_age":"20"}
    - headache_form
    - slot{"patient_age":"20"}
    - slot{"requested_slot":"symptom_duration"}
* inform{"symptom_duration":"2 days"}
    - headache_form
    - slot{"symptom_duration":"2 days"}
    - slot{"requested_slot":"headache_location"}
* inform{"headache_location":"One side"}
    - headache_form
    - slot{"headache_location":"One side"}
    - slot{"requested_slot":"headache_pounding"}
* affirm
    - headache_form
    - slot{"headache_pounding":"Yes"}
    - slot{"requested_slot":"symptom_nausea"}
* affirm
    - headache_form
    - slot{"symptom_nausea":"Yes"}
    - slot{"requested_slot":"headache_pain"}
* affirm
    - headache_form
    - slot{"headache_pain":"Yes"}
    - slot{"requested_slot":"headache_tearing"}
* affirm
    - headache_form
    - slot{"headache_tearing":"Yes"}
    - slot{"requested_slot":"headache_nasal"}
* affirm
    - headache_form
    - slot{"headache_nasal":"Yes"}
    - slot{"requested_slot":"headache_facial"}
* affirm
    - utter_slots_values
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_default_fallback

## New Story

* greet
    - utter_juddie_greet
* headache_symptom_match{"headache_symptom":"Headache"}
    - headache_form
    - form{"name":"headache_form"}
    - slot{"requested_slot":"patient_sex"}
* inform{"patient_sex":"Male"}
    - headache_form
    - slot{"patient_sex":"Male"}
    - slot{"requested_slot":"patient_age"}
* inform{"patient_age":"20"}
    - headache_form
    - slot{"patient_age":"20"}
    - slot{"requested_slot":"symptom_duration"}
* inform{"symptom_duration":"1 hour"}
    - headache_form
    - slot{"symptom_duration":"Less than 1 hour"}
    - slot{"requested_slot":"headache_location"}
* inform{"headache_location":"One side"}
    - headache_form
    - slot{"headache_location":"One side"}
    - slot{"requested_slot":"headache_pounding"}
* affirm
    - headache_form
    - slot{"headache_pounding":"Yes"}
    - slot{"requested_slot":"symptom_nausea"}
* inform
    - headache_form
    - slot{"symptom_nausea":"No"}
    - slot{"requested_slot":"headache_pain"}
* affirm
    - headache_form
    - slot{"headache_pain":"Yes"}
    - slot{"requested_slot":"headache_tearing"}
* inform
    - headache_form
    - slot{"headache_tearing":"No"}
    - slot{"requested_slot":"headache_nasal"}
* affirm
    - headache_form
    - slot{"headache_nasal":"Yes"}
    - slot{"requested_slot":"headache_facial"}
* inform
    - utter_slots_values
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_default_fallback
