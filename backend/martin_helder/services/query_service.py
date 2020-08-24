"""
Service layer for query related operations
"""

from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector, TrigramSimilarity


class QueryService:
    """
    Service class for query related operations
    """

    @staticmethod
    def get_query_results(query_set, query, search_structure):
        """
        Returns the list of relevant results for the searched query

        :param query_set: QuerySet of the data to be searched
        :param query: Query with keywords to be used in search
        :param search_structure: List of fields to search on and respective weight
        :return: list of models order by relevance for the search
        """

        if query:
            search_vector = QueryService.build_search_vector(search_structure)
            term_query = SearchQuery(query)
            results = query_set.annotate(rank=SearchRank(search_vector, term_query)).filter(
                rank__gte=0.1).order_by('-rank')
        else:
            results = query_set.all()

        return results

    @staticmethod
    def build_search_vector(search_structure):
        """
        Builds the search vector to be used in a search from the list of fields and respective weights

        :param search_structure: List of fields to search on and respective weight
        :return: Search vector to be used on a search
        """

        if search_structure:
            iterator = iter(search_structure)
            field = next(iterator)
            search_vector = SearchVector(field, weight=search_structure[field])

            try:
                while True:
                    field = next(iterator)
                    search_vector += SearchVector(field, weight=search_structure[field])
            except StopIteration:
                return search_vector

        return None

    @staticmethod
    def get_trigram_similarity_results(model, query):
        """
        Search using similarity

        :param model: Model of the data to be searched
        :param query: Query with keywords to be used in search
        """

        if query:
            results = model.objects.annotate(similarity=TrigramSimilarity('name', query)).filter(
                similarity__gt=0.1).order_by('-similarity')
        else:
            results = model.objects.all()

        return results
