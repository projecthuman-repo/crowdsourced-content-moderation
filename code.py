#Thia ia helpful if we want to connect with PYBOSSA Client using Projecthumancity api

import requests
import json
from pybossa import PyBossa

# Configuration
PYBOSSA_API_KEY = 'YOUR_PYBOSSA_API_KEY'
PYBOSSA_ENDPOINT = 'http://your-pybossa-instance.com'
PROJECTHUMANCITY_API_ENDPOINT = 'http://your-website.com/api'

# Initialize PYBossa client
pybossa = PyBossa(PYBOSSA_API_KEY, PYBOSSA_ENDPOINT)

# Function to fetch content for moderation from your website's API
def fetch_content_for_moderation():
    response = requests.get(f'{PROJECTHUMANCITY_API_ENDPOINT}/content_to_moderate')
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch content for moderation")

# Function to create tasks in PYBossa
def create_pybossa_tasks(content_list):
    project_id = 1  # Replace with your PYBossa project ID
    tasks = []
    for content in content_list:
        task = {
            'project_id': project_id,
            'info': {
                'content_id': content['id'],
                'text': content['text']
            }
        }
        tasks.append(task)
    pybossa.create_tasks(tasks)

# Function to submit moderation results to your website's API
def submit_moderation_results(task_results):
    headers = {'Content-Type': 'application/json'}
    for result in task_results:
        payload = {
            'content_id': result['info']['content_id'],
            'moderation_result': result['info']['moderation']
        }
        response = requests.post(f'{PROJECTHUMANCITY_API_ENDPOINT}/submit_moderation', headers=headers, data=json.dumps(payload))
        if response.status_code != 200:
            print(f"Failed to submit result for content ID {result['info']['content_id']}")

# Fetch content to moderate
content_to_moderate = fetch_content_for_moderation()

# Create tasks in PYBossa
create_pybossa_tasks(content_to_moderate)

# Periodically fetch task results from PYBossa
task_results = pybossa.get_task_runs(project_id=1)

# Submit moderation results back to your website's API
submit_moderation_results(task_results)
