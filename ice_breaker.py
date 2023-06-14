from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    print("Hello LangChain!")

    summary_template = """
        given the information {information} about a person from I want to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(
        #linkedin_profile_url="https://www.linkedin.com/in/williamhgates"
        linkedin_profile_url="https://gist.githubusercontent.com/amkaur741/a8366711eae1505a94d351cb47629994/raw/aae2afca46a72178c61a11ccaedf4fdb279fdb3a/williamhgates"
        #linkedin_profile_url="https://gist.githubusercontent.com/amkaur741/dd3db54c7af0e09bb9e5ab51d11bb620/raw/7bedbf2907569736d856936157e99c2fea41cce9/linkedin-profile.json"
        #linkedin_profile_url="https://gist.githubusercontent.com/amkaur741/6c9d60182f22970672d56cb9e0f7e6a6/raw/deeb46a7d479910a56299ae0343b72476bc21d02/amandeep-kaur-b4888b21"
    )
    print(chain.run(information=linkedin_data))
