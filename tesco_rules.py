def validate_creative(text):
    if len(text) > 200:
        return 'Text exceeds Tesco limits'
    return 'Tesco Guideline Compliant'
