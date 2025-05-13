from mwater_client import MWaterClient

class SurveyUpdater:
    def __init__(self):
        self.client = MWaterClient()

    def update_question(self, survey_id, updated_data):
        """
        Updates a specific question in a survey.

        Args:
            survey_id (str): The ID of the survey.
            updated_data (dict): The updated question data.

        Returns:
            dict: The API response containing the updated question details.
        """
        try:
            response = self.client.update_survey_question(survey_id, updated_data)
            print(f"Successfully updated survey {survey_id}.")
            return response
        except Exception as e:
            print(f"Failed to update question survey {survey_id}: {e}")
            raise

    def list_surveys(self):
        """
        Lists all surveys available in the account.

        Returns:
            list: A list of surveys.
        """
        try:
            surveys = self.client.list_surveys()
            print("Successfully retrieved surveys.")
            return surveys
        except Exception as e:
            print(f"Failed to retrieve surveys: {e}")
            raise