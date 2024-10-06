from bs4 import BeautifulSoup
import requests
from Course import Course
import ipdb


class Scraper:

    def __init__(self):
        self.courses = []

    def get_page(self):
        url = 'http://learn-co-curriculum.github.io/site-for-scraping/courses'

        try:
            response = requests.get(url)
            response.raise_for_status(
            )  # Raises an exception for 4xx/5xx status codes
        except requests.RequestException as e:
            raise

        return BeautifulSoup(response.text, 'html.parser')

    def get_courses(self):
        return self.get_page().find_all('article', class_='post')

    def make_courses(self):
        for course_element in self.get_courses():
            # Scraping the title, date and description with a single find call
            title_element = course_element.find('h2')
            schedule_element = course_element.find('em', class_='date')
            description_element = course_element.find('p')

            title = title_element.get_text() if title_element else ''
            schedule = schedule_element.get_text() if schedule_element else ''
            description = description_element.get_text(
            ) if description_element else ''

            new_course = Course(title, schedule, description)
            self.courses.append(new_course)
        return self.courses

    def print_courses(self):
        for course in self.make_courses():
            print(course)


if __name__ == '__main__':
    # Initialize the scrapper and fetch the course
    scraper = Scraper()

    # Actiate debugging
    ipdb.set_trace()
