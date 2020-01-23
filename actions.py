from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class HeadacheForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "headache_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the headache form has to fill"""

        return ["patient_sex",
                "patient_age",
                "symptom_duration",
                "headache_location",
                "headache_pounding",
                "symptom_nausea",
                "headache_pain",
                "headache_tearing",
                "headache_nasal",
                "headache_facial"]
    


    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return{
            "patient_sex" : self.from_text(intent="inform"),
            "patient_age" : self.from_text(),
            "symptom_duration" : self.from_text(),
            "symptom_nausea" : self.from_text(),
            "headache_location" : self.from_text(),
            "headache_pounding" : self.from_text(),
            "headache_pain" : self.from_text(),
            "headache_tearing" : self.from_text(),
            "headache_nasal" : self.from_text(),
            "headache_facial" : self.from_text(),
            
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_goodbye")
        return []
