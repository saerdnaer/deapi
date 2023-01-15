# Auto generated from dapi.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-01-15T16:36:35
# Schema: de-meta
#
# id: https://codeforde.org/schema/meta
# description: Information about public organisations, their projects, products & service providers based on
#              [schema.org](http://schema.org)
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Date, Float, String
from linkml_runtime.utils.metamodelcore import Bool, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CODE = CurieNamespace('CODE', 'http://example.org/code/')
GEO = CurieNamespace('GEO', 'http://example.org/geoloc/')
P = CurieNamespace('P', 'http://example.org/P/')
ROR = CurieNamespace('ROR', 'http://example.org/ror/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
M = CurieNamespace('m', 'https://codeforde.org/schema/meta')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = M


# Types

# Class references
class PlaceId(extended_str):
    pass


class NamedThingId(extended_str):
    pass


class OrganizationId(NamedThingId):
    pass


class ProjectId(NamedThingId):
    pass


class ProductId(NamedThingId):
    pass


class ConceptId(NamedThingId):
    pass


@dataclass
class Place(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = M.Place
    class_class_curie: ClassVar[str] = "m:Place"
    class_name: ClassVar[str] = "Place"
    class_model_uri: ClassVar[URIRef] = M.Place

    id: Union[str, PlaceId] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlaceId):
            self.id = PlaceId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Address(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.PostalAddress
    class_class_curie: ClassVar[str] = "schema:PostalAddress"
    class_name: ClassVar[str] = "Address"
    class_model_uri: ClassVar[URIRef] = M.Address

    street: Optional[str] = None
    city: Optional[str] = None
    postal_code: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.street is not None and not isinstance(self.street, str):
            self.street = str(self.street)

        if self.city is not None and not isinstance(self.city, str):
            self.city = str(self.city)

        if self.postal_code is not None and not isinstance(self.postal_code, str):
            self.postal_code = str(self.postal_code)

        super().__post_init__(**kwargs)


@dataclass
class Event(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = M.Event
    class_class_curie: ClassVar[str] = "m:Event"
    class_name: ClassVar[str] = "Event"
    class_model_uri: ClassVar[URIRef] = M.Event

    start_date: Optional[Union[str, XSDDate]] = None
    end_date: Optional[Union[str, XSDDate]] = None
    duration: Optional[float] = None
    is_current: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.start_date is not None and not isinstance(self.start_date, XSDDate):
            self.start_date = XSDDate(self.start_date)

        if self.end_date is not None and not isinstance(self.end_date, XSDDate):
            self.end_date = XSDDate(self.end_date)

        if self.duration is not None and not isinstance(self.duration, float):
            self.duration = float(self.duration)

        if self.is_current is not None and not isinstance(self.is_current, Bool):
            self.is_current = Bool(self.is_current)

        super().__post_init__(**kwargs)


@dataclass
class Relationship(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = M.Relationship
    class_class_curie: ClassVar[str] = "m:Relationship"
    class_name: ClassVar[str] = "Relationship"
    class_model_uri: ClassVar[URIRef] = M.Relationship

    start_date: Optional[Union[str, XSDDate]] = None
    end_date: Optional[Union[str, XSDDate]] = None
    related_to: Optional[str] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.start_date is not None and not isinstance(self.start_date, XSDDate):
            self.start_date = XSDDate(self.start_date)

        if self.end_date is not None and not isinstance(self.end_date, XSDDate):
            self.end_date = XSDDate(self.end_date)

        if self.related_to is not None and not isinstance(self.related_to, str):
            self.related_to = str(self.related_to)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass
class WithLocation(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = M.WithLocation
    class_class_curie: ClassVar[str] = "m:WithLocation"
    class_name: ClassVar[str] = "WithLocation"
    class_model_uri: ClassVar[URIRef] = M.WithLocation

    in_location: Optional[Union[str, PlaceId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.in_location is not None and not isinstance(self.in_location, PlaceId):
            self.in_location = PlaceId(self.in_location)

        super().__post_init__(**kwargs)


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = M.NamedThing
    class_class_curie: ClassVar[str] = "m:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = M.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    url: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.image is not None and not isinstance(self.image, str):
            self.image = str(self.image)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        super().__post_init__(**kwargs)


@dataclass
class Organization(NamedThing):
    """
    An organization such as a government, political party, state, municipality, city, NGO, company, university or any
    other association
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Organization
    class_class_curie: ClassVar[str] = "schema:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = M.Organization

    id: Union[str, OrganizationId] = None
    legal_form: Optional[str] = None
    address: Optional[Union[dict, "Address"]] = None
    mission_statement: Optional[str] = None
    founding_date: Optional[str] = None
    founding_location: Optional[Union[str, PlaceId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganizationId):
            self.id = OrganizationId(self.id)

        if self.legal_form is not None and not isinstance(self.legal_form, str):
            self.legal_form = str(self.legal_form)

        if self.address is not None and not isinstance(self.address, Address):
            self.address = Address(**as_dict(self.address))

        if self.mission_statement is not None and not isinstance(self.mission_statement, str):
            self.mission_statement = str(self.mission_statement)

        if self.founding_date is not None and not isinstance(self.founding_date, str):
            self.founding_date = str(self.founding_date)

        if self.founding_location is not None and not isinstance(self.founding_location, PlaceId):
            self.founding_location = PlaceId(self.founding_location)

        super().__post_init__(**kwargs)


@dataclass
class Project(NamedThing):
    """
    An enterprise (potentially individual but typically collaborative), planned to achieve a particular aim.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Project
    class_class_curie: ClassVar[str] = "schema:Project"
    class_name: ClassVar[str] = "Project"
    class_model_uri: ClassVar[URIRef] = M.Project

    id: Union[str, ProjectId] = None
    start_date: Optional[Union[str, XSDDate]] = None
    end_date: Optional[Union[str, XSDDate]] = None
    is_current: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProjectId):
            self.id = ProjectId(self.id)

        if self.start_date is not None and not isinstance(self.start_date, XSDDate):
            self.start_date = XSDDate(self.start_date)

        if self.end_date is not None and not isinstance(self.end_date, XSDDate):
            self.end_date = XSDDate(self.end_date)

        if self.is_current is not None and not isinstance(self.is_current, Bool):
            self.is_current = Bool(self.is_current)

        super().__post_init__(**kwargs)


@dataclass
class Product(NamedThing):
    """
    Any offered product or service. For example: Managed Kubernetes, FIT-Connect, OK.Finanzen, owi21
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Product
    class_class_curie: ClassVar[str] = "schema:Product"
    class_name: ClassVar[str] = "Product"
    class_model_uri: ClassVar[URIRef] = M.Product

    id: Union[str, ProductId] = None
    start_date: Optional[Union[str, XSDDate]] = None
    end_date: Optional[Union[str, XSDDate]] = None
    is_current: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProductId):
            self.id = ProductId(self.id)

        if self.start_date is not None and not isinstance(self.start_date, XSDDate):
            self.start_date = XSDDate(self.start_date)

        if self.end_date is not None and not isinstance(self.end_date, XSDDate):
            self.end_date = XSDDate(self.end_date)

        if self.is_current is not None and not isinstance(self.is_current, Bool):
            self.is_current = Bool(self.is_current)

        super().__post_init__(**kwargs)


@dataclass
class Concept(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = M.Concept
    class_class_curie: ClassVar[str] = "m:Concept"
    class_name: ClassVar[str] = "Concept"
    class_model_uri: ClassVar[URIRef] = M.Concept

    id: Union[str, ConceptId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConceptId):
            self.id = ConceptId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class HasAliases(YAMLRoot):
    """
    A mixin applied to any class that can have aliases/alternateNames
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = M.HasAliases
    class_class_curie: ClassVar[str] = "m:HasAliases"
    class_name: ClassVar[str] = "HasAliases"
    class_model_uri: ClassVar[URIRef] = M.HasAliases

    aliases: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=M.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=M.name, domain=None, range=Optional[str])

slots.legal_form = Slot(uri=M.legal_form, name="legal_form", curie=M.curie('legal_form'),
                   model_uri=M.legal_form, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=M.description, domain=None, range=Optional[str])

slots.image = Slot(uri=SCHEMA.image, name="image", curie=SCHEMA.curie('image'),
                   model_uri=M.image, domain=None, range=Optional[str])

slots.email = Slot(uri=SCHEMA.email, name="email", curie=SCHEMA.curie('email'),
                   model_uri=M.email, domain=None, range=Optional[str])

slots.url = Slot(uri=SCHEMA.URL, name="url", curie=SCHEMA.curie('URL'),
                   model_uri=M.url, domain=None, range=Optional[str])

slots.is_current = Slot(uri=M.is_current, name="is_current", curie=M.curie('is_current'),
                   model_uri=M.is_current, domain=None, range=Optional[Union[bool, Bool]])

slots.in_location = Slot(uri=M.in_location, name="in_location", curie=M.curie('in_location'),
                   model_uri=M.in_location, domain=None, range=Optional[Union[str, PlaceId]])

slots.address = Slot(uri=M.address, name="address", curie=M.curie('address'),
                   model_uri=M.address, domain=None, range=Optional[Union[dict, Address]])

slots.related_to = Slot(uri=M.related_to, name="related_to", curie=M.curie('related_to'),
                   model_uri=M.related_to, domain=None, range=Optional[str])

slots.type = Slot(uri=M.type, name="type", curie=M.curie('type'),
                   model_uri=M.type, domain=None, range=Optional[str])

slots.street = Slot(uri=M.street, name="street", curie=M.curie('street'),
                   model_uri=M.street, domain=None, range=Optional[str])

slots.city = Slot(uri=M.city, name="city", curie=M.curie('city'),
                   model_uri=M.city, domain=None, range=Optional[str])

slots.mission_statement = Slot(uri=M.mission_statement, name="mission_statement", curie=M.curie('mission_statement'),
                   model_uri=M.mission_statement, domain=None, range=Optional[str])

slots.founding_date = Slot(uri=M.founding_date, name="founding_date", curie=M.curie('founding_date'),
                   model_uri=M.founding_date, domain=None, range=Optional[str])

slots.founding_location = Slot(uri=M.founding_location, name="founding_location", curie=M.curie('founding_location'),
                   model_uri=M.founding_location, domain=None, range=Optional[Union[str, PlaceId]])

slots.postal_code = Slot(uri=M.postal_code, name="postal_code", curie=M.curie('postal_code'),
                   model_uri=M.postal_code, domain=None, range=Optional[str])

slots.start_date = Slot(uri=PROV.startedAtTime, name="start_date", curie=PROV.curie('startedAtTime'),
                   model_uri=M.start_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.duration = Slot(uri=M.duration, name="duration", curie=M.curie('duration'),
                   model_uri=M.duration, domain=None, range=Optional[float])

slots.end_date = Slot(uri=PROV.endedAtTime, name="end_date", curie=PROV.curie('endedAtTime'),
                   model_uri=M.end_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.organizations = Slot(uri=M.organizations, name="organizations", curie=M.curie('organizations'),
                   model_uri=M.organizations, domain=None, range=Optional[Union[Dict[Union[str, OrganizationId], Union[dict, Organization]], List[Union[dict, Organization]]]])

slots.hasAliases__aliases = Slot(uri=M.aliases, name="hasAliases__aliases", curie=M.curie('aliases'),
                   model_uri=M.hasAliases__aliases, domain=None, range=Optional[Union[str, List[str]]])