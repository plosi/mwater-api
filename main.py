from survey_updater import SurveyUpdater
import json

def main():
    print("Welcome to the mWater API Survey Updater!")

    # Initialize the SurveyUpdater
    updater = SurveyUpdater()

    #  Example: Fetch a specific survey
    survey_id = "c6ef70b762064235847d8f6d0acd3efb"

    # try:
    #     print("Fetching survey...")
    #     survey = updater.client.get_survey(survey_id)
    #     survey = json.loads(json.dumps(survey[0]))
    #     print(survey)
    # except Exception as e:
    #     print(f"Error fetching survey: {e}")

    # # Example: List all surveys
    # print("Fetching surveys...")
    # surveys = updater.list_surveys()
    # for survey in surveys:
    #     # print(survey)
    #     print(f"Survey ID: {survey['_id']}")#, Name: {survey['name']}")

    # Example: Update a specific question in a survey
    # survey_id = input("Enter the survey ID to update: ")
    # question_id = input("Enter the question ID to update: ")

    # updated_data = {
    #     "text": input("Enter the new question text: "),
    #     "type": input("Enter the new question type: ")  # Example: "text", "number", etc.
    # }

    updated_data = {
        "design": {
            "contents":[
                {"_id": "d44b54afae18434e8b9c332d505827bb", "value": "916477118"},
                {"_id": "8803bfa9489f46d2b18dc71d9135cd48", "value": 3.2}
            ]
        }
    }

    try:
        response = updater.update_question(survey_id, updated_data)
        print("Updated question successfully!")
        print(response)
    except Exception as e:
        print(f"Error updating question: {e}")


if __name__ == "__main__":
    main()