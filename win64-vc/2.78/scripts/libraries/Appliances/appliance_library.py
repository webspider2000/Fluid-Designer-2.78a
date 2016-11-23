"""
Microvellum 
Appliances 
Stores all of the Logic, Product, and Insert Class definitions for appliances
"""

import os
from mv import fd_types, unit
from . import appliance_properties

ASSEMBLY_PATH = os.path.join(os.path.dirname(__file__),"Parametric Appliances")
MATERIAL_FILE = os.path.join(os.path.dirname(__file__),"materials","materials.blend")

WALL_APPLIANCE_PATH = os.path.join(os.path.dirname(__file__),"Wall Appliances")
COOKTOP_APPLIANCE_PATH = os.path.join(os.path.dirname(__file__),"Cooktops")
SINK_APPLIANCE_PATH = os.path.join(os.path.dirname(__file__),"Sinks")
FAUCET_APPLIANCE_PATH = os.path.join(os.path.dirname(__file__),"Faucets")

def get_file_name(path):
    file_name = os.path.basename(path)
    return os.path.splitext(file_name)[0]

class Parametric_Wall_Appliance(fd_types.Assembly):
    
    library_name = appliance_properties.LIBRARY_FOLDER_NAME
    type_assembly = "PRODUCT"
    
    """ Path to blend file that contains a group of the appliance """
    appliance_path = ""
    
    """ Set to True if you want to add a countertop to this appliance """
    add_countertop = False
    
    def draw(self):
        self.create_assembly()
        dim_x = self.get_var("dim_x")
        dim_z = self.get_var("dim_z")
        dim_y = self.get_var("dim_y")
        assembly = self.add_assembly(file_path = self.appliance_path)
        assembly.set_name(get_file_name(self.appliance_path))
        assembly.x_dim('dim_x',[dim_x])
        assembly.y_dim('dim_y',[dim_y])
        assembly.z_dim('dim_z',[dim_z])
        assembly.assign_material("Chrome",MATERIAL_FILE,"Chrome")
        assembly.assign_material("Stainless Steel",MATERIAL_FILE,"Stainless Steel")
        assembly.assign_material("Black Anodized Metal",MATERIAL_FILE,"Black Anodized Metal")
        
#         if self.add_ctop:
#             self.add_tab(name="Counter Top Options",tab_type='VISIBLE')
#             self.add_prompt(name="Countertop Overhang Front",prompt_type='DISTANCE',value=unit.inch(1),tab_index=0)
#             self.add_prompt(name="Countertop Overhang Back",prompt_type='DISTANCE',value=unit.inch(0),tab_index=0)
#             self.add_prompt(name="Countertop Overhang Left",prompt_type='DISTANCE',value=unit.inch(0),tab_index=0)
#             self.add_prompt(name="Countertop Overhang Right",prompt_type='DISTANCE',value=unit.inch(0),tab_index=0)
#             Countertop_Overhang_Front = self.get_var('Countertop Overhang Front')
#             Countertop_Overhang_Left = self.get_var('Countertop Overhang Left')
#             Countertop_Overhang_Right = self.get_var('Countertop Overhang Right')
#             Countertop_Overhang_Back = self.get_var('Countertop Overhang Back')

#             ctop = LM_countertops.Straight_Countertop()
#             ctop.draw()
#             ctop.obj_bp.mv.type_group = 'INSERT'
#             ctop.obj_bp.parent = self.obj_bp
#             ctop.x_loc('-Countertop_Overhang_Left',[Countertop_Overhang_Left])
#             ctop.y_loc('Countertop_Overhang_Back',[Countertop_Overhang_Back])
#             ctop.z_loc('dim_z',[dim_z])
#             ctop.x_rot(value = 0)
#             ctop.y_rot(value = 0)
#             ctop.z_rot(value = 0)
#             ctop.x_dim('dim_x+Countertop_Overhang_Left+Countertop_Overhang_Right',[dim_x,Countertop_Overhang_Left,Countertop_Overhang_Right])
#             ctop.y_dim('dim_y-Countertop_Overhang_Front-Countertop_Overhang_Back',[dim_y,Countertop_Overhang_Front,Countertop_Overhang_Back])
#             ctop.z_dim(value = unit.inch(4))        
        
