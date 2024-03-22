from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.error import Error
    from .....models.registered_model import RegisteredModel

class Registered_modelRequestBuilder(BaseRequestBuilder):
    """
    The REST endpoint/path used to search for a `RegisteredModel` entity.  This path contains a `GET` operation to perform the find task.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new Registered_modelRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/model_registry/v1alpha3/registered_model{?externalId*,name*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[RegisteredModel]:
        """
        Gets the details of a single instance of a `RegisteredModel` that matches search parameters.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RegisteredModel]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.error import Error

        error_mapping: Dict[str, ParsableFactory] = {
            "401": Error,
            "404": Error,
            "500": Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.registered_model import RegisteredModel

        return await self.request_adapter.send_async(request_info, RegisteredModel, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Gets the details of a single instance of a `RegisteredModel` that matches search parameters.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> Registered_modelRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: Registered_modelRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return Registered_modelRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class Registered_modelRequestBuilderGetQueryParameters():
        """
        Gets the details of a single instance of a `RegisteredModel` that matches search parameters.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "external_id":
                return "externalId"
            if original_name == "name":
                return "name"
            return original_name
        
        # External ID of entity to search.
        external_id: Optional[str] = None

        # Name of entity to search.
        name: Optional[str] = None

    

