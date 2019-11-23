## Exercise 8: Widgets and Gizmos

weightOfEachWidget = 75
weightOfEachGizmo = 112

widgets = int(input("Enter the number of widgets: "))
gizmos = int(input("Enter the number of gizmos: "))

widgetsWeight = widgets * weightOfEachWidget
gizmosWeight = gizmos * weightOfEachGizmo
totalWeight = widgetsWeight + gizmosWeight

print(f"The total weight for {widgets} widgets and {gizmos} gizmos is {totalWeight} grams.")
