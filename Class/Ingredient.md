---
fields:
  - name: Cost
    type: Object
    options: {}
    path: ""
    id: W9S2Cf
  - name: Shop - Rohlík
    type: Number
    options: {}
    path: W9S2Cf
    id: yIW1r4
  - name: Shop - Albert
    type: Number
    options: {}
    path: W9S2Cf
    id: wo9xwd
  - name: CostPerMeal
    type: Formula
    options:
      autoUpdate: false
      formula: Math.round(parseFloat(current.BoughtCost)/parseFloat(current.PotentialMeals)*100)/100
    path: ""
    id: skBl09
  - name: PotentialMeals
    type: Formula
    options:
      autoUpdate: false
      formula: Math.round(parseFloat(current.BoughtSize)/parseFloat(current.PortionSize)*100)/100
    path: ""
    id: BPGBcT
  - name: PortionSize
    type: Number
    options: {}
    path: ""
    id: ryXfpo
  - name: BoughtSize
    type: Number
    options: {}
    path: ""
    id: uuQNq1
  - name: BoughtCost
    type: Number
    options: {}
    path: ""
    id: Cf84Xf
  - name: Stock
    type: Boolean
    options: {}
    path: ""
    id: ySjtsP
version: "2.10"
limit: 20
mapWithTag: false
icon: apple
tagNames: 
filesPaths: 
bookmarksGroups: 
excludes: 
extends: 
savedViews: []
favoriteView: 
fieldsOrder:
  - ySjtsP
  - Cf84Xf
  - uuQNq1
  - ryXfpo
  - BPGBcT
  - skBl09
  - W9S2Cf
  - wo9xwd
  - yIW1r4
---
