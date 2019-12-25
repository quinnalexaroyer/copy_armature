# copy_armature
A Python script for Blender which replaces an object's armature with another and adjusts modifiers, constraints, and drivers

This script assumes you have an armature object called "base". If you want to use a different name, you can change the line `baseName = "base"` at the top of the program. It also assumes that any objects associated with a character will begin with the character's name followed by a period, and then any remaining text. It also assumes that a character's armature object ends in ".arm".

This script makes a copy of the armature called "base" for each character to replace the armature it already has. It does not delete the old armature. Also, hook modifiers may need to be recalculated after running this script.
