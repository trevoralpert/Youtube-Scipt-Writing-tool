from langchain_openai import ChatOpenAI  # Updated import for LangChain >=0.0.10
from langchain.prompts import PromptTemplate
from serpapi import GoogleSearch

# Helper to extract content from LangChain invoke result
def extract_content(result):
    if isinstance(result, dict) and "content" in result:
        return result["content"]
    elif hasattr(result, "content"):
        return result.content
    else:
        return str(result)

# Function to perform a Google search using SerpAPI
def serpapi_search(query, serp_api_key):
    params = {
        "engine": "google",
        "q": query,
        "api_key": serp_api_key
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    # Extract relevant snippets from results
    snippets = []
    for result in results.get("organic_results", []):
        if "snippet" in result:
            snippets.append(result["snippet"])
    return "\n".join(snippets) if snippets else "No search results found."

# Function to generate video script
def generate_script(prompt, video_length, creativity, openai_api_key, serp_api_key):
    # Template for generating 'Title'
    title_template = PromptTemplate(
        input_variables=['subject'],
        template='Please come up with a title for a YouTube video on the {subject}.'
    )

    # Template for generating 'Video Script' using search engine
    script_template = PromptTemplate(
        input_variables=['title', 'Search_Snippets', 'duration'],
        template=(
            'Create a script for a YouTube video based on this title. '
            'TITLE: {title} of duration {duration} minutes using this search data: {Search_Snippets}'
        )
    )

    # Setting up OpenAI LLM
    llm = ChatOpenAI(temperature=creativity, openai_api_key=openai_api_key, model_name='gpt-3.5-turbo')

    # RunnableSequences for 'Title' & 'Video Script'
    title_chain = title_template | llm
    script_chain = script_template | llm

    # Generate Title
    title = title_chain.invoke({"subject": prompt})
    title_text = extract_content(title)

    # Use SerpAPI for search
    try:
        search_result = serpapi_search(prompt, serp_api_key)
    except Exception as e:
        raise Exception(f"SerpAPI error: {e}")

    script = script_chain.invoke({"title": title_text, "Search_Snippets": search_result, "duration": video_length})
    script_text = extract_content(script)

    return search_result, title_text, script_text
