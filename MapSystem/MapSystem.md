# Map System
Map System is used to capture maps and display them on the screen. It handles player position, zoom, and points of interest.

(Examples are in the plugin content in the chat level)

![Map System](./MapSystem.png)

## How to Use
1. Drop a Map Volume actor into your level.
2. Set or create a render target and assign it to the Map Volume Capture Target (You have to size your render target based on your needs).
3. Open your render target and move around and play with the Ortho Width variable until you capture the desired map image.
4. Once capturing is done, you can right-click the render target and create an image texture (or you can use the render target directly as the map image, however, it's not recommended for most games).
5. You can also customize and stylize your map by adding a post-process material to the map capture.
6. Once the static image is generated, you can export it to your favorite image editor to draw and customize on top of it or use it as-is.

## Add Widget
1. Make a widget and add the Map Widget to it.
2. You need to set the map texture and also set the reference to the map volume in the level for this map if you have more than one map volume in this level (the map volume is used for automatic position calculations).