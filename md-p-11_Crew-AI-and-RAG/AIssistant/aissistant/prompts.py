from llama_index.core import PromptTemplate

instruction_str = """
    1. Convert the query to executable Python code using Pandas
    2. The final line of code should be a Python expression that can be call with the èval()`function.
    3. The code should represent asolution of the query.
    4. PRINT ONLY THE EXPRESSION.
    5. Do not quote the expression."""

new_prompt = PromptTemplate(
    """
    You are working with a Pandas dataframe in Python.
    The name of the dataframe is `df`.
    This is the resule of `print(airplane_df.head())`:
    {df_str}
    
    Follow these instructions:
    {instruction_str}
    Query: {query_str}
    
    Expression: """
)

context = """Purpose: The primary role of this agent is to assist users by providing accurate information about history plane crashes and fatalities information."""