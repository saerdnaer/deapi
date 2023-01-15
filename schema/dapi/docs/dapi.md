
# de-meta


**metamodel version:** 1.7.0

**version:** None


Information about public organisations, their projects, products & service providers based on [schema.org](http://schema.org)


### Classes

 * [Address](Address.md)
 * [Event](Event.md)
 * [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity
     * [Concept](Concept.md)
     * [Organization](Organization.md) - An organization such as a government, political party, state, municipality, city, NGO, company, university or any other association
     * [Product](Product.md) - Any offered product or service. For example: Managed Kubernetes, FIT-Connect, OK.Finanzen, owi21 
     * [Project](Project.md) - An enterprise (potentially individual but typically collaborative), planned to achieve a particular aim.
 * [Place](Place.md)
 * [Relationship](Relationship.md)

### Mixins

 * [HasAliases](HasAliases.md) - A mixin applied to any class that can have aliases/alternateNames
 * [WithLocation](WithLocation.md)

### Slots

 * [address](address.md) - The address at which a organization has its headquarters
 * [city](city.md)
 * [description](description.md)
 * [duration](duration.md)
 * [email](email.md)
 * [end_date](end_date.md)
 * [founding_date](founding_date.md)
 * [founding_location](founding_location.md)
 * [➞aliases](hasAliases__aliases.md)
 * [id](id.md)
 * [image](image.md)
 * [in_location](in_location.md)
 * [is_current](is_current.md)
 * [legal_form](legal_form.md)
 * [mission_statement](mission_statement.md)
 * [name](name.md)
 * [organizations](organizations.md)
 * [postal_code](postal_code.md)
 * [related_to](related_to.md)
 * [start_date](start_date.md)
 * [street](street.md)
 * [type](type.md)
 * [url](url.md)

### Enums


### Subsets

 * [BasicSubset](BasicSubset.md) - A subset of the schema that handles basic information

### Types


#### Built in

 * **Bool**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
