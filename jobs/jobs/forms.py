from django import forms
import requests

class JobForm(forms.Form):
    description = forms.CharField(max_length=100)
    location = forms.CharField(max_length=100)

    # def search(self):
    #     result = {}
    #     description = self.cleaned_data['description']
    #     location = self.cleaned_data['location']
    #     endpoint = 'https://jobs.github.com/positions.json?{description}&{location}'
    #     url = endpoint.format(description=description, location=location)
    #     # headers = {'app_id': settings.OXFORD_APP_ID, 'app_key': settings.OXFORD_APP_KEY}
    #     response = requests.get(url, headers={"Accept":"application/json"})
    #     # if response.status_code == 200:  # SUCCESS
    #     result = response.json()
    #         # result['success'] = True
    #     # else:
    #         # result['success'] = False
    #         # if response.status_code == 404:  # NOT FOUND
    #             # result['message'] = 'No entry found for "
    #         # else:
    #         #     result['message'] = 'The Oxford API is not available at the moment. Please try again later.'
    #     return result
