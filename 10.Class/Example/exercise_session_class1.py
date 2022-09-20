

class ExerciseSession:
    def __init__(self, exercise_name, exercise_intensity, duration_in_min):
        self.name = exercise_name
        self.intensity = exercise_intensity
        self.duration = duration_in_min

    def get_exercise(self):
        print("exercise name accessed, it is", self.name)
        return self.name

    def get_intensity(self):
        print("exercise intensity accessed, it is", self.intensity)
        return self.intensity

    def get_duration(self):
        print("exercise duration accessed, it is", self.duration)
        return self.duration

    def set_exercise(self, new_name):
        print("exercise name modified from ", self.name, "to", new_name)
        self.name = new_name

    def set_intensity(self, new_intensity):
        print("intensity modified from ", self.intensity, "to", new_intensity)
        self.intensity = new_intensity

    def set_duration(self, new_duration):
        print("intensity modified from ", self.duration, "to", new_duration)
        self.duration = new_duration


if __name__ == "__main__":
    new_exercise = ExerciseSession("Running", "Low", 60)
    print(new_exercise.get_exercise())
    print(new_exercise.get_intensity())
    print(new_exercise.get_duration())
    new_exercise.set_exercise("Swimming")
    new_exercise.set_intensity("High")
    new_exercise.set_duration(30)
    print(new_exercise.get_exercise())
    print(new_exercise.get_intensity())
    print(new_exercise.get_duration())
