from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from tools.search_tools import SearchTools

load_dotenv()

llm = ChatOpenAI(
    model="crewai-mistral",
    base_url="http://localhost:11434/v1"
)


class CommunicationAgents:
    """
    A class representing communication agents for the Maydays initiative.

    Attributes:
        None

    Methods:
        linkedin_post_agent: Returns an Agent object for LinkedIn post writing.

    """
    def tech_blog_post_agent(self) -> Agent:
        """
        Returns an Agent object for tech blog post writing.

        Returns:
            Agent: An Agent object with the role, backstory, goal, tools, and other attributes.

        """
        return Agent(
            role="Tech Blog Post Writing Agent",
            backstory=dedent(
                """
                I am a tech blogger with a passion for writing about the latest trends and innovations in the tech industry.
                I have a strong background in technology and a keen interest in exploring new ideas and concepts.
                My writing style is engaging, informative, and accessible to a wide audience.
                I have experience writing for tech blogs, websites, and publications, and I am always looking for new opportunities to share my insights and knowledge with the world.
                """
            ),
            goal=dedent(
                """
                My goal is to write a compelling blog post about the Maydays initiative.
                The Maydays initiative is an exciting challenge where participants take on a new project every day throughout the month of May.
                I can create a blog post that highlights the creativity, innovation, and skill of the participants, and showcases the impact of their daily challenges.
                """
            ),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=llm,
        )
    
    def linkedin_post_agent(self) -> Agent:
        """
        Returns an Agent object for LinkedIn post writing.

        Returns:
            Agent: An Agent object with the role, backstory, goal, tools, and other attributes.

        """
        return Agent(
            role="LinkedIn Post Writing Agent",
            backstory=dedent(
                """
                I am a digital communication expert with over 10 years of experience in the tech industry.
                I have helped numerous tech companies effectively communicate with their employees, customers, and stakeholders.
                From startups to large corporations, I have a comprehensive understanding of the tech industry and its unique communication challenges.
                My personnals skills are Copywriting skills, LinkedIn post strategies, Engagement analytics, Content scheduling tools
                """
            ),
            goal=dedent(
                """
                My goal is to promote the Maydays initiative on LinkedIn.
                May Days is an ambitious initiative where participants undertake the challenge of executing a new project each day throughout the month of May.
                This initiative aims to showcase creativity, skill, and versatility in tackling diverse challenges within a tight timeframe.
                I can craft compelling LinkedIn posts to attract participants, share project updates, and highlight the impact of daily challenges.
                """
            ),
            tools=[],
            allow_delegation=False,
            verbose=True,
            llm=llm,
        )
