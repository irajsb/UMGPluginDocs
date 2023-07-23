# This Radial Menu dynamicaly can accept children without any need for building static textures.

![](./RadialMenu.png)

# How To Use
- Drag radial menu to your widget.
- Add children by dragging and dropping into menu (Buttons can be added as well if you want to have hovering effects simulated. Buttons will be cosmetic only)
- Pass input to radial menu using one of these functions
![](./RadialMenuFuncs.png)
- get Output using this func (Returns selected index and widget)
![](./RadialResult.png)

# Variables and funtions



| Name                      | Type                    | Description                                                                                                 |
| :------------------------ | :----------------------: | :---------------------------------------------------------------------------------------------------------  |
| RadialMenuBaseMaterial    | UMaterialInterface*     | The material used for the RadialMenu base.                                                                  |
| SelectorColor             | FLinearColor            | Foreground color used for the selector.                                                                     |
| BackgroundColor           | FLinearColor            | Background color used for the RadialMenu.                                                                   |
| DividerOpacity            | float                   | Opacity of the divider between each element.                                                                |
| OptionsPadding            | float                   | Padding for options relative to the widget size.                                                            |
| BackgroundPadding         | float                   | Background padding relative to the widget size.                                                             |
| SnapSelector              | bool                    | Determines if the selector should snap instead of transitioning smoothly.                                  |
| HideSelectorWhenNotHovered| bool                    | Determines if the selector should be visible only when hovered with the mouse.                            |
| BackgroundRotationOffset  | float                   | Rotation offset for the background (0-90 degrees, starting from top and clockwise). Default value is 0.0.   |
| SetSelectorColor          | Function        | Setter function to set the selector color.                                                                  |
| SetSelectorAngle          | Function        | Setter function to set the angle of the selector (0-360 degrees, starting from top and clockwise).         |
| SetSelectorAngleByIndex   | Function        | Setter function to set the selector angle based on an item index.                                          |
| SetSelectorAngleFromViewportPosition | Function | Setter function to calculate the angle from viewport position.                                           |
| GetElementUnderSelector   | Function,BlueprintPure | Getter function to get the element under the selector.                                                  |
| SetSelectorVisibility     | Function        | Setter function to set the visibility of the selector.                                                    |
| MouseDown                 | Event   | Event delegate triggered when a mouse button is pressed down.                                             |
| MouseMove                 | Event   | Event delegate triggered when the mouse is moved.                                                          |
| MouseUp                   | Event   | Event delegate triggered when a mouse button is released.                                                  |
| TouchStart                | Event   | Event delegate triggered when a touch event starts.                                                        |
| TouchMove                 | Event   | Event delegate triggered when a touch event is moved.                                                      |
| TouchEnd                  | Event   | Event delegate triggered when a touch event ends.                                                          |