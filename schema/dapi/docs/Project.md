
# Class: Project


An enterprise (potentially individual but typically collaborative), planned to achieve a particular aim.

URI: [m:Project](https://codeforde.org/schema/metaProject)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing]^-[Project&#124;start_date:date%20%3F;end_date:date%20%3F;is_current:boolean%20%3F;id(i):string;name(i):string%20%3F;description(i):string%20%3F;image(i):string%20%3F;url(i):string%20%3F],[NamedThing])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing]^-[Project&#124;start_date:date%20%3F;end_date:date%20%3F;is_current:boolean%20%3F;id(i):string;name(i):string%20%3F;description(i):string%20%3F;image(i):string%20%3F;url(i):string%20%3F],[NamedThing])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity

## Attributes


### Own

 * [start_date](start_date.md)  <sub>0..1</sub>
     * Range: [Date](types/Date.md)
 * [end_date](end_date.md)  <sub>0..1</sub>
     * Range: [Date](types/Date.md)
 * [is_current](is_current.md)  <sub>0..1</sub>
     * Range: [Boolean](types/Boolean.md)

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
| **Mappings:** | | schema:Project |

