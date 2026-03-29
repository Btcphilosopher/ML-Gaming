# Integration Example

## Integration Patterns

1. **Event-Driven Architecture**: This pattern empowers systems to communicate via events, making them highly decoupled.
   - Example in Python:
     ```python
     import time
     import random
     
def event_listener():
         while True:
             event = random.choice(['event1', 'event2'])
             print(f"Listening for {event}")
             time.sleep(2)
     
event_listener()
     ```

2. **Microservices Architecture**: In this pattern, applications are broken down into smaller services that communicate over a network.

3. **Service-Oriented Architecture (SOA)**: SOA involves integrating various services to work together towards a common goal.

## REST API Examples

### Example 1: GET Request

Fetching user data from a placeholder API.

```python
import requests

response = requests.get('https://jsonplaceholder.typicode.com/users/1')
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
```

### Example 2: POST Request

Creating a new user in a placeholder API.

```python
import requests

new_user = {
    'name': 'John Doe',
    'email': 'john.doe@example.com'
}
response = requests.post('https://jsonplaceholder.typicode.com/users', json=new_user)
if response.status_code == 201:
    print('User created successfully!')
else:
    print(f"Error: {response.status_code}")
```