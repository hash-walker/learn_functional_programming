def new_collection(initial_docs):
    closed_over = initial_docs.copy()
    def new_collection_doc(doc):
        closed_over.append(doc)
        return closed_over
    
    return new_collection_doc