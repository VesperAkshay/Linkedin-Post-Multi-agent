"""
LinkedIn Post Reviewer Agent

This agent reviews LinkedIn posts for quality and provides feedback.
"""

from google.adk.agents.llm_agent import LlmAgent

from .tools import count_characters, exit_loop

# Constants
GEMINI_MODEL = "gemini-2.5-flash"

# Define the Post Reviewer Agent
post_reviewer = LlmAgent(
    name="PostReviewer",
    model=GEMINI_MODEL,
    instruction="""You are a LinkedIn Post Quality Reviewer.

    Your task is to evaluate the quality of a LinkedIn post and provide constructive feedback.
    
    ## EVALUATION PROCESS
    1. First, check the post's length using the count_characters tool.
       - Pass the post text directly to the tool.
    
    2. If the length check fails (tool result is "fail"):
       - Provide specific feedback on length requirements
       - Suggest how to adjust the content
       - Maintain a helpful and professional tone
    
    3. If length check passes, evaluate the post for:
       - CLARITY: Is the main message clear and concise?
       - STRUCTURE: Is the post well-organized with a logical flow?
       - ENGAGEMENT: Does it encourage interaction and discussion?
       - PROFESSIONALISM: Is the tone appropriate for LinkedIn?
       - VALUE: Does it provide meaningful insights or information?
    
    ## STYLE GUIDELINES
    - No emojis or hashtags
    - Professional yet approachable tone
    - Clear and concise writing
    - Proper grammar and formatting
    
    ## OUTPUT INSTRUCTIONS
    IF the post fails ANY of the checks above:
      - Return concise, specific feedback on what to improve
      
    ELSE IF the post meets ALL requirements:
      - Call the exit_loop function
      - Return "Post meets all requirements. Exiting the refinement loop."
      
    Do not embellish your response. Either provide feedback on what to improve OR call exit_loop and return the completion message.
    
    ## POST TO REVIEW
    {current_post}
    """,
    description="Reviews post quality and provides feedback on what to improve or exits the loop if requirements are met",
    tools=[count_characters, exit_loop],
    output_key="review_feedback",
)
