---
fields:
  - name: Ingredients
    type: MultiFile
    options:
      dvQueryString: dv.pages('"Ingredients"')
    path: ""
    id: dGZ0rW
  - name: Day
    type: CanvasGroup
    options:
      groupColors:
        - "5"
      groupLabels: []
      canvasPath: Meal Plan.canvas
    path: ""
    id: YtQf2K
  - name: Cost
    type: Formula
    options:
      autoUpdate: false
      formula: |-
        function(){
            const ingredients = current.Ingredients;
            let result = 0;
            if(Array.isArray(ingredients)){
                result = ingredients
                    .map(ingredient => dv.page(ingredient.path))
                    .map(p => parseFloat(p.CostPerMeal) || 0 )
                    .reduce((a, c) => a+c, 0);
            }else{
                result = dv.page(ingredients.path).CostPerMeal || 0
            }
            return Math.round(result*100)/100;
        }()
    path: ""
    id: Z0SPYt
  - name: Time
    type: CanvasGroup
    options:
      groupColors:
        - "4"
      groupLabels: []
      canvasPath: Meal Plan.canvas
    path: ""
    id: U5FOfZ
version: "2.10"
limit: 20
mapWithTag: false
icon: scroll-text
tagNames: 
filesPaths: 
bookmarksGroups: 
excludes: 
extends: 
savedViews:
  - name: Recipes
    sorters: []
    filters:
      - name: file
        query: ""
      - name: Ingredients
        query: ""
      - name: Day
        query: ""
      - name: Cost
        query: __existing__
    columns:
      - name: file
        hidden: false
        position: 0
      - name: Ingredients
        hidden: false
        position: 2
      - name: Day
        hidden: true
        position: 3
      - name: Cost
        hidden: false
        position: 1
favoriteView: Recipes
fieldsOrder:
  - U5FOfZ
  - Z0SPYt
  - YtQf2K
  - dGZ0rW
---
