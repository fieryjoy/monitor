import requests


def get_result(url):
    response = requests.get(url)

    return {
        'status_code': response.status_code,
        'reason': response.reason,
        'response_time': response.elapsed.total_seconds(),
        }
