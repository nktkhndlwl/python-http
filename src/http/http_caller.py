from requests import sessions
from requests.models import Response
from requests.sessions import Session


def call(method: str, url: str, data: dict, headers: dict, retries: int = 10) -> Response:
	global response
	session: Session = sessions.Session()
	retry_count: int = 0
	status_code: int = 0
	while status_code != 200 and retry_count < retries:
		response: Response = session.request(method, url, data, headers)
		status_code = response.status_code
		retry_count += 1

	return response
