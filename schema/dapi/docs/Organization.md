
# Class: Organization


An organization such as a government, political party, state, municipality, city, NGO, company, university or any other association

URI: [m:Organization](https://codeforde.org/schema/metaOrganization)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Place],[Place]<founding_location%200..1-%20[Organization&#124;legal_form:string%20%3F;mission_statement:string%20%3F;founding_date:string%20%3F;id(i):string;name(i):string%20%3F;description(i):string%20%3F;image(i):string%20%3F;url(i):string%20%3F],[Address]<address%200..1-++[Organization],[NamedThing]^-[Organization],[NamedThing],[Address])](https://yuml.me/diagram/nofunky;dir:TB/class/[Place],[Place]<founding_location%200..1-%20[Organization&#124;legal_form:string%20%3F;mission_statement:string%20%3F;founding_date:string%20%3F;id(i):string;name(i):string%20%3F;description(i):string%20%3F;image(i):string%20%3F;url(i):string%20%3F],[Address]<address%200..1-++[Organization],[NamedThing]^-[Organization],[NamedThing],[Address])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity

## Referenced by Class

 *  **None** *[organizations](organizations.md)*  <sub>0..\*</sub>  **[Organization](Organization.md)**

## Attributes


### Own

 * [legal_form](legal_form.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [address](address.md)  <sub>0..1</sub>
     * Description: The address at which a organization has its headquarters
     * Range: [Address](Address.md)
 * [mission_statement](mission_statement.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [founding_date](founding_date.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [founding_location](founding_location.md)  <sub>0..1</sub>
     * Range: [Place](Place.md)

### Inherited from NamedThing:

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [name](name.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [image](image.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [url](url.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | schema:Organization |

