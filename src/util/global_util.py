from typing import List


def get_property_value(name: str) -> str:
	with open("/Users/niketkhandelwal/PycharmProjects/python-http/resources/tokens.properties") as properties_file:
		line: str
		for line in properties_file:
			split_line: List[str] = line.split('=')
			if split_line[0] == name:
				return split_line[1].strip()
	return ""
