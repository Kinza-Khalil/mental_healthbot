import os
import openai
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa.shared.core.events import UserUtteranceReverted
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


class ActionFetchDepressionInfo(Action):
    def name(self) -> Text:
        return "action_fetch_depression_info"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that provides information about mental health issues."},
                {"role": "user", "content": user_message}
            ]
        )

        assistant_message = response.choices[0].message['content']

        dispatcher.utter_message(text=assistant_message)

        return []

class ActionFetchAnxietyInfo(Action):
    def name(self) -> Text:
        return "action_fetch_anxiety_info"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that provides information about mental health issues."},
                {"role": "user", "content": user_message}
            ]
        )

        assistant_message = response.choices[0].message['content']

        dispatcher.utter_message(text=assistant_message)

        return []

class ActionFetchCopingStrategies(Action):
    def name(self) -> Text:
        return "action_fetch_coping_strategies"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that provides information about mental health issues."},
                {"role": "user", "content": user_message}
            ]
        )

        assistant_message = response.choices[0].message['content']

        dispatcher.utter_message(text=assistant_message)

        return []

class ActionProvideProfessionalHelpInfo(Action):
    def name(self) -> Text:
        return "action_provide_professional_help_info"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that provides information about mental health issues."},
                {"role": "user", "content": user_message}
            ]
        )

        assistant_message = response.choices[0].message['content']

        dispatcher.utter_message(text=assistant_message)

        return []

class ActionFetchSelfHelpResources(Action):
    def name(self) -> Text:
        return "action_fetch_self_help_resources"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that provides information about mental health issues."},
                {"role": "user", "content": user_message}
            ]
        )

        assistant_message = response.choices[0].message['content']

        dispatcher.utter_message(text=assistant_message)

        return []

class ActionFetchSupportGroupsInfo(Action):
    def name(self) -> Text:
        return "action_fetch_support_groups_info"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that provides information about mental health issues."},
                {"role": "user", "content": user_message}
            ]
        )

        assistant_message = response.choices[0].message['content']

        dispatcher.utter_message(text=assistant_message)

        return []

class ActionProvideEmergencyResourcesInfo(Action):
    def name(self) -> Text:
        return "action_provide_emergency_resources_info"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that provides information about mental health issues."},
                {"role": "user", "content": user_message}
            ]
        )

        assistant_message = response.choices[0].message['content']

        dispatcher.utter_message(text=assistant_message)

        return []

class ActionDefaultFallback(Action):
    def name(self):
        return "action_default_fallback"

    async def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="I'm not sure how to help with that. Can you please rephrase your question?")
        return [UserUtteranceReverted()]

class ActionDefaultAskAffirmation(Action):
    def name(self):
        return "action_default_ask_affirmation"

    async def run(self, dispatcher, tracker, domain):
        message = "I didn't understand your question. Can you please try again?"
        buttons = [
            {"title": "Yes", "payload": "/affirm"},
            {"title": "No", "payload": "/deny"},
        ]
        dispatcher.utter_message(text=message, buttons=buttons)
        return []
