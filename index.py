class ObstructionChecker:
    def __init__(self, speed_of_machine):
        self.speed_of_machine = speed_of_machine

    def calculate_expected_time(self, distance):
        expected_time = distance / self.speed_of_machine * 60
        return expected_time

    def check_obstruction(self, distance, expected_time, actual_time):
        time_difference = actual_time - expected_time
        if time_difference > 60:
            return True  # Impenetrable obstruction
        return False  # No obstruction


if __name__ == "__main__":
    obstruction_checker = ObstructionChecker(speed_of_machine=50)
    distance_ab = 100  # miles
    actual_time_taken = 150  # minutes

    expected_time_ab = obstruction_checker.calculate_expected_time(distance_ab)
    
    is_obstruction = obstruction_checker.check_obstruction(distance_ab, expected_time_ab, actual_time_taken)

    if is_obstruction:
        print("There is an impenetrable obstruction between points a and b.")
    else:
        print("No obstruction between points a and b.")
