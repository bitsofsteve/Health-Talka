## Main Happy Path

* greet
    - utter_juddie_greet
    - utter_symptom_ask
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
    - slot{"symptom_duration":"About 1 hour"}
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
    - slot{"symptom_nausea":"No"}
    - slot{"requested_slot":"headache_pain"}
* affirm
    - headache_form
    - slot{"headache_pain":"Yes"}
    - slot{"requested_slot":"headache_tearing"}
* affirm
    - headache_form
    - slot{"headache_tearing":"No"}
    - slot{"requested_slot":"headache_nasal"}
* affirm
    - headache_form
    - slot{"headache_nasal":"No"}
    - slot{"requested_slot":"headache_facial"}
* affirm
    - headache_form
    - slot{"headache_facial":"No"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_default_fallback
    - utter_slots_values
    - utter_follow_up
