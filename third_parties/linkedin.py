import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )
    #response = requests.get(params={"url": linkedin_profile_url})

    data = response.json()

    print("17------data-----")
    print(data)

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    print("29------data-----")
    print(data)
    return data

#scrape_linkedin_profile('https://gist.githubusercontent.com/amkaur741/dcee1c1a695db47573803d0316d490d2/raw/b9593280ec1fdee66084eb8669214e6dcbe58467/eden-marco-pub')
# import os
#
# import openai
# import requests
#
# openai.api_key = os.getenv("OPENAI_API_KEY")
#
# def scrape_linkedin_profile(linkedin_profile_url: str):
#     """
#     scrape information from LinkedIn profiles,
#     Manually scrape the information from LinkedIn profile
#     """
#     print("linkedin_profile_url-----13------")
#     print(linkedin_profile_url)
#     api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
#     # linkedin_profile_url = 'https://www.linkedin.com/in/williamhgates'
#     header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_APY_KEY")}'}
#
#     response = requests.get(
#         api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
#     )
#     data = response.json()
#     print("22------data-----")
#     print(data)
#     data = {
#         k: v
#         for k, v in data.items()
#         if v not in ([], "", "", None)
#         and k not in ["people_also_viewed", "certifications"]
#     }
#     if data.get("groups"):
#         for group_dict in data.get("groups"):
#             group_dict.pop("profile_pic_url")
#
#     print("linkedIn data: ")
#     print(data)
#     return data



