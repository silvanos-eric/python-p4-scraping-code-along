class Course:
    """
    A class that represents a course, with a title, schedule and description.

    Attributes:
        title (str): The title of the course.
        schedule (str): The schedule of the course.
        description (str): The description of the course.

    Methods:
        __str__: Returns a string representation of the course.
        __repr__: Returns a string that represents the course as an instance of the class.
    """

    def __init__(self, title: str, schedule: str, description: str) -> None:
        """
        Initializes a new Course with the given title, schedule and description.

        Parameters:
            title (str): The title of the course.
            schedule (str): The schedule of the course.
            description (str): The description of the course.
        """
        self.title = title
        self.schedule = schedule
        self.description = description

    def __str__(self) -> str:
        """
        Returns a string representation of the course.

        Returns:
            str: The string representation of the course.
        """
        output = ''
        output += f'Title: {self.title}\nSchedule: {self.schedule}\nDescription: {self.description}'
        output += '\n------------------'
        return output

    def __repr__(self) -> str:
        """
        Returns a string that represents the course as an instance of the class.

        Returns:
            str: The string representation of the course as an instance of the class.
        """
        return f'Course("{self.title}", "{self.schedule}", "{self.description}")'
