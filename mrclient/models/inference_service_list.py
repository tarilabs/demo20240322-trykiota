from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_resource_list import BaseResourceList
    from .inference_service import InferenceService

from .base_resource_list import BaseResourceList

@dataclass
class InferenceServiceList(BaseResourceList):
    """
    List of InferenceServices.
    """
    # The items property
    items: Optional[List[InferenceService]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InferenceServiceList:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InferenceServiceList
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return InferenceServiceList()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .base_resource_list import BaseResourceList
        from .inference_service import InferenceService

        from .base_resource_list import BaseResourceList
        from .inference_service import InferenceService

        fields: Dict[str, Callable[[Any], None]] = {
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(InferenceService)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("items", self.items)
    

