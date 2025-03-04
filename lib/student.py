# Define the Student class (superclass)
class Student:
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")
    
    def raise_hand(self):
        print("Pick me!")

# Define the ChattyStudent class (subclass) that inherits from Student
class ChattyStudent(Student):
    def hello(self):
        # Call the hello() method from the superclass (Student)
        super().hello()
        # Add more chatty behavior
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")

    def raise_hand(self):
        # Call the raise_hand() method from the superclass multiple times using super()
        for _ in range(10):
            super().raise_hand()
