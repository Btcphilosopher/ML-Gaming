# Grand Strategy AI Event Generation Engine

class Event:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class EventGenerator:
    def __init__(self):
        self.events = []

    def create_event(self, name, description):
        event = Event(name, description)
        self.events.append(event)
        return event

    def generate_random_event(self):
        import random
        event = random.choice(self.events)
        return event

    def list_events(self):
        return [(event.name, event.description) for event in self.events]

# Example usage
if __name__ == '__main__':
    generator = EventGenerator()
    generator.create_event('War', 'A major conflict between nations.')
    generator.create_event('Trade Agreement', 'A deal to promote economic exchange.')
    generator.create_event('Natural Disaster', 'A catastrophic event caused by nature.')
    print(generator.list_events())
    random_event = generator.generate_random_event()
    print(f'Random Event: {random_event.name} - {random_event.description}')