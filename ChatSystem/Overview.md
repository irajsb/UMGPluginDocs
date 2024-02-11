# Overview

Although the system is usable as it is, I would like to paint a picture of how it works because the main key point of this system is its modularity and ability to combine the parts to achieve the desired result. Here is a short description of important parts of each system:

## Chat System
- **Chat Component**: A component handling transportation of messages and pings (This component is attached to PlayerState BP).
- **Chat Widget**: The widget that shows the messages.

## Ping System
- **Ping Actor**: An actor representing the ping spawned in the world. The widgets and effects can be attached to this for visual representation.
- **Titan Widget Component**: An optional widget which will remain on the corners of the screen when the ping is not in the view.

## Map System
- **Map POI (Point of Interest)**: A component that can be attached to Pings, Player, and any other kind of Blueprints. It receives a widget input and will draw that widget on top of the map in the correct position.
- **Map Volume**: A placeable box volume. Captures that map texture which can be used directly or to be moved and edited in external photo editors. Map volume will also automatically calculate correct positions of POIs mathematically which is a very complex process otherwise.
- **Map Widget**: Widget that will draw the final map. Using the map material and volume for the input data.

For more information, you can visit the following links:
- [Map System Documentation](https://irajsb.github.io/UMGPluginDocs/MapSystem/MapSystem)
- [Ping System Documentation](https://irajsb.github.io/UMGPluginDocs/ChatSystem/PingSystem)
- [Chat Component Documentation](https://irajsb.github.io/UMGPluginDocs/ChatSystem/ChatComponent)
