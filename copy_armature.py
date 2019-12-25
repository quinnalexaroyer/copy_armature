import bpy

baseName = "base"
baseArmObj = bpy.data.objects[baseName]
baseArm = baseArmObj.data
for i in bpy.data.objects:
	if i.name[-4:] == ".arm":
		a = baseArm.copy()
		bpy.ops.object.add(type="ARMATURE", location=i.location, rotation=i.rotation_euler)
		o = bpy.context.active_object
		o.data = a
		chrName = i.name[:-4]
		for j in [k for k in bpy.data.objects if k.name == chrName or k.name[:k.name.find(".")] == chrName]:
			if hasattr(j, "modifiers"):
				for k in j.modifiers:
					for k2 in dir(k):
						if getattr(k, k2) == i:
							setattr(k, k2, o)
			if hasattr(j, "constraints"):
				for k in j.constraints:
					for k2 in dir(k):
						if getattr(k, k2) == i:
							setattr(k, k2, o)
			if j.animation_data is not None:
				for d in j.animation_data.drivers:
					for v in d.driver.variables:
						for t in v.targets:
							if t.id == i:
								t.id = o
