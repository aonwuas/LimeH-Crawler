import json
import re


def jsonize(string_input):
	json_text = re.sub(r"'", '"', string_input)
        return json.loads(json_text)



