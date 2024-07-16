from crewai import Agent, Task
from langchain_openai import ChatOpenAI
from tools.gmailScraper import GmailFetchTool

"""
Defines all of the agents necessary as well as their tasks
"""

class gmailAgents:
    
    # AGENT DECLARATION
    
    # Agent that fetches the Gmails
    def fetching_agent(self):
        
        gmail_tool = GmailFetchTool()
        
        llmturbo = ChatOpenAI(
            model = 'gpt-4o'
        )
        
        return Agent(
            role="Email Fetcher",
            goal=(
                "Fetch emails from the user\'s Gmail account and pass them on to the importance_decider_agent"
            ),
            backstory=(
                "You are a diligent season email fetcher, responsible for finding all the necessary emails from the User\'s account in the most efficiant way possible"
            ),
            llm = llmturbo,
            allow_delegation = False,
            memory = False,
            tools = [gmail_tool],
        )
    
    # Agent that decides what emails are important and which ones should be ignored
    def importance_decider_agent(self):
    
        llm4o = ChatOpenAI(
            model = 'gpt-4o'
        )
    
        return Agent(
            role="Email Importance Decider",
            goal=(
                "You take in all the emails given to you by the fetching_agent and you decide whether or not the email should be sent over to the summarizer or not"
            ),
            backstory=(
                "You are a proffessional email analyzer and have a keen eye for noticing important information. You have years of experience behind your belt and have an "
                "extremely good grasp on what would be important for the user and what would be considered spam that the user would overlook on their own"
            ),
            llm = llm4o,
            allow_delegation = False,
            memory = False,
            tools = [],
        )
    
    # Agent that takes the emails and summarizes them 
    # Returns the summary in a txt file
    def summary_writer_agent(self):
        llm4o = ChatOpenAI(
            model = 'gpt-4o'
        )
    
        return Agent(
            role="Detailed Email Summary Writer",
            goal=(
                "Your task is to create comprehensive, detailed summaries of important emails. These summaries should be extensive, capturing all relevant information and nuances "
                "from the original emails. You must provide a thorough breakdown of each email's content, ensuring no potentially useful information is omitted."
            ),
            backstory=(
                "You are an expert writer with a specialization in creating detailed, long-form summaries. Your background includes years of experience in journalism, technical writing, "
                "and data analysis. You have a keen eye for detail and the ability to distill complex information into clear, organized, and comprehensive reports. Your summaries are known "
                "for their thoroughness, clarity, and ability to capture even subtle nuances of the original content."
            ),
            llm = llm4o,
            allow_delegation = False,
            memory = False,
            tools = [],
        )
    
class gmailTasks:
      
    # TASK DECLARATION
    
    # Task for fetching the emails
    def fetching_task(self, agent):    
        return Task(
            description=(
                'Fetch emails from the user\'s gmail account using the query "in:inbox" '
            ),
            expected_output=(
                "A comprehensive clear list of fetched emails for the importance_decider_agent"
            ),
            agent = agent,
        )
    
    # Task for deciding the importance of the email
    def deciding_task(self, agent):
        return Task(
            description=(
                'Analyze all the fetched emails and determine which ones are important based on certain keywords and critera such as "urgent", "important", and "asap", as well as '
                'emails from specific senders and those containing attachtments that could be userful for the user'
                
                "If no emails are determined to be important, make sure to at least summarize all of them for the user regardless"
            ),
            expected_output=(
                "A list of all the emails deemed important"
                "If none are important, summarize all"
            ),
            agent = agent,
        )
    
    # Task for summarizing the task
    # Outputting the file as a txt file
    def summarizing_task(self, agent):  
        return Task(
            description=(
                "Create extensive, detailed summaries of the important emails identified by the importance_decider_agent. Your summaries should be comprehensive and much longer than a typical "
                "brief summary. For each email, include:\n"
                "1. Subject line (in full)\n"
                "2. Sender's full name and email address\n"
                "3. Date and time received\n"
                "4. Detailed breakdown of the email's content, including:\n"
                "   - Main points (with context and explanation)\n"
                "   - Secondary points\n"
                "   - Any background information provided\n"
                "   - Specific details, numbers, or data mentioned\n"
                "5. Any attachments or links (with descriptions if available)\n"
                "6. Action items or requests, clearly highlighted\n"
                "7. Deadlines or important dates mentioned\n"
                "8. Tone and urgency of the message\n"
                "9. Any potential implications or follow-up actions required\n"
                "10. Your analysis of the email's importance and why it was flagged\n\n"
                "Format each email summary with clear headings, bullet points where appropriate, and ensure readability despite the increased length. "
                "The goal is to provide the user with a comprehensive understanding of each important email without needing to refer back to the original."
            ),
            expected_output=(
                "A detailed, extensive summary of each important email in a well-formatted text file. Each summary should be significantly longer than a brief overview, "
                "providing in-depth information and analysis. The file should clearly separate different email summaries and use formatting to enhance readability and quick reference. "
                "Ensure that the user can easily identify which summary corresponds to which email, including clear indicators of the email's origin, timing, and importance."
            ),
            agent = agent,
            output_file = 'Detailed_Important_Email_Summaries.txt'
        )
    
    
    
    
    
    
