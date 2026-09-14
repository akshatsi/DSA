class Solution:
    def carPooling(self, trips, capacity):
        events = []

        for passengers, start, end in trips:
            events.append((start, passengers))
            events.append((end, -passengers))

        events.sort()

        for location, passenger_change in events:
            capacity -= passenger_change

            if capacity < 0:
                return False

        return True