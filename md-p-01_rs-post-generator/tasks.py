from crewai import Task
from textwrap import dedent


class CopyWrittingTask:
    def __tip_section(self):
        return dedent(
            """If you do your BEST WORK, I'll give you a $10,000 commission!
            """
        )

    def create_linkedin_post(self, agent, name, description, technology) -> Task:
        return Task(
            title="Write a linkedin post",
            description=dedent(
                f"""
                **Task**: Create a LinkedIn post for the Maydays initiative project {name}.
                **Description**: Share the innovative use of {technology} in the {name} project. 
                Describe how this project addresses real-world challenges and leverages {technology} to deliver impactful solutions.
                Highlight the unique features of the project and using {description}.
            
                **Note**:{self.__tip_section()}
                """
            ),
            agent=agent,
        )
    
    def search_tech_info(self, agent, technology) -> Task:
        return Task(
            title="Search for tech information",
            description=dedent(
                f"""
                **Task**: Search for information about {technology} for the tech blog post.
                **Description**: Use the search tool to find the latest trends and innovations in {technology}.
                Gather relevant information, statistics, and examples to include in the tech blog post.
            
                **Note**:{self.__tip_section()}
                """
            ),
            agent=agent,
        )
