from google.cloud import language
client = language.Client()

def get_document(text_content):
    document = client.document_from_text(text_content)
    return document

def get_entities(text_content):
    document = get_document(text_content)
    entity_response = document.analyze_entities()
    response = []
    for entity in entity_response.entities:
        response.append({ "name": entity.name, "type": entity.entity_type,
                            "metadata": entity.metadata, "salience": entity.salience })
    return response

def get_sentiment(text_content):
    document = get_document(text_content)
    return document.analyze_sentiment()

def main():
    pass

if __name__ == '__main__':
    main()
