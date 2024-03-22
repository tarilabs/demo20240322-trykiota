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
    from .....models.inference_service import InferenceService
    from .....models.inference_service_create import InferenceServiceCreate
    from .....models.inference_service_list import InferenceServiceList
    from .....models.order_by_field import OrderByField
    from .....models.sort_order import SortOrder
    from .item.with_inferenceservice_item_request_builder import WithInferenceserviceItemRequestBuilder

class Inference_servicesRequestBuilder(BaseRequestBuilder):
    """
    The REST endpoint/path used to list and create zero or more `InferenceService` entities.  This path contains a `GET` and `POST` operation to perform the list and create tasks, respectively.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new Inference_servicesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/model_registry/v1alpha3/inference_services{?nextPageToken*,orderBy*,pageSize*,sortOrder*}", path_parameters)
    
    def by_inferenceservice_id(self,inferenceservice_id: str) -> WithInferenceserviceItemRequestBuilder:
        """
        The REST endpoint/path used to get, update, and delete single instances of an `InferenceService`. This path contains `GET`, `PUT`, and `DELETE` operations used to perform the get, update, and delete tasks, respectively.
        param inferenceservice_id: A unique identifier for a `InferenceService`.
        Returns: WithInferenceserviceItemRequestBuilder
        """
        if not inferenceservice_id:
            raise TypeError("inferenceservice_id cannot be null.")
        from .item.with_inferenceservice_item_request_builder import WithInferenceserviceItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["inferenceserviceId"] = inferenceservice_id
        return WithInferenceserviceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[InferenceServiceList]:
        """
        Gets a list of all `InferenceService` entities.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[InferenceServiceList]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.error import Error

        error_mapping: Dict[str, ParsableFactory] = {
            "400": Error,
            "401": Error,
            "404": Error,
            "500": Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.inference_service_list import InferenceServiceList

        return await self.request_adapter.send_async(request_info, InferenceServiceList, error_mapping)
    
    async def post(self,body: Optional[InferenceServiceCreate] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[InferenceService]:
        """
        Creates a new instance of a `InferenceService`.
        param body: An `InferenceService` entity in a `ServingEnvironment` represents a deployed `ModelVersion` from a `RegisteredModel` created by Model Serving.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[InferenceService]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.error import Error

        error_mapping: Dict[str, ParsableFactory] = {
            "400": Error,
            "401": Error,
            "500": Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.inference_service import InferenceService

        return await self.request_adapter.send_async(request_info, InferenceService, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Gets a list of all `InferenceService` entities.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: Optional[InferenceServiceCreate] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Creates a new instance of a `InferenceService`.
        param body: An `InferenceService` entity in a `ServingEnvironment` represents a deployed `ModelVersion` from a `RegisteredModel` created by Model Serving.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, '{+baseurl}/api/model_registry/v1alpha3/inference_services', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> Inference_servicesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: Inference_servicesRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return Inference_servicesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class Inference_servicesRequestBuilderGetQueryParameters():
        """
        Gets a list of all `InferenceService` entities.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "next_page_token":
                return "nextPageToken"
            if original_name == "order_by":
                return "orderBy"
            if original_name == "page_size":
                return "pageSize"
            if original_name == "sort_order":
                return "sortOrder"
            return original_name
        
        # Token to use to retrieve next page of results.
        next_page_token: Optional[str] = None

        # Specifies the order by criteria for listing entities.
        order_by: Optional[OrderByField] = None

        # Number of entities in each page.
        page_size: Optional[str] = None

        # Specifies the sort order for listing entities, defaults to ASC.
        sort_order: Optional[SortOrder] = None

    

