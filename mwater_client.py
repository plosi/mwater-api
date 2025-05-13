import requests
import os
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

class MWaterClient:
    def __init__(self):
        self.base_url = "https://api.mwater.co/v3"  # Base URL for the mWater API
        self.api_key = os.getenv("MWATER_API_KEY")  # API key from environment variables
        if not self.api_key:
            raise ValueError("API key not found. Please set MWATER_API_KEY in your .env file.")

        self.headers = {
            # "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get_survey(self, survey_id):
        """Fetch a survey by its ID."""
        if not survey_id:
            raise ValueError("survey_id must be provided")
        filter_query = json.dumps({"_id": survey_id})  # Properly format the filter as a JSON string
        url = f"{self.base_url}/forms?filter={filter_query}&client={self.api_key}"
        # print(url)
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_survey_question(self, survey_id, updated_data):
        """Update a specific question in a survey."""
        # url = f"{self.base_url}/forms/{survey_id}/questions/{question_id}"
        url = f"{self.base_url}/forms/{survey_id}?client={self.api_key}"
        response = requests.post(url, headers=self.headers, json=updated_data)
        print(response)
        response.raise_for_status()
        return response.json()

    def list_surveys(self):
        """List all surveys."""
        url = f"{self.base_url}/forms"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()