from crewai import Crew, Process
from agents_tasks import gmailTasks, gmailAgents
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

class gmailCrew:
    
    def run(self):
        agents = gmailAgents()
        tasks = gmailTasks()
    
        fetching_agent = agents.fetching_agent()
        importance_decider_agent = agents.importance_decider_agent()
        summary_writer_agent = agents.summary_writer_agent()
        
        fetching_task = tasks.fetching_task(
            fetching_agent,
        )
        
        deciding_task = tasks.deciding_task(
            importance_decider_agent,
        )
        
        summarizing_task = tasks.summarizing_task(
            summary_writer_agent,
        )
        
        
        crew = Crew(
            agents=[
                fetching_agent, importance_decider_agent, summary_writer_agent
            ],
            tasks=[
                fetching_task, deciding_task, summarizing_task
            ],
            verbose=True,
            process=Process.sequential,
        )
        
        print("=== Starting Crew Kickoff ===")
        print(f"Fetching Task Input: argument = 'in:inbox'")
        
        result = crew.kickoff(inputs={'argument': 'in:inbox'})
        print("=== Crew Kickoff Complete ===")
        return result
    
if __name__ == "__main__":
    gmail_crew = gmailCrew()
    result = gmail_crew.run()
    
    print(result)
    
    
