#!/usr/bin/env python
import sys


from test_crew.crew import ResumeBuilderCrew

def run():
    """
    Run the crew.
    """
    inputs={
        'topic':'Data engineering'
    }
    ResumeBuilderCrew.crew.kickoff(inputs=inputs)
    
    