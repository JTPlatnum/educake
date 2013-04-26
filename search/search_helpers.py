STATES = ('State', 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY')
INSIGNIFICANT_WORDS = "a an the in for and with at school or on as".split()

def get_keywords(query = ""):
    """
    Take a search string and return an array of significant words
    """
    if query:
        keywords = query.split()
        for word in keywords:
            if word in INSIGNIFICANT_WORDS:
                keywords.remove(word)
        return keywords
    else:    
        return ""
            
    
    
    