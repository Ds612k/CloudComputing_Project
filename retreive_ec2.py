import requests

url = "http://169.254.169.254/latest/meta-data/"
response = requests.get(url)
print("Instance metadata categories:")
print(response.text)
instance_id = requests.get(url + "instance-id").text
print(f"Instance ID: {instance_id}")
