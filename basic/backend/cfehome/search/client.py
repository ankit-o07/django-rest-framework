from algoliasearch_django import algolia_engine


def get_client():
    return algolia_engine.client

def get_index(index_name='cfe_Product'):
    client = get_client()
    index = client.init_index("cfe_Product")
    return index


def perform_search(query,**kwargs):
    index = get_index()
    params = {}
    tags = ''
    print(kwargs["tags"])
    if ("tags" in kwargs) and (kwargs['tags'] is not None):
        tags = kwargs.pop('tags', '')  
        if len(tags) !=0 :
            params['tagFilters'] = tags
        
    index_filters = [f"{k}:{v}" for k,v in kwargs.items() if v]
    
    # if len(index_filters) !=0:
    #     print(index_filters)
    #     params['facetFilters'] = index_filters
                
        
    results = index.search(query,params)
   
    print("Resutl",results)
    print("\n\n\n\n\n")
    return results