# import requests

# def get_windows_version_info(api_key):
#     url = "https://api.health.microsoft.com/api/v1/windows"
#     headers = {"Ocp-Apim-Subscription-Key": api_key}

#     try:
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()  # Raise an exception for bad status codes
#         data = response.json()
#         return data
#     except requests.exceptions.RequestException as e:
#         print("Error fetching Windows version information:", e)
#         return None

# def main():
#     api_key = "010281b3-d5d6-4bc8-b561-bf4794b97036"  # Replace with your actual API key
#     windows_info = get_windows_version_info(api_key)
    
#     if windows_info:
#         print("Windows Version Information:")
#         print("------------------------------")
#         for release in windows_info['releases']:
#             print("Release Name:", release['releaseName'])
#             print("Version:", release['version'])
#             print("Build:", release['build'])
#             print("End of Support Date:", release['endOfSupportDate'])
#             print("------------------------------")

# if __name__ == "__main__":
#     main()


import requests

def get_access_token(tenant_id, client_id, client_secret):
    token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"
    # data = {
    #     'grant_type': 'client_credentials',
    #     'client_id': client_id,
    #     'client_secret': client_secret,
    #     'resource': 'https://management.azure.com/'
    # }

    response = requests.post(token_url)
    print(response)
    token = response.json().get('access_token')
    return token

def get_api_key(tenant_id, client_id, client_secret):
    access_token = get_access_token(tenant_id, client_id, client_secret)
    print(access_token)
    # if access_token:
    #     headers = {
    #         'Authorization': 'Bearer ' + access_token
    #     }
    #     key_url = "https://management.azure.com/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.KeyVault/vaults/{key_vault}/secrets/{secret}?api-version=2016-10-01"
    #     response = requests.get(key_url, headers=headers)
    #     api_key = response.json().get('value')
    #     return api_key
    # else:
    #     return None

def main():
    tenant_id = '010281b3-d5d6-4bc8-b561-bf4794b97036'
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'

    api_key = get_api_key(tenant_id, client_id, client_secret)
    if api_key:
        print("Your API key:", api_key)
    else:
        print("Failed to retrieve API key.")

if __name__ == "__main__":
    main()