# Bitto

## What

Bitto is a template project to setup a basic framework for the development of a blender render engine.

In addition to the offcial example presented [here](https://docs.blender.org/api/current/bpy.types.RenderEngine.html), Bitto is a more complete framework which contains the scene element output, UI element setup and the shading network creation.

As for the name, Bitto is coined from **B**lender and D**itto**, hope it can be transformed into any render engine addon you would like to create.

## Why

I've created a blender render engine addon for PBRT-v3, named [btop](https://github.com/joeyskeys/btop).

This experience gave me the fundamental knowledge of developing a blender render engine addon. When it comes to the time I need to write a addon for my own [renderer](https://github.com/joeyskeys/kazen_proto), which is still in the early stage of development, I found it's total duplicated work since the data you need to get out from blender is the same and the GUI you need to setup in blender shares the similar pattern.

So I decided to write this template as a summarize for the development of such kind blender addon and hope it can help others to do the same kind of work easily.

## How

A render engine addon mainly contains four parts.

### Scene Data Output

This part controls how your render engine converts the scene data into something that your renderer can consume. This part of code lives in [io/](https://github.com/joeyskeys/bitto/tree/main/io).

The naming of files is straight forward and you have to write your own code for **two interfaces** for each data type. Namely:
- write_description
- feed_api

write_description is the interface to write out the scene description that your renderer can consume. Note the only parameter for this interface defined here is handler, a file IO handler for you to write out the data.

feed_api is the interface that is used to feed the data directly into your renderer APIs, which will be python bindings to your renderer's c++ data IO interfaces.

Besides these two methods, there're some data fetching methods for you to get data from blender:

- get_props
- type specific interface

get_props is a common interface to fetch the custom properties that you defined for your renderer. These properties will be stored into blender types and is heavily related to the GUI setup which will be introduced later. What you need to know here is, the custom property can be fetched this way(take camera for example):

```
props = camera_io.get_props()
your_custom_property_value = props.your_property_name
```

type specific interface is some useful utility method for you to get some essential properties from blender, saving your time to look into the documentation and help find the data you need. Take camera class's get_camera_infos for example, it simply returns the eye position, look to vector and the up vector of the camera.

### GUI for Custom Properties

Your renderer may provide quite a lot properties on each type of objects in the scene, which will require you to add corresponding GUIs in the blender panel to let your user to adjust these properties.

To add these properties you need to:

1. Define your property group class by inheriting [bpy.types.PropertyGroup](https://docs.blender.org/api/current/bpy.types.PropertyGroup.html);
2. Register the property group class, then create a instance and store it into a proper place;
3. Define your GUI panel class by inheriting [bpy.types.Panel](https://docs.blender.org/api/current/bpy.types.Panel.html), define your draw method to properly draw the GUI of your properties with the built-in GUI widgets;
4. Register the GUI class.

Same workflow for every property which make it very boring to write duplicated codes. Luckily, Bitto provides a much simpler way of doing it.

All you need to do is to define your properties in the [config.py](https://github.com/joeyskeys/bitto/blob/main/config.py) and then Bitto will take care of the rest.

All the GUI panel class is predefined. If you're not happy with the default draw method, just checkout the corresponding code modify it at your will.

### Shading Network

Most hard part of a render engine addon is to write the shading nodes and then take advantage of the blender node system since APIs of this part is not well documented.

Thanks to the work of [blenderseed](https://github.com/appleseedhq/blenderseed) and [LuxCoreRender](https://github.com/LuxCoreRender/BlendLuxCore), Bitto is able to summarize the relating code and provide the user quite a ease to create your own shading network system in blender.

### Render Engine

The last and the most important part of a render engine addon is the render engine class itself.

Bitto provides you the basic interface where you need to fill in your own code and make your render working properly when you hit F12.

## About config.py

Besides custom property definition, there're some other properties you could customize in config.py, check the file to find out. More comments will be added to further explain the variables in it.

## Utilities

Some utilities live in the [utils/](https://github.com/joeyskeys/bitto/tree/main/utils) folder. These codes aren't neccessary part of a render engine but you may find it handy. One good example is the triangulation function provided in [triangulate.py](https://github.com/joeyskeys/bitto/blob/main/utils/triangulate.py). Your renderer may only support triangle meshes but meshes in the scene could possibly contain ngons. Run it as a pre-render pass to validate your scene data and then feed it into your renderer.

## Example

[bazen](https://github.com/joeyskeys/bazen) is a live example of create a render engine addon by applying Bitto, checkout the code for details.