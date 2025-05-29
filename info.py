import requests
import json

url = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info"

# Input collection
student_data = {
    "UCID": "mr822",
    "first_name": "Mariano",
    "last_name": "Ramos",
    "github_username": "mramos822",
    "discord_username": "bluelite",
    "favorite_cartoon": "Regular Show",
    "favorite_language": "Python",
    "movie_or_game_or_book": "Portal 2"
}

try:
    # Make the POST request
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, json=student_data)

    # Output result
    print(f"Status Code: {response.status_code}")
    print("Response Body:", response.text)

    # Check for success
    if response.status_code == 200:
        print("✅ Information successfully submitted.")
    else:
        print("❌ Submission failed. Check data or endpoint.")

except requests.RequestException as e:
    print("❌ An error occurred:", e)
