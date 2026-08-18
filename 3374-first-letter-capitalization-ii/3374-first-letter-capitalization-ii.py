import pandas as pd
import re

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    def cap_word(m):
        word = m.group(0)
        if re.fullmatch(r'[a-z]+(-[a-z]+)+', word):
            return '-'.join(part[0].upper() + part[1:] for part in word.split('-'))
        else:
            if word[0].isalpha():
                return word[0].upper() + word[1:]
            return word

    def transform(text):
        text = text.lower()
        return re.sub(r'\S+', cap_word, text)

    result = user_content.copy()
    result['converted_text'] = result['content_text'].apply(transform)
    result = result.rename(columns={'content_text': 'original_text'})

    return result[['content_id', 'original_text', 'converted_text']]