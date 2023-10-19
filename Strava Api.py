# Import necessary library
from stravalib.client import Client

# Initialize the Client
client = Client()

# Set your access token directly
client.access_token = '542f05e94aa312f248581561da16734e7a419b9b'

def get_all_activities():
    # Fetch all activities of the authorized user
    activities = client.get_activities()
    for activity in activities:
        print(f'Activity ID: {activity.id}, Name: {activity.name}, Distance: {activity.distance}, Start Date: {activity.start_date_local}')

if __name__ == "__main__":
    get_all_activities()  # Fetch all activities
