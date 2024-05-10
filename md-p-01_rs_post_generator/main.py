import os
from crewai import Crew

from textwrap import dedent
from agents import CommunicationAgents
from tasks import CopyWrittingTask

class CopyWrittingCrew:
    def __init__(self, name, description, technology):
        self.name = name
        self.description = description
        self.technology = technology

    def run(self):
        agents = CommunicationAgents()
        tasks = CopyWrittingTask()

        # Create a Crew
        crew = Crew(
            agents=[
                agents.linkedin_post_agent(),
                agents.tech_blog_post_agent()
            ],
            tasks=[
                tasks.search_tech_info(agents.tech_blog_post_agent(), self.technology),
                tasks.create_linkedin_post(agents.linkedin_post_agent(), self.name, self.description, self.technology)
            ],
            verbose=True
        )
        result = crew.kickoff()
        return result


if __name__ == '__main__':
    print("Welcome to the May Day's communication Crew!")
    name = input("Enter the name of the project : ")
    description = input("Enter the description of the project :")
    technology = input("Enter the technology used in the project :")

    crew = CopyWrittingCrew(name, description, technology)
    result = crew.run()
