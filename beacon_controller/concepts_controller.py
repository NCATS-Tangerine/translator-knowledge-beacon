from swagger_server.models.beacon_concept import BeaconConcept  # noqa: E501
from swagger_server.models.beacon_concept_with_details import BeaconConceptWithDetails  # noqa: E501
from swagger_server.models.exact_match_response import ExactMatchResponse  # noqa: E501

from beacon_controller import biolink_model as blm

def get_concept_details(concept_id):  # noqa: E501
    """get_concept_details

    Retrieves details for a specified concepts in the system, as specified by a (url-encoded) CURIE identifier of a concept known the given knowledge source.  # noqa: E501

    :param concept_id: (url-encoded) CURIE identifier of concept of interest
    :type concept_id: str

    :rtype: BeaconConceptWithDetails
    """
    return 'do some magic!'


def get_concepts(keywords=None, categories=None, offset=None, size=None):  # noqa: E501
    """get_concepts

    Retrieves a list of whose concept in the beacon knowledge base with names and/or synonyms matching a set of keywords or substrings. The results returned should generally be returned in order of the quality of the match, that is, the highest ranked concepts should exactly match the most keywords, in the same order as the keywords were given. Lower quality hits with fewer keyword matches or out-of-order keyword matches, should be returned lower in the list.  # noqa: E501

    :param keywords: (Optional) array of keywords or substrings against which to match concept names and synonyms
    :type keywords: List[str]
    :param categories: (Optional) array set of concept categories - specified as Biolink name labels codes gene, pathway, etc. - to which to constrain concepts matched by the main keyword search (see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of terms)
    :type categories: List[str]
    :param offset: offset (cursor position) to next batch of statements of amount &#39;size&#39; to return.
    :type offset: int
    :param size: maximum number of concept entries requested by the client; if this argument is omitted, then the query is expected to returned all the available data for the query
    :type size: int

    :rtype: List[BeaconConcept]
    """
    return 'do some magic!'


def get_exact_matches_to_concept_list(c):  # noqa: E501
    """get_exact_matches_to_concept_list

    Given an input array of [CURIE](https://www.w3.org/TR/curie/) identifiers of known exactly matched concepts [*sensa*-SKOS](http://www.w3.org/2004/02/skos/core#exactMatch), retrieves the list of [CURIE](https://www.w3.org/TR/curie/) identifiers of additional concepts that are deemed by the given knowledge source to be exact matches to one or more of the input concepts **plus** whichever concept identifiers from the input list were specifically matched to these additional concepts, thus giving the whole known set of equivalent concepts known to this particular knowledge source.  If an empty set is returned, the it can be assumed that the given knowledge source does not know of any new equivalent concepts matching the input set. The caller of this endpoint can then decide whether or not to treat  its input identifiers as its own equivalent set.  # noqa: E501

    :param c: an array set of [CURIE-encoded](https://www.w3.org/TR/curie/) identifiers of concepts thought to be exactly matching concepts, to be used in a search for additional exactly matching concepts [*sensa*-SKOS](http://www.w3.org/2004/02/skos/core#exactMatch).
    :type c: List[str]

    :rtype: List[ExactMatchResponse]
    """
    return 'do some magic!'
