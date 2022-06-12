# This file MUST be configured in order for the code to run properly

# Make sure you put all your input images into an 'assets' folder. 
# Each layer (or category) of images must be put in a folder of its own.

# CONFIG is an array of objects where each object represents a layer
# THESE LAYERS MUST BE ORDERED.

# Each layer needs to specify the following
# 1. id: A number representing a particular layer
# 2. name: The name of the layer. Does not necessarily have to be the same as the directory name containing the layer images.
# 3. directory: The folder inside assets that contain traits for the particular layer
# 4. required: If the particular layer is required (True) or optional (False). The first layer must always be set to true.
# 5. rarity_weights: Denotes the rarity distribution of traits. It can take on three types of values.
#       - None: This makes all the traits defined in the layer equally rare (or common)
#       - "random": Assigns rarity weights at random. 
#       - array: An array of numbers where each number represents a weight. 
#                If required is True, this array must be equal to the number of images in the layer directory. The first number is  the weight of the first image (in alphabetical order) and so on...
#                If required is False, this array must be equal to one plus the number of images in the layer directory. The first number is the weight of having no image at all for this layer. The second number is the weight of the first image and so on...

# Be sure to check out the tutorial in the README for more details.                

CONFIG = [
    {
        'id': 0,
        'name': 'KIKIBG',
        'directory': 'KIKIBG',
        'required': True,
        'rarity_weights':  "random",
    },
    {
        'id': 1,
        'name': 'Effect',
        'directory': 'effect',
        'required': True,
        'rarity_weights':[10,5,3,100,34],
    },
    {
        'id': 2,
        'name': 'hairback',
        'directory': 'hairback',
        'required': True,
        'rarity_weights': "random",
    },
     {
        'id': 3,
        'name': 'Body',
        'directory': 'Body',
        'required': True,
        'rarity_weights': None,
    },
      {
        'id': 4,
        'name': 'shirt',
        'directory': 'shirt',
        'required': True,
        'rarity_weights': "random",
    },
    {
        'id': 5,
        'name': 'Head',
        'directory': 'Head',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 6,
        'name': 'mouth',
        'directory': 'mouth',
        'required': True,
        'rarity_weights': "random",
    },
    {
        'id': 7,
        'name': 'eye',
        'directory': 'eye',
        'required': True,
        'rarity_weights': "random",
    },
    {
        'id': 8,
        'name': 'hand',
        'directory': 'hand',
        'required': True,
        'rarity_weights':None,
    },
    {
        'id': 9,
        'name': 'hairfront',
        'directory': 'hairfront',
        'required': True,
        'rarity_weights': "random",
    },
     {
        'id': 10,
        'name': 'Head_Hat',
        'directory': 'Head_Hat',
        'required': True,
        'rarity_weights': "random",
    },
     {
        'id': 11,
        'name': 'eye_Hat',
        'directory': 'eye_Hat',
        'required': True,
        'rarity_weights': "random",
    },
     {
        'id': 12,
        'name': 'mouth_Hat',
        'directory': 'mouth_Hat',
        'required': True,
        'rarity_weights': "random",
    },
    
   
]
