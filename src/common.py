import re
#write a function  that takes a sentence and returns a hyfenated sentace removing the spaces and all punctiations
def hyphenate_sentence(sentence: str) -> str:
    #remove all punctuations
    sentence = re.sub(r'[^\w\s]', '', sentence)
    return "-".join(sentence.split())



def remove_null_values(model_dict: dict) -> dict:
    cleaned_dict = {}
    for key, value in model_dict.items():
        if value is not None:
            if isinstance(value, dict):
                nested_result = remove_null_values(value)
                if nested_result:  # Only add if nested dict isn't empty
                    cleaned_dict[key] = nested_result
            else:
                cleaned_dict[key] = value
    return cleaned_dict



