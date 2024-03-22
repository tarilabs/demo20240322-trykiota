from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .serving_environment_create_custom_properties import ServingEnvironmentCreate_customProperties

@dataclass
class ServingEnvironmentCreate(AdditionalDataHolder, Parsable):
    """
    A Model Serving environment for serving `RegisteredModels`.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # User provided custom properties which are not defined by its type.
    custom_properties: Optional[ServingEnvironmentCreate_customProperties] = None
    # An optional description about the resource.
    description: Optional[str] = None
    # The external id that come from the clients’ system. This field is optional.If set, it must be unique among all resources within a database instance.
    external_id: Optional[str] = None
    # The client provided name of the artifact. This field is optional. If set,it must be unique among all the artifacts of the same artifact type withina database instance and cannot be changed once set.
    name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServingEnvironmentCreate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServingEnvironmentCreate
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ServingEnvironmentCreate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .serving_environment_create_custom_properties import ServingEnvironmentCreate_customProperties

        from .serving_environment_create_custom_properties import ServingEnvironmentCreate_customProperties

        fields: Dict[str, Callable[[Any], None]] = {
            "customProperties": lambda n : setattr(self, 'custom_properties', n.get_object_value(ServingEnvironmentCreate_customProperties)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("customProperties", self.custom_properties)
        writer.write_str_value("description", self.description)
        writer.write_str_value("externalId", self.external_id)
        writer.write_str_value("name", self.name)
        writer.write_additional_data_value(self.additional_data)
    
