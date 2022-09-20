

class ExerciseSession:
    class_name = "yoga"
    all_ainstances=[]
    def __init__(self, exercise_name, exercise_intensity, duration_in_min):
        self.__name = exercise_name
        self.__intensity = exercise_intensity
        self.__duration = duration_in_min
        ExerciseSession.all_ainstances.append(self)
    def get_exercise(self):
        print("exercise __name accessed, it is" , self.__name )
        return self.__name

    def get_intensity(self):
        print("exercise __intensity accessed, it is" , self.__intensity )
        return self.__intensity

    def get_duration(self):
        print("exercise __duration accessed, it is" , self.__duration )
        return self.__duration

    def set_exercise(self, new_name):
        print("exercise __name modified from " , self.__name , "to" , new_name )
        self.__name = new_name

    def set_intensity(self, new_intensity):
        print("__intensity modified from " , self.__intensity , "to" , new_intensity )
        self.__intensity = new_intensity

    def set_duration(self, new_duration):
        print("__intensity modified from " , self.__duration , "to" , new_duration )
        self.__duration = new_duration

    def calories_burned(self):
        if self.__intensity == "Low":
            return 4 * self.__duration
        elif self.__intensity == "Medium":
            return 8 * self.__duration
        elif self.__intensity == "High":
            return 12 * self.__duration
        else:
            return None

    def __repr__(self):
        s = f"exercise {self.__name} with id {(id(self))}"
        return s

if __name__ == "__main__":
    new_exercise = ExerciseSession("Running", "Low", 60)
    print(new_exercise.calories_burned())
    new_exercise.set_exercise("Swimming")
    new_exercise.set_intensity("High")
    new_exercise.set_duration(30)
    print(new_exercise.calories_burned())
    print(ExerciseSession.all_ainstances)
    print(ExerciseSession.__dict__) # get all class attributes
    print(new_exercise.__dict__) #get all instance attributes