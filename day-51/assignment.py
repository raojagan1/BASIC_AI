import re


def rank_documents(query: str, documents: dict[str, str]) -> list[str]:
    terms = set(re.findall(r'[a-z]+', query.lower()))
    return sorted(documents, key=lambda name: len(terms & set(re.findall(r'[a-z]+', documents[name].lower()))), reverse=True)

if __name__ == '__main__':
    result = rank_documents('backup errors', {'a': 'backup errors', 'b': 'weather'})
    assert result[0] == 'a'
    print('PASS: retrieval index ranked the relevant document first')