class Countertop_Appliance(fd_types.Assembly):
    
    library_name = appliance_properties.LIBRARY_FOLDER_NAME
    type_assembly = "NONE"
    
    """ Path to blend file that contains a group of the appliance """
    appliance_path = ""
    drop_id = appliance_properties.LIBRARY_NAME_SPACE + ".place_countertop_appliance"

    def draw(self):
        self.create_assembly()
        dim_x = self.get_var("dim_x")
        dim_z = self.get_var("dim_z")
        dim_y = self.get_var("dim_y")
        assembly = self.add_assembly(file_path = self.appliance_path)
        assembly.set_name(get_file_name(self.appliance_path))
        assembly.x_dim('dim_x',[dim_x])
        assembly.y_dim('dim_y',[dim_y])
        assembly.z_dim('dim_z',[dim_z])
        assembly.assign_material("Chrome",MATERIAL_FILE,"Chrome")
        assembly.assign_material("Stainless Steel",MATERIAL_FILE,"Stainless Steel")
        assembly.assign_material("Black Anodized Metal",MATERIAL_FILE,"Black Anodized Metal")        

class Object_Appliance(fd_types.Assembly):
    
    library_name = appliance_properties.LIBRARY_FOLDER_NAME
    type_assembly = "NONE"
    
    """ Path to blend file that contains a group of the appliance """
    appliance_path = ""
    
    drop_id = appliance_properties.LIBRARY_NAME_SPACE + ".place_appliance_object"

    def draw(self):
        self.create_assembly()
#         dim_x = self.get_var("dim_x")
#         dim_z = self.get_var("dim_z")
#         dim_y = self.get_var("dim_y")
        assembly = self.add_object(file_path = self.appliance_path)
        assembly.set_name(get_file_name(self.appliance_path))
#         assembly.x_dim('dim_x',[dim_x])
#         assembly.y_dim('dim_y',[dim_y])
#         assembly.z_dim('dim_z',[dim_z])
#         assembly.assign_material("Chrome",MATERIAL_FILE,"Chrome")
#         assembly.assign_material("Stainless Steel",MATERIAL_FILE,"Stainless Steel")
#         assembly.assign_material("Black Anodized Metal",MATERIAL_FILE,"Black Anodized Metal")              
        
#---------PRODUCT: PARAMETRIC APPLIANCES
        
class PRODUCT_Refrigerator(Parametric_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Appliances"
        self.assembly_name = "Refrigerator"
        self.width = unit.inch(36)
        self.height = unit.inch(84)
        self.depth = unit.inch(27)
        self.appliance_path = os.path.join(WALL_APPLIANCE_PATH,"Professional Refrigerator Generic.blend")
        
class PRODUCT_Range(Parametric_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Appliances"
        self.assembly_name = "Range"
        self.width = unit.inch(30)
        self.height = unit.inch(42)
        self.depth = unit.inch(28)
        self.appliance_path = os.path.join(WALL_APPLIANCE_PATH,"Professional Gas Range Generic.blend")
        
class PRODUCT_Dishwasher(Parametric_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Appliances"
        self.assembly_name = "Dishwasher"
        self.width = unit.inch(24)
        self.height = unit.inch(34)
        self.depth = unit.inch(23)
        self.appliance_path = os.path.join(WALL_APPLIANCE_PATH,"Professional Dishwasher Generic.blend")
        
class PRODUCT_Range_Hood(Parametric_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Appliances"
        self.assembly_name = "Range Hood"
        self.width = unit.inch(30)
        self.height = unit.inch(14)
        self.depth = unit.inch(12.5)
        self.appliance_path = os.path.join(WALL_APPLIANCE_PATH,"Wall Mounted Range Hood 01.blend")
        self.height_above_floor = unit.inch(60)
    
class PRODUCT_Wolf_CG152_Transitional_Gas_Cooktop(Countertop_Appliance):
    
    def __init__(self):
        self.category_name = "Appliances"
        self.width = unit.inch(15)
        self.height = unit.inch(5.25)
        self.depth = unit.inch(21)
        self.appliance_path = os.path.join(COOKTOP_APPLIANCE_PATH,"Wolf CG152 Transitional Gas Cooktop.blend")

class PRODUCT_Bathroom_Faucet(Object_Appliance):
    
    def __init__(self):
        self.category_name = "Appliances"
        self.width = unit.inch(15)
        self.height = unit.inch(5.25)
        self.depth = unit.inch(21)
        self.appliance_path = os.path.join(FAUCET_APPLIANCE_PATH,"Bathroom Faucet.blend")
        