import requests
from django.conf import settings
from six import BytesIO


def convert_to_excel_file(csv_content, goodgrids_api_url):
    """
    Converts a CSV file into an Excel file
    :param csv_content: a string containing the contents of a CSV file
    :param goodgrids_api_url: the GoodGrids API URL for the Excel export configuration to use
    :return: an Excel file, as bytes
    """
    verify_ssl = True
    if settings.DEBUG or getattr(settings, 'TEST', False):
        verify_ssl = False

    response = requests.post(
        url=goodgrids_api_url,
        files={
            'file': BytesIO(csv_content),
        },
        verify=verify_ssl,
    )

    if response.status_code != 200:
        raise RuntimeError('Could not create Excel file from CSV file')

    return response.content

