
# Class: NamedThing


A generic grouping for any identifiable entity

URI: [m:NamedThing](https://codeforde.org/schema/metaNamedThing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Project],[Product],[Organization],[NamedThing&#124;id:string;name:string%20%3F;description:string%20%3F;image:string%20%3F;url:string%20%3F]^-[Project],[NamedThing]^-[Product],[NamedThing]^-[Organization],[NamedThing]^-[Concept],[Concept])](https://yuml.me/diagram/nofunky;dir:TB/class/[Project],[Product],[Organization],[NamedThing&#124;id:string;name:string%20%3F;description:string%20%3F;image:string%20%3F;url:string%20%3F]^-[Project],[NamedThing]^-[Product],[NamedThing]^-[Organization],[NamedThing]^-[Concept],[Concept])

## Children

 * [Concept](Concept.md)
 * [Organization](Organization.md) - An organization such as a government, political party, state, municipality, city, NGO, company, university or any other association
 * [Product](Product.md) - Any offered product or service. For example: Managed Kubernetes, FIT-Connect, OK.Finanzen, owi21 
 * [Project](Project.md) - An enterprise (potentially individual but typically collaborative), planned to achieve a particular aim.

## Referenced by Class


## Attributes


### Own

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
| **Close Mappings:** | | schema:Thing |

